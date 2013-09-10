import re
import string

alphabet = string.ascii_letters

o_phrase = raw_input('Phrase to encrypt: ')
has_letter = re.search('[A-Za-z]', o_phrase)

if has_letter:
        e_phrase = ''
        for char in o_phrase:
                if char not in alphabet:
                        e_phrase = e_phrase + char
                else:
                        s_char = (alphabet.index(char) + 3) % 26
                        e_phrase = e_phrase + alphabet[s_char]
        print e_phrase
else:
	print 'That is not a valid word or phrase. Please try again.'
