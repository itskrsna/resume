"""Write resume/cover-letter-custom.tex from COMPANY / POSITION / LETTER_ROLE env vars.

Inputs come from a workflow_dispatch form, so every value is LaTeX-escaped and
length-limited before it is written.
"""
import os

BS = chr(92)
SPECIAL = {
    BS: BS + "textbackslash{}",
    "&": BS + "&",
    "%": BS + "%",
    "$": BS + "$",
    "#": BS + "#",
    "_": BS + "_",
    "{": BS + "{",
    "}": BS + "}",
    "~": BS + "textasciitilde{}",
    "^": BS + "textasciicircum{}",
}


def esc(text: str) -> str:
    text = " ".join(text.split())[:100]
    return "".join(SPECIAL.get(c, c) for c in text)


role = os.environ["LETTER_ROLE"]
if role not in ("ai", "cloud"):
    raise SystemExit("letter_role must be 'ai' or 'cloud'")

lines = [BS + "def" + BS + "company{" + esc(os.environ["COMPANY"]) + "}"]
position = esc(os.environ.get("POSITION", ""))
if position:
    lines.append(BS + "def" + BS + "position{" + position + "}")
lines.append(BS + "input{cover-letter-" + role + "}")

with open("resume/cover-letter-custom.tex", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
