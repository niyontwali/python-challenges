"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""
def alphabet_position(text):
    # Dictionary mapping letters to their positions in the alphabet
    letter_to_position = {chr(ord('a') + i): str(i + 1) for i in range(26)}
    
    # Function to get position for a letter, returns empty string for non-letter characters
    def get_position(char):
        return letter_to_position.get(char.lower(), '')
    
    # Use generator expression to get positions for all letters in the text
    positions = (get_position(char) for char in text)
    
    # Filter out empty strings (non-letter characters) and join the positions with spaces
    return ' '.join(filter(None, positions))

# Test case
print(alphabet_position("The sunset sets at twelve o' clock."))
