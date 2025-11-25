import unittest
from dedekorkut.preprocessing import normalize_text, remove_punctuation, tokenize

class TestPreprocessing(unittest.TestCase):
    
    def test_normalize_text(self):
        self.assertEqual(normalize_text("İSTANBUL"), "istanbul")
        self.assertEqual(normalize_text("Isparta"), "ısparta")
        self.assertEqual(normalize_text("  Merhaba   Dünya  "), "merhaba dünya")
        
    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Merhaba, Dünya!"), "Merhaba Dünya")
        
    def test_tokenize(self):
        self.assertEqual(tokenize("merhaba dünya"), ["merhaba", "dünya"])

if __name__ == '__main__':
    unittest.main()
