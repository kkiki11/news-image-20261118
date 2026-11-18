#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261118.

Writes the bundled image to /output/entry.png. No network access, no
randomness: every run writes the same bytes.
"""
import hashlib
import os
import shutil
import sys


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(source, "/output/entry.png")
    if _sha256(source) != _sha256("/output/entry.png"):
        print("error: /output/entry.png differs from the bundled entry.png",
              file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
