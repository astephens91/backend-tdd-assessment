#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):

    def test_echo(self):
        # Echoes input text if string, else returns "Not a string!"
        integer = echo.text_echo(13)
        no_text = echo.text_echo("")
        test_result = echo.text_echo("Test")
        self.assertEqual(test_result, "Test")
        self.assertEqual(no_text, "")
        self.assertEqual(integer, "Not a string!")

    def test_help(self):
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-u', 'hello'])
        print(args)
        result = echo.text_upper('hello')
        no_text = echo.text_upper("")
        integer = echo.text_upper(13)
        self.assertEquals(result, "HELLO")
        self.assertEquals(no_text, "")
        self.assertEquals(integer, "Not a string!")
        self.assertEquals(args.upper, True)

    def test_lower(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-l', 'HELLO'])
        print(args)
        result = echo.text_lower('HELLO')
        no_text = echo.text_lower("")
        integer = echo.text_lower(13)
        self.assertEquals(result, "hello")
        self.assertEquals(no_text, "")
        self.assertEquals(integer, "Not a string!")

    def test_title(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-t', 'hello'])
        print(args)
        result = echo.text_title('hello')
        no_text = echo.text_title("")
        integer = echo.text_title(13)
        self.assertEquals(result, "Hello")
        self.assertEquals(no_text, "")
        self.assertEquals(integer, "Not a string!")

    def all_options(self):
        parser = echo.create_parser()
        args = parser.parse_args(['-tul', 'heLLo'])
        print(args)
        string = "heLLo"
        result = echo.text_lower(echo.text_upper(echo.text_title(string)))
        self.assertEquals(result, "hello")
        self.assertEquals(args.upper, True)
        self.assertEquals(args.lower, True)
        self.assertEquals(args.title, True)


if __name__ == '__main__':
    unittest.main()
