# -*- coding: utf-8 -*-

print "Stuff works, ok"

# My first go at providing forbidden characters to my eventual function
forbidden_characters = ["“", "”", "‘", "’"]

magical_character_conversion_dict = {
    "“": "\"",
    "”": "\"", 
    "‘": "\'", 
    "’": "\'"
}

# Test strings and user input
sample_fucked_string = "“This shit looks casual but will fuck you up.”"
other_sample_fucked_string = "“Well, my favorite quote is ‘Good typography includes curly quotes,’ even though it can basically destroy your code.”"
unfucked_string = "These are words with no curly quotes."
string_from_terminal = raw_input("Gimme that string.")

def unfuck_your_string (str): 
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
unfuck_your_string(string_from_terminal)