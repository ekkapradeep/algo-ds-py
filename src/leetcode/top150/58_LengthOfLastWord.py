def lengthOfLastWord(s: str) -> int:
    # Trim trailing spaces and split by spaces
    words = s.strip().split()
    
    # Return length of last word
    return len(words[-1])
