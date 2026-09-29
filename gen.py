import os, glob, base64
os.makedirs("assets", exist_ok=True)
for f in glob.glob("assets/*.svg"):
    os.remove(f)

FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','Helvetica Neue',Helvetica,Arial,sans-serif"

# Apple.com palette
THEMES = {
    "light": dict(tile="#F5F5F7", fg="#1D1D1F", sub="#6E6E73", link="#0066CC"),
    "dark":  dict(tile="#1D1D1F", fg="#F5F5F7", sub="#86868B", link="#2997FF"),
}

# Layout grid: every tile SVG is 1200 units wide (full) or 600 (half) and carries
# its own share of the 20-unit gutter, so rows line up edge to edge on GitHub.
W, GAP = 1200, 20

def hero(t):
    c = THEMES[t]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="400" viewBox="0 0 {W} 400">
<g font-family="{FONT}" text-anchor="middle">
 <text x="600" y="140" font-size="21" font-weight="600" fill="{c['sub']}" letter-spacing="0.2">iOS · macOS · AI</text>
 <text x="600" y="232" font-size="96" font-weight="700" fill="{c['fg']}" letter-spacing="-3">Edison.</text>
 <text x="600" y="290" font-size="28" font-weight="400" fill="{c['fg']}" letter-spacing="-0.3">Native apps, thoughtfully made.</text>
 <text x="600" y="330" font-size="19" font-weight="400" fill="{c['sub']}">Previously at Kwai and Mixin Network.</text>
</g>
</svg>'''

LULL_ICON = "data:image/jpeg;base64," + base64.b64encode(open("assets/lull-icon.jpg", "rb").read()).decode()

def lull(t):
    c = THEMES[t]
    h = 360
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{h + GAP}" viewBox="0 0 {W} {h + GAP}">
<defs><clipPath id="icon"><rect x="908" y="80" width="200" height="200" rx="45"/></clipPath></defs>
<rect width="{W}" height="{h}" rx="24" fill="{c['tile']}"/>
<g font-family="{FONT}">
 <text x="64" y="96" font-size="17" font-weight="600" fill="{c['sub']}" letter-spacing="0.1">New on the App Store · iPhone</text>
 <text x="64" y="166" font-size="56" font-weight="700" fill="{c['fg']}" letter-spacing="-1.6">Lull</text>
 <text x="64" y="218" font-size="28" font-weight="400" fill="{c['fg']}" letter-spacing="-0.3">A feeding reminder you won’t sleep through.</text>
 <text x="64" y="288" font-size="19" font-weight="400" fill="{c['link']}">View on the App Store ›</text>
</g>
<image x="908" y="80" width="200" height="200" href="{LULL_ICON}" xlink:href="{LULL_ICON}" clip-path="url(#icon)"/>
<rect x="908.5" y="80.5" width="199" height="199" rx="45" fill="none" stroke="#000" stroke-opacity=".08"/>
</svg>'''

SOON = [
    ("PasteFlow", ["Clipboard history for", "Mac and iPhone."]),
    ("Flow",      ["A quiet, clear way to", "manage your money."]),
    ("Odo",       ["Ride stats that become", "cards worth sharing."]),
    ("Reverie",   ["Your photos, arranged", "into beautiful albums."]),
]

def soon(t):
    c = THEMES[t]
    h = 320
    cols = ""
    for i, (name, lines) in enumerate(SOON):
        x = 64 + i * 272
        cols += f'''<text x="{x}" y="206" font-size="24" font-weight="700" fill="{c['fg']}" letter-spacing="-0.4">{name}</text>
 <text x="{x}" y="240" font-size="17" fill="{c['sub']}">{lines[0]}</text>
 <text x="{x}" y="264" font-size="17" fill="{c['sub']}">{lines[1]}</text>
 '''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h + GAP}" viewBox="0 0 {W} {h + GAP}">
<rect width="{W}" height="{h}" rx="24" fill="{c['tile']}"/>
<g font-family="{FONT}">
 <text x="64" y="84" font-size="17" font-weight="600" fill="{c['sub']}" letter-spacing="0.1">Coming soon</text>
 <text x="64" y="132" font-size="40" font-weight="700" fill="{c['fg']}" letter-spacing="-1">More apps on the way.</text>
 {cols}
</g>
</svg>'''

PROJECTS = [
    ("openpulse",      "Menu bar app",                 "OpenPulse",      ["Every AI coding quota,", "at a glance."]),
    ("brightnessflow", "Menu bar app",                 "BrightnessFlow", ["One brightness key.", "Every display."]),
    ("markdownflow",   "Reader &amp; Xcode extension", "MarkdownFlow",   ["Markdown and diagrams,", "beautifully offline."]),
    ("edisonskills",   "Open source",                  "edison-skills",  ["Practical skills for", "AI coding agents."]),
]

def tile(t, p, right):
    c = THEMES[t]
    key, eyebrow, name, lines = p
    w, h = W // 2, 300
    x0 = GAP // 2 if right else 0
    tx = x0 + 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h + GAP}" viewBox="0 0 {w} {h + GAP}">
<rect x="{x0}" width="{w - GAP // 2}" height="{h}" rx="24" fill="{c['tile']}"/>
<g font-family="{FONT}">
 <text x="{tx}" y="68" font-size="15" font-weight="600" fill="{c['sub']}" letter-spacing="0.1">{eyebrow}</text>
 <text x="{tx}" y="112" font-size="34" font-weight="700" fill="{c['fg']}" letter-spacing="-0.8">{name}</text>
 <text x="{tx}" y="162" font-size="22" font-weight="400" fill="{c['fg']}" letter-spacing="-0.2">{lines[0]}</text>
 <text x="{tx}" y="192" font-size="22" font-weight="400" fill="{c['fg']}" letter-spacing="-0.2">{lines[1]}</text>
 <text x="{tx}" y="252" font-size="17" font-weight="400" fill="{c['link']}">View on GitHub ›</text>
</g>
</svg>'''

for t in THEMES:
    open(f"assets/hero-{t}.svg", "w").write(hero(t))
    open(f"assets/lull-{t}.svg", "w").write(lull(t))
    open(f"assets/soon-{t}.svg", "w").write(soon(t))
    for i, p in enumerate(PROJECTS):
        open(f"assets/{p[0]}-{t}.svg", "w").write(tile(t, p, i % 2 == 1))
print("done")
