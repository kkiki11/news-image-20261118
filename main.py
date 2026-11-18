#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261118.

Writes the bundled image to /output/entry.png. No network access, no
randomness: every run writes the same bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(here, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
