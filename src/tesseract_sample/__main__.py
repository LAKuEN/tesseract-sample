# -*- coding: utf-8 -*-
"""画像をTesseractで読み取る."""
import argparse
from pathlib import Path

import cv2
import pytesseract


def main(fpath):
    img = cv2.imread(str(fpath), cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(img, lang='jpn', config="--psm 6")

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    res = main(args.path)
    print(res)
