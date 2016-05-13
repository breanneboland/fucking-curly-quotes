# -*- coding: utf-8 -*-

print "Stuff works, ok"

forbidden_characters = ["“", "”", "‘", "’"]

# print "The array", forbidden_characters

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"", 
    "‘": "\'", 
    "’": "\'"
}

# print "The dict", magical_character_conversion_dict

sample_fucked_string = "“This shit looks casual but will fuck you up.”"

# print "Sample fucked string: ", sample_fucked_string

other_sample_fucked_string = "“Well, my favorite quote is ‘Good typography includes curly quotes,’ even though it can basically destroy your code.”"

unfucked_string = "These are words with no curly quotes."

# def detect_curly_quotes (str):
#     if "!" in str:
#         print "The function recognized a curly quote!"

# detect_curly_quotes(sample_fucked_string)
# detect_curly_quotes(other_sample_fucked_string)

def unfuck_your_string (str): 
    # for index, char in enumerate(str):
    #     if char in forbidden_characters:
    #         print char, index, "Fuckin\' curly quotes!!!!"
    if "“" in str:
        print "true"
    elif "”" in str:
        print "true"
    elif "‘" in str:
        print "true"
    elif "’" in str:
        print "true"
    else:
        print "false"

unfuck_your_string(sample_fucked_string)
unfuck_your_string(other_sample_fucked_string)
unfuck_your_string(unfucked_string)