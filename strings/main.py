# -*- coding: utf-8 -*-

import argparse

from formatter import StringFormatter, FileFormatter


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--text', dest='text', default=None, type=str,
                    help='an integer for the accumulator')
parser.add_argument('--limit', dest='limit', default=40, type=int,
                    help='sum the integers (default: find the max)')
parser.add_argument('--justify', dest='justify', action='store_true',
                    help='sum the integers (default: find the max)')
parser.add_argument('--file_path', dest='file_path', default=None, type=str,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()


if not args.text:
    input_string = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " + \
                   "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.\n" + \
                   "\n" + \
                   "And God said, \"Let there be light,\" and there was light. God saw that the light was good, and he " + \
                   "separated the light from the darkness. God called the light \"day,\" and the darkness he " + \
                   "called \"night.\" And there was evening, and there was morning - the first day."
else:
    input_string = args.text


if args.file_path:
    formatter = FileFormatter(args.limit, args.justify)
    input_text = args.file_path
else:
    formatter = StringFormatter(args.limit, args.justify)
    input_text = input_string


print("Inputs: ")
print(f"Limit: {args.limit}")
print(f"Should justify: {args.justify}")
print("\n=========================\n")

output_string = formatter.format_output(input_text)
print(output_string)
