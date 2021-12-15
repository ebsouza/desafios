# -*- coding: utf-8 -*-

import textwrap
import logging
from abc import ABC, abstractmethod


class IdWallFormatter(ABC):

    def __init__(self, limit, justify=False, break_symbol="\n\n"):
        self.justify = justify
        self.limit = limit
        self.break_symbol = break_symbol

    @abstractmethod
    def next_paragraph(self):
        pass

    @abstractmethod
    def format_output(self, input_string):
        pass

    def format_paragraph(self, paragraph):
        lines = textwrap.wrap(paragraph, width=self.limit)
        output_string = ""
        for line in lines:
            line = self.justify_text(line) if self.justify else line
            output_string += f"{line}\n"

        return output_string

    def justify_text(self, phrase):
        count = self.limit - len(phrase)
        words = phrase.strip().split(" ")

        if len(words) == 1:
            return words[0].ljust(self.limit)

        while count > 0:
            for index in range(len(words) - 1, 0, -1):
                word = words[index]
                words[index] = f" {word}"
                count -= 1
                if count == 0:
                    break

        return " ".join(words)


class StringFormatter(IdWallFormatter):

    def next_paragraph(self, input_string):
        paragraphs = input_string.split(self.break_symbol)
        for paragraph in paragraphs:
            yield paragraph

    def format_output(self, input_string):
        output_string = ""
        try:
            for paragraph in self.next_paragraph(input_string):
                formatted_paragraph = self.format_paragraph(paragraph)
                output_string += f"{formatted_paragraph}\n"
        except Exception as e:
            error_message = f"[StringFormatter]: {e}"
            logging.error(error_message)

        return output_string


class FileFormatter(IdWallFormatter):

    def next_paragraph(self, input_file):
        with open(input_file) as file:
            paragraph = str()

            for line in file.readlines():
                if line == "\n":
                    yield paragraph
                    paragraph = str()
                paragraph += f"{line}"
            else:
                yield paragraph

    def generate_output_name(self, input_file):
        return f"{input_file[:-4]}_output.txt"

    def format_output(self, input_file):
        try:
            output_file = self.generate_output_name(input_file)
            with open(output_file, "w") as file:
                for paragraph in self.next_paragraph(input_file):
                    output_string = self.format_paragraph(paragraph)
                    file.write(f"{output_string}\n")

            return output_file
        except Exception as e:
            error_message = f"[FileFormatter]: {e}"
            logging.error(error_message)



