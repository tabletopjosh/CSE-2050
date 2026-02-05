import string

def count_letters(data):
    # Initialize an empty dictionary to store our results
    counts = {}
    """
        Define the allowed characters (lowercase a-z)
    """ 
    allowed = string.ascii_lowercase
    
    # Iterate through every character in the input string, converted to lowercase
    for char in data.lower():
        # Only process the character if it is a standard lowercase letter
        if char in allowed:
            # If the letter is already in our dictionary, add 1 to its count
            if char in counts:
                counts[char] += 1
            # If it's the first time seeing the letter, start the count at 1
            else:
                counts[char] = 1
                
    return counts