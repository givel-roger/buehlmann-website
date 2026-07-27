// Minimaler Formular-Handler fuer bs-luzern.ch (keine externen Abhaengigkeiten).
// Nimmt POST /api/kontakt entgegen, sendet per Brevo an info@bs-luzern.ch,
// legt zusaetzlich eine Sicherungskopie in /data/anfragen.log ab.
const http = require("http");
const https = require("https");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 8080;
const BREVO_API_KEY = process.env.BREVO_API_KEY || "";
const TO_EMAIL = process.env.TO_EMAIL || "info@bs-luzern.ch";
const TO_NAME = process.env.TO_NAME || "Bühlmann Söhne AG";
const FROM_EMAIL = process.env.FROM_EMAIL || "";     // verifizierter Brevo-Absender
const FROM_NAME = process.env.FROM_NAME || "Website bs-luzern.ch";
const LOG_FILE = process.env.LOG_FILE || "/data/anfragen.log";

function esc(s) {
  return String(s || "").replace(/[<>&]/g, (c) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;" }[c]));
}

function sendViaBrevo({ name, email, tel, msg }) {
  const html =
    `<p><strong>Neue Anfrage über bs-luzern.ch</strong></p>` +
    `<p><strong>Name:</strong> ${esc(name)}<br>` +
    `<strong>E-Mail:</strong> ${esc(email)}<br>` +
    `<strong>Telefon:</strong> ${esc(tel)}</p>` +
    `<p><strong>Nachricht:</strong><br>${esc(msg).replace(/\n/g, "<br>")}</p>`;
  const payload = JSON.stringify({
    sender: { email: FROM_EMAIL, name: FROM_NAME },
    to: [{ email: TO_EMAIL, name: TO_NAME }],
    replyTo: email ? { email: email, name: name || email } : undefined,
    subject: `Neue Anfrage über bs-luzern.ch${name ? " von " + name : ""}`,
    htmlContent: html,
  });
  return new Promise((resolve, reject) => {
    const req = https.request(
      {
        method: "POST",
        hostname: "api.brevo.com",
        path: "/v3/smtp/email",
        headers: {
          "api-key": BREVO_API_KEY,
          "content-type": "application/json",
          "content-length": Buffer.byteLength(payload),
        },
      },
      (res) => {
        let body = "";
        res.on("data", (d) => (body += d));
        res.on("end", () => {
          if (res.statusCode >= 200 && res.statusCode < 300) resolve(body);
          else reject(new Error(`Brevo ${res.statusCode}: ${body}`));
        });
      }
    );
    req.on("error", reject);
    req.write(payload);
    req.end();
  });
}

function backup(entry) {
  try {
    fs.mkdirSync(path.dirname(LOG_FILE), { recursive: true });
    fs.appendFileSync(LOG_FILE, JSON.stringify(entry) + "\n");
  } catch (e) {
    console.error("Backup fehlgeschlagen:", e.message);
  }
}

const server = http.createServer((req, res) => {
  if (req.method === "GET" && req.url === "/api/health") {
    res.writeHead(200, { "content-type": "text/plain" });
    return res.end("ok");
  }
  if (req.method !== "POST" || req.url !== "/api/kontakt") {
    res.writeHead(404, { "content-type": "text/plain" });
    return res.end("Not found");
  }
  let raw = "";
  req.on("data", (c) => {
    raw += c;
    if (raw.length > 20000) req.destroy(); // simpler Missbrauchsschutz
  });
  req.on("end", async () => {
    let data = {};
    try {
      data = raw.trim().startsWith("{") ? JSON.parse(raw) : Object.fromEntries(new URLSearchParams(raw));
    } catch (_) {}
    const name = (data.name || "").trim();
    const email = (data.email || "").trim();
    const tel = (data.tel || "").trim();
    const msg = (data.msg || data.nachricht || "").trim();
    // Honeypot gegen Bots
    if ((data.website || "").trim()) {
      res.writeHead(200, { "content-type": "application/json" });
      return res.end(JSON.stringify({ ok: true }));
    }
    if (!name || !msg || (!email && !tel)) {
      res.writeHead(400, { "content-type": "application/json" });
      return res.end(JSON.stringify({ ok: false, error: "Bitte Name, Nachricht und eine Kontaktangabe ausfüllen." }));
    }
    const entry = { ts: new Date().toISOString(), name, email, tel, msg };
    backup(entry);
    try {
      await sendViaBrevo({ name, email, tel, msg });
      res.writeHead(200, { "content-type": "application/json" });
      res.end(JSON.stringify({ ok: true }));
    } catch (e) {
      console.error("Versand fehlgeschlagen:", e.message);
      // Anfrage ist dank Backup nicht verloren
      res.writeHead(502, { "content-type": "application/json" });
      res.end(JSON.stringify({ ok: false, error: "Versand momentan nicht möglich. Bitte rufen Sie uns an: 041 269 88 50." }));
    }
  });
});

server.listen(PORT, () => console.log(`Formular-Backend läuft auf Port ${PORT}`));
