#!/usr/bin/python
"""  Translator Unit Tester Module"""
import unittest
from machinetranslation import translator

class TestingTranslator(unittest.TestCase):
    """Testing the Translator for the all the cases"""
    translator =  translator.Translator()

    def test_e2f_translator_function_check_null(self):
        """Testing the English to French for Null case"""
        text_to_translate = "" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.e2f_translator_function(text_to_translate)
        self.assertEqual(translation,"Text to Translate cannot be empty")
    def test_e2f_translator_function_equals(self):
        """Testing the English to French for Proper translation case"""
        text_to_translate = "Hello" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.e2f_translator_function(text_to_translate)
        self.assertEqual(translation,"Bonjour")
    def test_e2f_translator_function_not_equals(self):
        """Testing the English to French for improper translation case"""
        text_to_translate = "Hello" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.e2f_translator_function(text_to_translate)
        self.assertNotEqual(translation,"Hello", "\"Hello\" in English is not \"Hello\" in French")

    def test_f2e_translator_function_check_null(self):
        """Testing the French to English for Null case"""
        text_to_translate = "" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.f2e_translator_function(text_to_translate)
        self.assertEqual(translation,"Text to Translate cannot be empty")
    def test_f2e_translator_function_equals(self):
        """Testing the  French To English for Proper translation case"""
        text_to_translate = "Bonjour" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.f2e_translator_function(text_to_translate)
        self.assertEqual(translation,"Hello")
    def test_f2e_translator_function_not_equals(self):
        """Testing the  French To English for improper translation case"""
        text_to_translate = "Hello" # must match ""Bonjour, comment es-tu?""
        translation =  self.translator.f2e_translator_function(text_to_translate)
        self.assertNotEqual(translation,"Bonjour","\"Bonjour\" in frecnh != \"Bonjour\" in English")

if __name__ == "__main__":
    unittest.main()
