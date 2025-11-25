import numpy as np

def levenshtein_distance(ref: list, hyp: list) -> int:
    """
    Calculates the Levenshtein distance between two sequences.
    
    Args:
        ref (list): Reference sequence.
        hyp (list): Hypothesis sequence.
        
    Returns:
        int: The edit distance.
    """
    m, n = len(ref), len(hyp)
    
    # Create a matrix of size (m+1) x (n+1)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if ref[i - 1] == hyp[j - 1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost # Substitution
            )
            
    return dp[m][n]

def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculates Word Error Rate (WER).
    
    Args:
        reference (str): Ground truth text.
        hypothesis (str): Predicted text.
        
    Returns:
        float: WER score.
    """
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    if not ref_words:
        return 0.0 if not hyp_words else 1.0
        
    distance = levenshtein_distance(ref_words, hyp_words)
    return distance / len(ref_words)

def calculate_cer(reference: str, hypothesis: str) -> float:
    """
    Calculates Character Error Rate (CER).
    
    Args:
        reference (str): Ground truth text.
        hypothesis (str): Predicted text.
        
    Returns:
        float: CER score.
    """
    ref_chars = list(reference)
    hyp_chars = list(hypothesis)
    
    if not ref_chars:
        return 0.0 if not hyp_chars else 1.0
        
    distance = levenshtein_distance(ref_chars, hyp_chars)
    return distance / len(ref_chars)
