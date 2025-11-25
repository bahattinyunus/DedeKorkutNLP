def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculates Word Error Rate (WER).
    Placeholder implementation - in a real scenario, use a library like jiwer.
    
    Args:
        reference (str): Ground truth text.
        hypothesis (str): Predicted text.
        
    Returns:
        float: WER score (0.0 to 1.0+)
    """
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    # Simple Levenshtein distance on words (simplified for placeholder)
    # TODO: Implement full WER calculation
    return 0.0

def calculate_cer(reference: str, hypothesis: str) -> float:
    """
    Calculates Character Error Rate (CER).
    Placeholder implementation.
    
    Args:
        reference (str): Ground truth text.
        hypothesis (str): Predicted text.
        
    Returns:
        float: CER score.
    """
    # TODO: Implement full CER calculation
    return 0.0
