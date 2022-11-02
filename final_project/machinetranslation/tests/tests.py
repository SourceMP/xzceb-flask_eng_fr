import unittest

from ... import english_to_french, french_to_english


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(french_to_english)
        self.assertEqual(french_to_english('Bonjour'), '"Hello"') 

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(english_to_french)
        self.assertEqual(english_to_french('Hello'), '"Bonjour"') 
             
unittest.main()

