"""Regenerates the SVG assets in ../assets (banner, footer, ecosystem map).

Optional maintenance tool: the SVGs are committed, so you only need this if you
want to change the typing phrases or colours. Pure Python standard library.

    python tools/generate_assets.py

Edit PHRASES below to change the typing line in the banner. Keep each phrase
at 33 characters or fewer so it fits the banner without touching the artwork.
The animation is SMIL only: no JavaScript, no external resources.
"""
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

BG = "#0B1020"
PANEL = "#111827"
BLUE = "#3B82F6"
CYAN = "#22D3EE"
VIOLET = "#8B5CF6"
LIGHT = "#E5E7EB"
MUTED = "#94A3B8"
SANS = "'Segoe UI','Inter','Helvetica Neue',Arial,sans-serif"
PHRASES = [
    "Agentic AI · LLM Applications",
    "RAG & Document Intelligence",
    "Web Scraping & Browser Automation",
    "FastAPI · Celery · Redis backends",
]
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def f(x):
    return ("%.2f" % x).rstrip("0").rstrip(".")


def write(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(name, len(svg.encode("utf-8")), "bytes")


# ---------------------------------------------------------------- banner
def banner():
    W, H = 1000, 340
    phrases = PHRASES
    FS, CW, X0, Y = 22, 13.2, 86, 262
    T, WIN = 20.0, 5.0
    n_ph = len(phrases)

    # ---- typing timelines (discrete steps, one loop = T seconds)
    clip_defs, text_els = [], []
    cursor_times, cursor_vals = [], []
    for i, p in enumerate(phrases):
        n = len(p)
        full = n * CW
        step = min(0.07, 2.4 / n)
        t0 = i * WIN
        times, vals = [], []
        if t0 > 0:
            times.append(0.0)
            vals.append(0.0)
        for k in range(n + 1):
            times.append(t0 + k * step)
            vals.append(k * CW)
        if t0 + WIN < T:
            times.append(t0 + WIN)
            vals.append(0.0)
        kt = ";".join(f(t / T) for t in times)
        kv = ";".join(f(v) for v in vals)
        clip_defs.append(
            f'<clipPath id="c{i}"><rect x="{X0}" y="236" height="38" width="{f(full)}">'
            f'<animate attributeName="width" dur="{int(T)}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{kt}" values="{kv}"/>'
            f"</rect></clipPath>"
        )
        # opacity window for the phrase
        if i == 0:
            base_op, o_vals, o_kt = "1", "1;0", "0;" + f(WIN / T)
        elif i == n_ph - 1:
            base_op, o_vals, o_kt = "0", "0;1", "0;" + f(t0 / T)
        else:
            base_op, o_vals, o_kt = "0", "0;1;0", "0;" + f(t0 / T) + ";" + f((t0 + WIN) / T)
        text_els.append(
            f'<text x="{X0}" y="{Y}" font-family="{MONO}" font-size="{FS}" fill="{LIGHT}" '
            f'textLength="{f(full)}" lengthAdjust="spacingAndGlyphs" clip-path="url(#c{i})" opacity="{base_op}">{esc(p)}'
            f'<animate attributeName="opacity" dur="{int(T)}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{o_kt}" values="{o_vals}"/>'
            f"</text>"
        )
        # cursor path
        if t0 > 0 and not cursor_times:
            cursor_times.append(0.0)
            cursor_vals.append(X0)
        for k in range(n + 1):
            cursor_times.append(t0 + k * step)
            cursor_vals.append(X0 + k * CW)
    ckt = ";".join(f(t / T) for t in cursor_times)
    ckv = ";".join(f(v) for v in cursor_vals)
    first_full = len(phrases[0]) * CW

    # ---- neural network art
    layers = [
        (650, [70, 135, 200, 265]),
        (745, [42, 102, 162, 222, 282]),
        (840, [72, 132, 192, 252]),
        (930, [105, 170, 235]),
    ]
    node_cols = [CYAN, BLUE, VIOLET, CYAN]
    rnd = random.Random(7)
    edges, hot = [], []
    for li in range(len(layers) - 1):
        for a in layers[li][1]:
            for b in layers[li + 1][1]:
                edges.append((layers[li][0], a, layers[li + 1][0], b))
    hot_idx = set(rnd.sample(range(len(edges)), 9))
    edge_svg = []
    for idx, (x1, y1, x2, y2) in enumerate(edges):
        if idx in hot_idx:
            edge_svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{CYAN}" stroke-opacity=".42" stroke-width="1.2"/>')
        else:
            edge_svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{BLUE}" stroke-opacity=".16"/>')
    node_svg = []
    big = {(1, 2), (2, 1), (3, 1), (0, 0)}
    pulse_i = 0
    for li, (x, ys) in enumerate(layers):
        for ni, y in enumerate(ys):
            col = node_cols[li]
            if (li, ni) in big:
                node_svg.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{col}" fill-opacity=".10"/>')
                r = 7
            else:
                r = 5
            dur = 4 + (pulse_i % 4)
            begin = (pulse_i * 0.7) % 5
            node_svg.append(
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}">'
                f'<animate attributeName="opacity" values="1;.45;1" dur="{dur}s" begin="{f(begin)}s" repeatCount="indefinite"/></circle>'
            )
            pulse_i += 1

    def pt(li, ni):
        return layers[li][0], layers[li][1][ni]

    packets = [
        ([(0, 0), (1, 1), (2, 1), (3, 0)], 7, 0.5),
        ([(0, 2), (1, 3), (2, 2), (3, 1)], 8.5, 2.5),
        ([(0, 3), (1, 4), (2, 3), (3, 2)], 9.5, 4.5),
        ([(0, 1), (1, 2), (2, 0), (3, 1)], 8, 1.5),
    ]
    pk_svg = []
    for path_nodes, dur, begin in packets:
        pts = [pt(*p) for p in path_nodes]
        d = "M" + " L".join(f"{x},{y}" for x, y in pts)
        pk_svg.append(
            f'<circle r="3.4" fill="#A5F3FC" opacity="0">'
            f'<animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{d}"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.9;1" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/>'
            f"</circle>"
        )

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Mr Faizan, Python Backend and Applied AI Developer</title>
<desc id="d">Dark navy banner with a cyan, blue and violet neural network graphic and a typing line cycling through Agentic AI, RAG, web scraping and FastAPI backends.</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".6" stop-color="#0E1530"/><stop offset="1" stop-color="#15122E"/></linearGradient>
<radialGradient id="gB" cx="200" cy="40" r="420" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{BLUE}" stop-opacity=".22"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<radialGradient id="gV" cx="880" cy="300" r="360" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".26"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<radialGradient id="gC" cx="720" cy="20" r="280" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CYAN}" stop-opacity=".13"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<linearGradient id="nm" x1="{X0-30}" y1="0" x2="520" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CYAN}"/><stop offset=".55" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
<linearGradient id="dv" x1="56" y1="0" x2="420" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
<linearGradient id="fadeL" x1="590" y1="0" x2="690" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="artMask"><rect x="560" y="0" width="440" height="{H}" fill="url(#fadeL)"/></mask>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{BLUE}" stroke-opacity=".07"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
{chr(10).join(clip_defs)}
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#gB)"/>
<rect width="{W}" height="{H}" fill="url(#gV)"/>
<rect width="{W}" height="{H}" fill="url(#gC)"/>
<g mask="url(#artMask)">
{chr(10).join(edge_svg)}
{chr(10).join(node_svg)}
{chr(10).join(pk_svg)}
</g>
<text x="56" y="64" font-family="{MONO}" font-size="15" letter-spacing="1.5" fill="{CYAN}" fill-opacity=".9">&gt; mrfaizan-dev</text>
<text x="56" y="152" font-family="{SANS}" font-size="80" font-weight="800" fill="url(#nm)" textLength="470" lengthAdjust="spacingAndGlyphs">MR FAIZAN</text>
<text x="58" y="196" font-family="{SANS}" font-size="27" font-weight="600" fill="{LIGHT}" textLength="500" lengthAdjust="spacingAndGlyphs">Python Backend &amp; Applied AI Developer</text>
<rect x="56" y="215" width="364" height="2.5" rx="1.25" fill="url(#dv)"/>
<text x="56" y="{Y}" font-family="{MONO}" font-size="{FS}" font-weight="700" fill="{CYAN}">›</text>
{chr(10).join(text_els)}
<g><animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite" calcMode="discrete"/>
<rect x="{f(X0 + first_full + 3)}" y="244" width="9" height="24" fill="{CYAN}">
<animate attributeName="x" dur="{int(T)}s" repeatCount="indefinite" calcMode="discrete" keyTimes="{ckt}" values="{ckv}"/></rect></g>
<text x="58" y="306" font-family="{MONO}" font-size="14" letter-spacing=".6" fill="{MUTED}">Building systems that read, reason &amp; extract.</text>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="17.5" fill="none" stroke="#1E293B"/>
</svg>
"""
    write("profile-banner.svg", svg)


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1000, 170
    wave = "M0,128 Q62.5,106 125,128 T250,128 T375,128 T500,128 T625,128 T750,128 T875,128 T1000,128"
    dots = []
    cols = [CYAN, BLUE, VIOLET, CYAN]
    for i, x in enumerate([125, 375, 625, 875]):
        dots.append(
            f'<circle cx="{x}" cy="128" r="9" fill="{cols[i]}" fill-opacity=".12"/>'
            f'<circle cx="{x}" cy="128" r="4.5" fill="{cols[i]}"><animate attributeName="opacity" values="1;.4;1" dur="{4+i}s" begin="{i*0.9}s" repeatCount="indefinite"/></circle>'
        )
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Mr Faizan footer</title>
<desc id="d">Dark navy footer with a flowing cyan, blue and violet wave and the line: Reliable pipelines. Grounded answers. Clean data.</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#15122E"/><stop offset=".5" stop-color="#0E1530"/><stop offset="1" stop-color="{BG}"/></linearGradient>
<linearGradient id="wv" x1="0" y1="0" x2="{W}" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".25" stop-color="{CYAN}"/><stop offset=".6" stop-color="{BLUE}"/><stop offset=".85" stop-color="{VIOLET}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
<radialGradient id="gl" cx="500" cy="150" r="420" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{BLUE}" stop-opacity=".2"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{BLUE}" stroke-opacity=".06"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#gl)"/>
<path d="{wave}" fill="none" stroke="url(#wv)" stroke-width="2" stroke-opacity=".7"/>
<path d="{wave}" fill="none" stroke="#A5F3FC" stroke-width="2" stroke-opacity=".55" stroke-dasharray="3 22" stroke-linecap="round">
<animate attributeName="stroke-dashoffset" from="0" to="-250" dur="10s" repeatCount="indefinite"/></path>
{chr(10).join(dots)}
<text x="500" y="56" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" fill="{LIGHT}" textLength="540" lengthAdjust="spacingAndGlyphs">Reliable pipelines. Grounded answers. Clean data.</text>
<text x="500" y="86" text-anchor="middle" font-family="{MONO}" font-size="14" letter-spacing=".8" fill="{MUTED}" textLength="470" lengthAdjust="spacingAndGlyphs">mrfaizan-dev · Python Backend &amp; Applied AI Developer</text>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="17.5" fill="none" stroke="#1E293B"/>
</svg>
"""
    write("profile-footer.svg", svg)


# ---------------------------------------------------------------- architecture / ecosystem map
def architecture():
    W, H = 900, 676
    CHW = 7.7  # approx px per char at 14px
    layers = [
        ("01 · DATA IN", "web data + processing", BLUE,
         [["Playwright", "Selenium", "SeleniumBase", "Nodriver", "BeautifulSoup"],
          ["Pandas", "Pydantic V2", "Asyncio", "Proxy Rotation"]]),
        ("02 · RETRIEVAL", "grounding models in data", CYAN,
         [["RAG", "Corrective RAG (CRAG)", "Chroma", "FAISS"]]),
        ("03 · AGENTS", "orchestration + evaluation", VIOLET,
         [["LangChain", "LangGraph", "LlamaIndex", "CrewAI", "Prompt Engineering"],
          ["LangSmith", "DeepEval"]]),
        ("04 · MODELS", "providers + assistants", BLUE,
         [["OpenAI", "OpenRouter", "Groq"],
          ["ChatGPT", "Claude", "Gemini"]]),
        ("05 · SERVING", "APIs, queues, deploy", CYAN,
         [["FastAPI", "Celery", "Redis", "Docker"],
          ["Next.js", "Tailwind CSS"]]),
    ]
    LX, LW, LH, GAP, Y0 = 40, 820, 86, 22, 112
    CX0, CX1 = 262, 836
    out = []
    for li, (name, sub, col, rows) in enumerate(layers):
        y = Y0 + li * (LH + GAP)
        out.append(f'<rect x="{LX}" y="{y}" width="{LW}" height="{LH}" rx="14" fill="{PANEL}" stroke="{col}" stroke-opacity=".45"/>')
        out.append(f'<rect x="{LX}" y="{y+14}" width="4" height="{LH-28}" rx="2" fill="{col}"/>')
        out.append(f'<text x="64" y="{y+38}" font-family="{MONO}" font-size="14" font-weight="700" letter-spacing="1.2" fill="{col}">{esc(name)}</text>')
        out.append(f'<text x="64" y="{y+60}" font-family="{MONO}" font-size="11.5" fill="{MUTED}">{esc(sub)}</text>')
        for ri, row in enumerate(rows):
            cy = y + 9 + ri * 38
            x = CX0
            if name.startswith("05") and ri == 1:
                lbl = "AI-assisted UI:"
                out.append(f'<text x="{x}" y="{cy+20}" font-family="{MONO}" font-size="12" fill="{MUTED}">{lbl}</text>')
                x += 112
            for label in row:
                tl = max(len(label) * CHW, 36)
                w = tl + 24
                dash = ' stroke-dasharray="4 3"' if name.startswith("05") and ri == 1 else ""
                out.append(f'<rect x="{f(x)}" y="{cy}" width="{f(w)}" height="30" rx="15" fill="{BG}" stroke="{col}" stroke-opacity=".7"{dash}/>')
                out.append(
                    f'<text x="{f(x+w/2)}" y="{cy+20}" text-anchor="middle" font-family="{SANS}" font-size="14" fill="{LIGHT}" '
                    f'textLength="{f(tl)}" lengthAdjust="spacingAndGlyphs">{esc(label)}</text>'
                )
                x += w + 10
            assert x - 10 <= CX1 + 4, (name, x)
        if li < len(layers) - 1:
            ay = y + LH + 3
            out.append(
                f'<path d="M444,{ay} L450,{ay+8} L456,{ay}" fill="none" stroke="{CYAN}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-opacity=".9">'
                f'<animate attributeName="stroke-opacity" values=".9;.25;.9" dur="3s" begin="{li*0.5}s" repeatCount="indefinite"/></path>'
            )
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">AI development ecosystem map</title>
<desc id="d">A five-layer map of the tools Mr Faizan works with: data acquisition and processing, retrieval, agents and evaluation, models and providers, and serving infrastructure.</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/><stop offset="1" stop-color="#14122C"/></linearGradient>
<radialGradient id="gV" cx="780" cy="40" r="360" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".2"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<radialGradient id="gB" cx="100" cy="620" r="360" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{BLUE}" stop-opacity=".18"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="{BLUE}" stroke-opacity=".06"/></pattern>
<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#frame)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#gV)"/>
<rect width="{W}" height="{H}" fill="url(#gB)"/>
<text x="40" y="52" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{CYAN}">AI DEVELOPMENT ECOSYSTEM</text>
<text x="40" y="84" font-family="{SANS}" font-size="24" font-weight="700" fill="{LIGHT}" textLength="440" lengthAdjust="spacingAndGlyphs">How the tools I work with fit together</text>
{chr(10).join(out)}
<text x="40" y="{H-20}" font-family="{MONO}" font-size="11.5" fill="{MUTED}">A map of my toolset, not a claim that every project uses every tool.</text>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="17.5" fill="none" stroke="#1E293B"/>
</svg>
"""
    write("ai-architecture.svg", svg)


if __name__ == "__main__":
    assert all(len(p) <= 33 for p in PHRASES), "phrases must be 33 characters or fewer"
    banner()
    footer()
    architecture()
