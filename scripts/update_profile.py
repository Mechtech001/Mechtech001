#!/usr/bin/env python3
"""Refreshes the profile README from live GitHub data. Standard library only.

It does two things on every run:
  1. rewrites the text stats between the stats markers in README.md
     (contributions, public repos, joined date, email)
  2. redraws the contribution graph widget as assets/contributions-{light,dark}.svg

Runs in GitHub Actions with the built-in GITHUB_TOKEN. Change EMAIL below to show another address.
"""
import json
import os
import re
import sys
import urllib.request
from collections import OrderedDict
from datetime import date
from html import escape
from pathlib import Path

EMAIL = "aditya16may@gmail.com"
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ASSETS = ROOT / "assets"

QUERY = """
query($login: String!) {
  user(login: $login) {
    createdAt
    repositories(privacy: PUBLIC, ownerAffiliations: OWNER) { totalCount }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""

# Transparent widget (no card, no border). Colours are chosen per theme so text stays readable.
THEMES = {
    "light": dict(text="#57606a", axis="#6e7781", fill="#5a6e73"),
    "dark": dict(text="#9198a1", axis="#7d8590", fill="#6b8c93"),
}
W, H = 540, 204
CX0, CX1, CY0, CY1 = 8, 478, 40, 168


def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-readme-updater"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    if payload.get("errors") or not payload.get("data", {}).get("user"):
        raise RuntimeError(f"GitHub API error: {payload.get('errors')}")
    return payload["data"]["user"]


def monthly(calendar):
    buckets = OrderedDict()
    for week in calendar["weeks"]:
        for day in week["contributionDays"]:
            key = day["date"][:7]
            buckets[key] = buckets.get(key, 0) + day["contributionCount"]
    return list(buckets.items())


def nice_max(v):
    for step in (8, 16, 40, 80, 160, 320, 640, 1280):
        if v <= step:
            return step
    return int(-(-v // 640) * 640)


def joined_text(created_at, today):
    months = (today.year - int(created_at[:4])) * 12 + today.month - int(created_at[5:7])
    if months >= 12:
        n = months // 12
        return f"{n} year{'s' if n != 1 else ''} ago"
    if months >= 1:
        return f"{months} month{'s' if months != 1 else ''} ago"
    return "this month"


def stats_block(user, today):
    cal = user["contributionsCollection"]["contributionCalendar"]
    return (
        f"- **{cal['totalContributions']:,}** contributions on GitHub\n"
        f"- **{user['repositories']['totalCount']}** public repos\n"
        f"- Joined GitHub {joined_text(user['createdAt'], today)}\n"
        f"- [{EMAIL}](mailto:{EMAIL})"
    )


def replace_block(text, block):
    pattern = re.compile(r"(<!-- stats:start -->\n).*?(\n<!-- stats:end -->)", re.DOTALL)
    if not pattern.search(text):
        raise RuntimeError("Stats markers not found in README.md")
    return pattern.sub(lambda m: m.group(1) + block + m.group(2), text)


def smooth(pts):
    def clamp(y):
        return max(CY0, min(CY1, y))
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, clamp(p1[1] + (p2[1] - p0[1]) / 6))
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, clamp(p2[1] - (p3[1] - p1[1]) / 6))
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def graph_svg(t, series, total):
    values = [v for _, v in series]
    n = len(values)
    ymax = nice_max(max(values + [1]))
    pts = [(CX0 + (CX1 - CX0) * i / max(n - 1, 1), CY1 - (CY1 - CY0) * v / ymax)
           for i, v in enumerate(values)]
    line_d = smooth(pts) if n > 1 else f"M{CX0},{CY1} L{CX1},{CY1}"
    area_d = f"{line_d} L{pts[-1][0]:.1f},{CY1} L{pts[0][0]:.1f},{CY1} Z"

    ticks = ""
    for k in range(9):                         # 0 .. ymax in eight steps, like the original
        v = ymax * k / 8
        y = CY1 - (CY1 - CY0) * k / 8
        ticks += (f'<line x1="{CX1}" x2="{CX1 + 5}" y1="{y:.1f}" y2="{y:.1f}" stroke="{t["axis"]}"/>'
                  f'<text x="{CX1 + 9}" y="{y + 4:.1f}" font-size="13" fill="{t["text"]}">{v:g}</text>')
    xt = ""
    for i in range(n - 1, -1, -2):
        key = series[i][0]
        x = pts[i][0]
        xt += (f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{CY1}" y2="{CY1 + 5}" stroke="{t["axis"]}"/>'
               f'<text x="{x:.1f}" y="{CY1 + 23}" font-size="13" fill="{t["text"]}" text-anchor="middle">'
               f'{key[2:4]}/{key[5:7]}</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d" font-family="-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif">
  <title id="t">Contributions in the last year</title>
  <desc id="d">Area chart of monthly GitHub contributions. {total} contributions in the last year.</desc>
  <text x="{CX1}" y="18" font-size="14" fill="{t["text"]}" text-anchor="end">contributions in the last year</text>
  <path d="{area_d}" fill="{t["fill"]}"/>
  <line x1="{CX0}" x2="{CX1}" y1="{CY1}" y2="{CY1}" stroke="{t["axis"]}"/>
  <line x1="{CX1}" x2="{CX1}" y1="{CY0}" y2="{CY1}" stroke="{t["axis"]}"/>
  {ticks}
  {xt}
</svg>
'''


def update(user, today=None, readme=README, assets=ASSETS):
    today = today or date.today()
    cal = user["contributionsCollection"]["contributionCalendar"]
    series = monthly(cal)
    assets.mkdir(parents=True, exist_ok=True)
    for name, t in THEMES.items():
        (assets / f"contributions-{name}.svg").write_text(
            graph_svg(t, series, cal["totalContributions"]), encoding="utf-8")
    block = stats_block(user, today)
    readme.write_text(replace_block(readme.read_text(encoding="utf-8"), block), encoding="utf-8")
    return block


if __name__ == "__main__":
    token, login = os.environ.get("GH_TOKEN"), os.environ.get("GH_USER")
    if not token or not login:
        sys.exit("Set GH_TOKEN and GH_USER (the workflow does this for you).")
    print(update(fetch(login, token)))
