import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Merci')
        self.assertEqual(english_to_french('good'),'bien')

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hi')
        self.assertNotEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('bien'),'good')

if __name__ == "__main__":
    unittest.main()
