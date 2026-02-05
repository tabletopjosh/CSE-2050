from count_letters import count_letters

def is_anagram(word1, word2):
    """
    Returns True if word1 and word2 are anagrams by comparing letter counts.
    """
    # If the dictionary of letter counts for both words is identical, they are anagrams
    return count_letters(word1) == count_letters(word2)