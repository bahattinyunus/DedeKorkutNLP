import re
import string

def normalize_text(text: str) -> str:
    """
    Normalizes Turkish text by converting to lowercase and handling special characters.
    
    Args:
        text (str): Input text.
        
    Returns:
        str: Normalized text.
    """
    if not text:
        return ""
        
    # Turkish specific lowercase handling
    text = text.replace('İ', 'i').replace('I', 'ı')
    text = text.lower()
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from the text.
    
    Args:
        text (str): Input text.
        
    Returns:
        str: Text without punctuation.
    """
    return text.translate(str.maketrans('', '', string.punctuation))

def tokenize(text: str) -> list:
    """
    Simple whitespace tokenizer.
    
    Args:
        text (str): Input text.
        
    Returns:
        list: List of tokens.
    """
    return text.split()
