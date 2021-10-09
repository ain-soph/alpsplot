#!/usr/bin/env python3

import argparse
import glob
from fontTools.ttLib.ttCollection import TTCollection
from fontTools.ttLib.ttFont import TTFont

# https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6name.html
# https://onlinefontconverter.com/

# pip install fonttools


def merge_ttc(pattern: str, ttc_path: str):
    path_list = glob.glob(pattern)
    ttc = TTCollection()
    ttc.fonts.extend([TTFont(file=fontpath, fontNumber=i)
                      for i, fontpath in enumerate(path_list)])
    ttc.save(ttc_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', help='glob match pattern for ttf files')
    parser.add_argument('ttc_path', help='output ttc path')
    args = parser.parse_args()
    pattern: str = args.pattern
    ttc_path: str = args.ttc_path
    merge_ttc(pattern, ttc_path)


if __name__ == '__main__':
    main()
