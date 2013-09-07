alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

o_phrase = raw_input('Phrase to encrypt: ')

if len(o_phrase) > 0:
        e_phrase = ''
        for letter in o_phrase.upper():
                if letter not in alphabet:
                        e_phrase = e_phrase + letter
                else:
                        s_letter = (alphabet.index(letter) + 3) % 26
                        e_phrase = e_phrase + alphabet[s_letter]
        print e_phrase
else:
	print 'That is not a valid word or phrase. Please try again.'


"""
Future Features:

1. Decryption.

"""
