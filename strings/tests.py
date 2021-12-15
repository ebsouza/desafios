# -*- coding: utf-8 -*-

import unittest

from formatter import StringFormatter, FileFormatter


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.text = "In the beginning God\ncreated the heavens and the earth." + \
                    "\n\n" +\
                    "Now the earth was formless and empty, darkness was\nover the " + \
                    "surface of the deep, and the Spirit of God\nwas hovering over the waters." + \
                    "\n\n" +\
                    "And God said, \"Let there be light,\" and there was light."
        self.total_paragraphs = 3
        self.paragraph = "In the beginning God\ncreated the heavens and the earth."

    def test_format_paragraph(self):
        limit = 15
        string_formatter = StringFormatter(limit)

        formatted_paragraph = string_formatter.format_paragraph(self.paragraph)
        lines = formatted_paragraph.split("\n")
        for line in lines[:-1]:
            self.assertLessEqual(len(line), limit)

    def test_format_paragraph_justified_text(self):
        limit = 15
        string_formatter = StringFormatter(limit, True)

        formatted_paragraph = string_formatter.format_paragraph(self.paragraph)
        lines = formatted_paragraph.split("\n")
        for line in lines[:-1]:
            self.assertEqual(len(line), limit)

    def test_next_paragraphs_formatter_break_symbol(self):
        limit = 15
        string_formatter = StringFormatter(limit, break_symbol='<br><br>')
        text = self.text.replace("\n", "<br>")

        paragraph_counter = 0
        for _ in string_formatter.next_paragraph(text):
            paragraph_counter += 1

        self.assertEqual(paragraph_counter, self.total_paragraphs)

    def test_next_paragraphs_string_formatter(self):
        limit = 15
        string_formatter = StringFormatter(limit)

        paragraph_counter = 0
        for _ in string_formatter.next_paragraph(self.text):
            paragraph_counter += 1

        self.assertEqual(paragraph_counter, self.total_paragraphs)

    def test_next_paragraphs_file_formatter(self):
        limit = 30
        file_formatter = FileFormatter(limit)
        input_file = "data/input-1.txt"

        paragraph_counter = 0
        for _ in file_formatter.next_paragraph(input_file):
            paragraph_counter += 1

        self.assertEqual(paragraph_counter, self.total_paragraphs)


if __name__ == '__main__':
    unittest.main()
