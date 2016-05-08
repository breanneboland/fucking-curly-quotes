# -*- coding: utf-8 -*-

print "Stuff works, ok"

forbidden_characters = ["“", "”", "‘", "’"]

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"", 
    "‘": "\'", 
    "’": "\'"
}

print magical_character_conversion_dict

sample_fucked_string = "“This shit looks casual but will fuck you up.”"

other_sample_fucked_string = "“Well, my favorite quote is ‘Good typography includes curly quotes,’ even though it can basically destroy your code.”"

def unfuck_your_string (str): 
    for char, index in enumerate(str):
        # if char in forbidden_characters:
        print char, index, "Fuckin\' curly quotes!!!!"

# unfuck_your_string(sample_fucked_string)
# unfuck_your_string(other_sample_fucked_string)