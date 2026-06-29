#!/usr/bin/env python3
"""
Generate the liquid-glass "Random Dev Quote" card (quote-card.svg) with a
randomly chosen, recruiter-safe, on-brand quote.

Run on a schedule by .github/workflows/random-quote.yml so the quote rotates.
Stdlib only — no pip installs needed on the runner.

Want different quotes? Just edit the QUOTES list below (keep each quote under
~115 characters so it wraps cleanly into at most 3 lines).
"""
import random
from xml.sax.saxutils import escape

# (quote, author) — markets / quant / ML-AI / engineering / discipline
QUOTES = [
    ("The market can stay irrational longer than you can stay solvent.", "John Maynard Keynes"),
    ("In investing, what is comfortable is rarely profitable.", "Robert Arnott"),
    ("Risk comes from not knowing what you're doing.", "Warren Buffett"),
    ("Markets are never wrong; opinions often are.", "Jesse Livermore"),
    ("Price is what you pay. Value is what you get.", "Warren Buffett"),
    ("The four most dangerous words in investing: this time it's different.", "John Templeton"),
    ("The stock market transfers money from the impatient to the patient.", "Warren Buffett"),
    ("It's not whether you're right or wrong, but how much you make when right.", "George Soros"),
    ("Diversification is protection against ignorance.", "Warren Buffett"),
    ("All models are wrong, but some are useful.", "George Box"),
    ("In God we trust. All others must bring data.", "W. Edwards Deming"),
    ("Torture the data, and it will confess to anything.", "Ronald Coase"),
    ("The first principle is that you must not fool yourself.", "Richard Feynman"),
    ("If you can't measure it, you can't improve it.", "Peter Drucker"),
    ("What gets measured gets managed.", "Peter Drucker"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Premature optimization is the root of all evil.", "Donald Knuth"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Programs must be written for people to read.", "Harold Abelson"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("Any sufficiently advanced technology is indistinguishable from magic.", "Arthur C. Clarke"),
    ("Discipline equals freedom.", "Jocko Willink"),
    ("Slow is smooth, and smooth is fast.", "Navy SEAL adage"),
    ("Amateurs wait for inspiration; the rest of us go to work.", "Stephen King"),
    ("The best way out is always through.", "Robert Frost"),
    ("Quality is not an act, it is a habit.", "Aristotle"),
    ("Compound interest is the eighth wonder of the world.", "Albert Einstein"),
]


def wrap(text, max_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= max_chars:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def layout(text):
    """Pick the largest font size at which the quote fits in <= 3 lines."""
    for max_chars, font in [(46, 30), (50, 27), (56, 24)]:
        lines = wrap(text, max_chars)
        if len(lines) <= 3:
            return lines, font
    return wrap(text, 62), 22


TEMPLATE = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="Random developer quote">
  <defs>
    <linearGradient id="qbg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0c0c16"/>
      <stop offset="1" stop-color="#06060f"/>
    </linearGradient>
    <linearGradient id="qsheen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.09"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0.03"/>
    </linearGradient>
    <linearGradient id="qhl" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.42"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="qaccent" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffb56b"/>
      <stop offset="1" stop-color="#ff7a3c"/>
    </linearGradient>
    <linearGradient id="qshine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.11"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="qa" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ff7a3c" stop-opacity="0.85"/><stop offset="1" stop-color="#ff7a3c" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="qb" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#38bdf8" stop-opacity="0.45"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="qc" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffb56b" stop-opacity="0.6"/><stop offset="1" stop-color="#ffb56b" stop-opacity="0"/>
    </radialGradient>
    <filter id="qsoft" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="48"/></filter>
    <clipPath id="qround"><rect x="0" y="0" width="1000" height="300" rx="26"/></clipPath>
    <clipPath id="qpanelClip"><rect x="30" y="34" width="940" height="232" rx="24"/></clipPath>
  </defs>

  <g clip-path="url(#qround)">
    <rect width="1000" height="300" fill="url(#qbg)"/>

    <g filter="url(#qsoft)">
      <circle cx="160" cy="80" r="140" fill="url(#qa)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 38 28; -20 22; 0 0" dur="14s" repeatCount="indefinite"/>
      </circle>
      <circle cx="860" cy="230" r="150" fill="url(#qb)">
        <animateTransform attributeName="transform" type="translate" values="0 0; -38 -20; 22 -30; 0 0" dur="17s" repeatCount="indefinite"/>
      </circle>
      <circle cx="540" cy="40" r="110" fill="url(#qc)">
        <animateTransform attributeName="transform" type="translate" values="0 0; 26 30; -26 12; 0 0" dur="19s" repeatCount="indefinite"/>
      </circle>
    </g>

    <rect x="30" y="34" width="940" height="232" rx="24" fill="url(#qsheen)" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1.5"/>
    <rect x="42" y="40" width="916" height="48" rx="20" fill="url(#qhl)" opacity="0.45"/>

    <g clip-path="url(#qpanelClip)">
      <rect x="-350" y="34" width="240" height="232" fill="url(#qshine)" transform="skewX(-18)">
        <animate attributeName="x" values="-350; 1100" dur="7.5s" repeatCount="indefinite"/>
      </rect>
    </g>

    <rect x="64" y="92" width="5" height="116" rx="2.5" fill="url(#qaccent)"/>
    <text x="74" y="166" font-family="Georgia, 'Times New Roman', serif" font-size="150" font-weight="700" fill="url(#qaccent)" opacity="0.20">&#8220;</text>

    <text font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" fill="#ece3d8" font-size="__FONT__" font-style="italic" font-weight="500">__TSPANS__
    </text>

    <text x="938" y="236" text-anchor="end" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="20" font-weight="600" fill="#ff9a5c">&#8212;&#160; __AUTHOR__</text>
  </g>
</svg>
'''


def build():
    quote, author = random.choice(QUOTES)
    lines, font = layout(quote)
    n = len(lines)
    lh = font + 13
    first = 150 - (n - 1) * lh / 2 + 6
    tspans = "".join(
        '\n      <tspan x="100" y="{:.0f}">{}</tspan>'.format(first + i * lh, escape(line))
        for i, line in enumerate(lines)
    )
    return (TEMPLATE
            .replace("__FONT__", str(font))
            .replace("__TSPANS__", tspans)
            .replace("__AUTHOR__", escape(author)))


if __name__ == "__main__":
    svg = build()
    with open("quote-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Wrote quote-card.svg")
