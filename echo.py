#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "astephens91"

import sys
import argparse


def text_echo(text):
    if isinstance(text, basestring):
        return text
    else:
        return "Not a string!"


def text_upper(text):
    if isinstance(text, basestring):
        return text.upper()
    else:
        return "Not a string!"


def text_lower(text):
    if isinstance(text, basestring):
        return text.lower()
    else:
        return "Not a string!"


def text_title(text):
    if isinstance(text, basestring):
        return text.title()
    else:
        return "Not a string!"


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
      description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper',
                        help='convert text to uppercase',
                        action="store_true")
    parser.add_argument('-l', '--lower',
                        help='convert text to lowercase',
                        action="store_true")
    parser.add_argument('-t', '--title',
                        help='convert text to titlecase',
                        action="store_true")
    return parser


def main():
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args()
    text = args.text

    if not args:
        parser.print_usage()
        sys.exit()

    if args.upper:
        text = text_upper(text)

    if args.lower:
        text = text_lower(text)

    if args.title:
        text = text_title(text)

    print(text)


if __name__ == "__main__":
    main()
