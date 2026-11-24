#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one sharp, funny loading-screen tip for stressed developers and
AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

No arguments, no network, stdlib only, deterministic: the same bytes
every run.
"""

import os
import sys

TIP = (
    "Tip: your AI agent is waiting on this build too \u2014 it just can't "
    "pace the room. Stretch, drink water, and let the loading bar "
    "carry the stress for once."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate validation: a single line, 1-200 characters, not only whitespace.
    if "\n" in TIP or "\r" in TIP:
        print("error: tip must be a single line", file=sys.stderr)
        return 1
    if not TIP.strip():
        print("error: tip must not be only whitespace", file=sys.stderr)
        return 1
    if len(TIP) > MAX_CHARS:
        print(
            f"error: tip is {len(TIP)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)

    # Read-back verification: the file on disk must be byte-for-byte the tip.
    with open(path, "rb") as f:
        written_bytes = f.read()
    if written_bytes != TIP.encode("utf-8"):
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if written_bytes.endswith(b"\n"):
        print("error: file must not end with a newline", file=sys.stderr)
        return 1

    print(
        f"Wrote {len(TIP)}-character ({len(written_bytes)}-byte) "
        f"tip to {path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
