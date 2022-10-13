import unittest  
from translator import english_to_french
from translator import french_to_english

class Test_English_to_French(unittest.TestCase):
    def test_en_to_fr_equal(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(None),None)
        self.assertEqual(english_to_french('Good night'),'Bonne nuit')

    def test_en_to_fr_notequal(self):
        self.assertNotEqual(english_to_french('Hello'),'Bonjour.')
        self.assertNotEqual(english_to_french('Good night'),'bonne nuit.')


class Test_French_to_English(unittest.TestCase):
    def test_fr_to_en_equal(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(None),None)
        self.assertEqual(french_to_english('Bonne nuit'),'Good night')

    def test_fr_to_en_notequal(self):
        self.assertNotEqual(french_to_english('Bonjour.'),'Hello')
        self.assertNotEqual(french_to_english('Bonne nuit.'),'Good night')


unittest.main()