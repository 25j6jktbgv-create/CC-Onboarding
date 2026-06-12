#!/usr/bin/env python3
"""Erzeugt die Curacon-Installationsanleitung als einseitiges A4-PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

OUT = "Installationsanleitung.pdf"
APP_URL = "https://25j6jktbgv-create.github.io/CC-Onboarding/"

RED    = HexColor("#C62635")
RED2   = HexColor("#A70C15")
BERRY  = HexColor("#971940")
AMBER  = HexColor("#E78A03")
YELLOW = HexColor("#F5BF06")
INK    = HexColor("#1C1C1E")
GRAY   = HexColor("#6B6B70")
LIGHT  = HexColor("#F6F3F1")
GREEN  = HexColor("#34C759")
BLUE   = HexColor("#007AFF")
WHITE  = HexColor("#FFFFFF")

W, H = A4          # 595.27 x 841.89
M = 48             # Seitenrand

c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Curacon Onboarding – Installationsanleitung")
c.setAuthor("Curacon")
c.setSubject("So installierst du die Onboarding-App auf deinem Smartphone")


def wrap(text, font, size, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


# ---------- Kopfband ----------
BAND_Y = 672
c.setFillColor(RED)
c.rect(0, BAND_Y, W, H - BAND_Y, stroke=0, fill=1)

# dezente Deko-Kreise (ans Hero-Design der App angelehnt), aufs Band geclippt
c.saveState()
p = c.beginPath()
p.rect(0, BAND_Y, W, H - BAND_Y)
c.clipPath(p, stroke=0, fill=0)
for (x, y, r, col, a) in [
    (90, 830, 46, WHITE, .08), (210, 690, 30, YELLOW, .10),
    (330, 815, 22, WHITE, .10), (430, 685, 42, AMBER, .10),
    (560, 805, 60, WHITE, .07), (285, 760, 12, AMBER, .12),
    (520, 700, 18, YELLOW, .09),
]:
    c.setFillColor(col)
    c.setFillAlpha(a)
    c.circle(x, y, r, stroke=0, fill=1)
c.restoreState()

# App-Icon rechts oben: weiße Kachel, rotes "C", Amber-Punkt
ix, iy, isz = W - M - 70, 718, 70
c.setFillColor(WHITE)
c.roundRect(ix, iy, isz, isz, 16, stroke=0, fill=1)
cx, cy, r = ix + isz / 2, iy + isz / 2, 21
c.setStrokeColor(RED)
c.setLineWidth(11)
c.setLineCap(1)
c.arc(cx - r, cy - r, cx + r, cy + r, startAng=38, extent=284)
c.setFillColor(AMBER)
c.circle(cx + r, cy, 5.5, stroke=0, fill=1)

# Kopfband-Texte
c.setFillColor(WHITE)
c.setFillAlpha(.9)
c.setFont("Helvetica-Bold", 9.5)
c.drawString(M, 792, "C U R A C O N   O N B O A R D I N G")
c.setFillAlpha(1)
c.setFont("Helvetica-Bold", 27)
c.drawString(M, 758, "So installierst du")
c.drawString(M, 726, "deine Onboarding-App")
c.setFillAlpha(.92)
c.setFont("Helvetica", 11.5)
c.drawString(M, 696, "In einer Minute auf dem Home-Bildschirm – ganz ohne App Store.")
c.setFillAlpha(1)

# ---------- Link-Box ----------
c.setFillColor(LIGHT)
c.roundRect(M, 622, W - 2 * M, 40, 12, stroke=0, fill=1)
c.setFillColor(RED)
c.setFont("Helvetica-Bold", 11)
c.drawString(M + 18, 637, "App-Link:")
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 12)
c.drawString(M + 92, 637, APP_URL)

# ---------- Mini-Icons ----------
def icon_compass(x, y):
    c.setStrokeColor(BLUE); c.setLineWidth(2)
    c.circle(x, y, 11, stroke=1, fill=0)
    c.setFillColor(BLUE)
    p = c.beginPath()
    p.moveTo(x + 5, y + 5); p.lineTo(x - 1.5, y - 1.5)
    p.lineTo(x - 5, y - 5); p.lineTo(x + 1.5, y + 1.5)
    p.close()
    c.drawPath(p, stroke=0, fill=1)

def icon_share(x, y):
    c.setStrokeColor(BLUE); c.setLineWidth(2); c.setLineCap(1); c.setLineJoin(1)
    c.roundRect(x - 8, y - 11, 16, 16, 3, stroke=1, fill=0)
    c.setFillColor(WHITE)                      # Lücke für den Pfeil
    c.rect(x - 3.5, y + 2.5, 7, 5, stroke=0, fill=1)
    c.setStrokeColor(BLUE)
    c.line(x, y - 3, x, y + 12)
    c.line(x, y + 12, x - 4, y + 8)
    c.line(x, y + 12, x + 4, y + 8)

def icon_plus(x, y):
    c.setStrokeColor(INK); c.setLineWidth(2); c.setLineCap(1)
    c.roundRect(x - 10, y - 10, 20, 20, 5, stroke=1, fill=0)
    c.line(x - 4.5, y, x + 4.5, y)
    c.line(x, y - 4.5, x, y + 4.5)

def icon_check(x, y):
    c.setFillColor(GREEN)
    c.circle(x, y, 11, stroke=0, fill=1)
    c.setStrokeColor(WHITE); c.setLineWidth(2.4); c.setLineCap(1); c.setLineJoin(1)
    c.line(x - 5, y, x - 1.5, y - 4)
    c.line(x - 1.5, y - 4, x + 5.5, y + 4.5)

# ---------- Schritt-Karten ----------
c.setFillColor(RED)
c.setFont("Helvetica-Bold", 12)
c.drawString(M, 594, "iPhone & iPad – Installation mit Safari")

steps = [
    ("Link in Safari öffnen",
     "Tippe den Link oben in die Adressleiste – wichtig: Safari verwenden, nicht Chrome.",
     icon_compass),
    ("Teilen-Symbol antippen",
     "Das Quadrat mit dem Pfeil nach oben, unten in der Mitte der Safari-Leiste.",
     icon_share),
    ("„Zum Home-Bildschirm“ wählen",
     "Im Teilen-Menü etwas nach unten scrollen, dann oben rechts mit „Hinzufügen“ bestätigen.",
     icon_plus),
    ("Fertig – einmal öffnen!",
     "Beim ersten Start kurz online sein, danach läuft die App auch komplett offline.",
     icon_check),
]

CARD_W, CARD_H, GAP = W - 2 * M, 62, 10
top = 584
for i, (title, desc, icon) in enumerate(steps):
    cy0 = top - CARD_H - i * (CARD_H + GAP)      # Unterkante der Karte
    mid = cy0 + CARD_H / 2
    c.setFillColor(LIGHT)
    c.roundRect(M, cy0, CARD_W, CARD_H, 12, stroke=0, fill=1)
    c.setFillColor(RED)
    c.circle(M + 28, mid, 13, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(M + 28, mid - 4.5, str(i + 1))
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(M + 52, cy0 + 36, title)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 10)
    for j, ln in enumerate(wrap(desc, "Helvetica", 10, CARD_W - 52 - 64)[:2]):
        c.drawString(M + 52, cy0 + 21 - j * 12, ln)
    icon(M + CARD_W - 30, mid)

# ---------- Untere Spalten ----------
COL_W = (CARD_W - 12) / 2
COL_H, COL_Y = 122, 146

def bullets(x0, y0, w, items, start_y):
    c.setFont("Helvetica", 9.5)
    yy = start_y
    for it in items:
        c.setFillColor(RED)
        c.rect(x0 + 16, yy + 2.5, 4, 4, stroke=0, fill=1)
        c.setFillColor(GRAY)
        for j, ln in enumerate(wrap(it, "Helvetica", 9.5, w - 44)):
            c.drawString(x0 + 28, yy - j * 11.5, ln)
            last = j
        yy -= 11.5 * (last + 1) + 7

for (x0, head, items) in [
    (M, "Android & Desktop", [
        "Android (Chrome): Drei-Punkte-Menü öffnen und „App installieren“ bzw. „Zum Startbildschirm hinzufügen“ wählen.",
        "Desktop (Chrome/Edge): Installations-Symbol rechts in der Adressleiste anklicken.",
    ]),
    (M + COL_W + 12, "Gut zu wissen", [
        "Läuft komplett offline – ideal unterwegs.",
        "Alle Daten bleiben auf deinem Gerät, kein Konto nötig.",
        "Updates meldet die App von selbst – einfach „Aktualisieren“ tippen.",
    ]),
]:
    c.setFillColor(LIGHT)
    c.roundRect(x0, COL_Y, COL_W, COL_H, 12, stroke=0, fill=1)
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 11.5)
    c.drawString(x0 + 16, COL_Y + COL_H - 24, head)
    bullets(x0, COL_Y, COL_W, items, COL_Y + COL_H - 46)

# ---------- Fußzeile ----------
c.setStrokeColor(HexColor("#E5E0DC"))
c.setLineWidth(1)
c.line(M, 108, W - M, 108)
c.setFillColor(GRAY)
c.setFont("Helvetica", 9)
c.drawCentredString(W / 2, 88, "Curacon Onboarding · Version v1 · Stand: Juni 2026")
c.setFont("Helvetica-Oblique", 9)
c.drawCentredString(W / 2, 73, "Sicherheit geben. Lösungen bieten.")

c.save()
print("OK ->", OUT)
