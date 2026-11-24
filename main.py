"""One-Line Office Joke: 24-Hour Sprint.

One original single-line joke about office life. Final line: the
meeting about having a shorter meeting, which then needs a pre-meeting
to prepare for it -- a specific, recognisable office absurdity with
the buzzword "alignment" as the sting, rather than a generic complaint
about work. The gate allows 1-200 characters, exactly one line, so
the program refuses to write anything outside that.
"""

import os

LINE = (
    "I love this job: only here can forty people spend an hour "
    "deciding next week's meeting should be shorter, then book a "
    "pre-meeting to prepare for it, call it alignment, and minute "
    "it as a win."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
