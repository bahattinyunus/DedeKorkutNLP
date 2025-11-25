import unittest
from dedekorkut.evaluation import calculate_wer, calculate_cer, levenshtein_distance

class TestEvaluation(unittest.TestCase):
    
    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance([], []), 0)
        
    def test_calculate_wer(self):
        ref = "bu bir test cümlesidir"
        hyp = "bu bir deneme cümlesidir"
        # "test" -> "deneme" (1 substitution)
        # Length = 4
        # WER = 1/4 = 0.25
        self.assertEqual(calculate_wer(ref, hyp), 0.25)
        
        ref = "merhaba dünya"
        hyp = "merhaba"
        # 1 deletion
        # Length = 2
        # WER = 1/2 = 0.5
        self.assertEqual(calculate_wer(ref, hyp), 0.5)
        
    def test_calculate_cer(self):
        ref = "test"
        hyp = "tost"
        # 1 substitution ('e' -> 'o')
        # Length = 4
        # CER = 1/4 = 0.25
        self.assertEqual(calculate_cer(ref, hyp), 0.25)

if __name__ == '__main__':
    unittest.main()
