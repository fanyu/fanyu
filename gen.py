import os, glob
os.makedirs("assets", exist_ok=True)
for f in glob.glob("assets/*.svg"):
    os.remove(f)

FONT = "-apple-system,BlinkMacSystemFont,'SF Pro Display','Helvetica Neue',Helvetica,Arial,sans-serif"

# Apple.com palette
THEMES = {
    "light": dict(tile="#F5F5F7", fg="#1D1D1F", sub="#6E6E73", link="#0066CC"),
    "dark":  dict(tile="#1D1D1F", fg="#F5F5F7", sub="#86868B", link="#2997FF"),
}

def hero(t):
    c = THEMES[t]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400">
<g font-family="{FONT}" text-anchor="middle">
 <text x="600" y="140" font-size="21" font-weight="600" fill="{c['sub']}" letter-spacing="0.2">iOS · macOS · AI</text>
 <text x="600" y="232" font-size="96" font-weight="700" fill="{c['fg']}" letter-spacing="-3">Edison.</text>
 <text x="600" y="290" font-size="28" font-weight="400" fill="{c['fg']}" letter-spacing="-0.3">Native apps, thoughtfully made.</text>
 <text x="600" y="330" font-size="19" font-weight="400" fill="{c['sub']}">Previously at Kwai and Mixin Network.</text>
</g>
</svg>'''

PROJECTS = [
    ("openpulse",      "Menu bar app",             "OpenPulse",      ["Every AI coding quota,", "at a glance."]),
    ("brightnessflow", "Menu bar app",             "BrightnessFlow", ["One brightness key.", "Every display."]),
    ("markdownflow",   "Reader &amp; Xcode extension", "MarkdownFlow", ["Markdown and diagrams,", "beautifully offline."]),
    ("edisonskills",   "Open source",              "edison-skills",  ["Practical skills for", "AI coding agents."]),
]

def tile(t, p):
    c = THEMES[t]
    key, eyebrow, name, lines = p
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="590" height="300" viewBox="0 0 590 300">
<rect width="590" height="300" rx="24" fill="{c['tile']}"/>
<g font-family="{FONT}">
 <text x="44" y="68" font-size="15" font-weight="600" fill="{c['sub']}" letter-spacing="0.1">{eyebrow}</text>
 <text x="44" y="112" font-size="34" font-weight="700" fill="{c['fg']}" letter-spacing="-0.8">{name}</text>
 <text x="44" y="162" font-size="22" font-weight="400" fill="{c['fg']}" letter-spacing="-0.2">{lines[0]}</text>
 <text x="44" y="192" font-size="22" font-weight="400" fill="{c['fg']}" letter-spacing="-0.2">{lines[1]}</text>
 <text x="44" y="252" font-size="17" font-weight="400" fill="{c['link']}">View on GitHub ›</text>
</g>
</svg>'''

for t in THEMES:
    open(f"assets/hero-{t}.svg", "w").write(hero(t))
    for p in PROJECTS:
        open(f"assets/{p[0]}-{t}.svg", "w").write(tile(t, p))
print("done")
