# テキストの品詞を書き換える

import re


def is_vowel(word):
    regex = re.compile(r'^[AIUEO]+')
    if regex.match(word):
        return True
    else:
        return False


text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

part_of_speech_regex = re.compile(r'ADJECTIVE|ADVERB|NOUN|VERB')

s = text
while part_of_speech_regex.search(s):
    mo = part_of_speech_regex.search(s)
    part_of_speech = mo.group()
    
    if is_vowel(part_of_speech):
        replacement = input(f'Enter an {part_of_speech.lower()}: \n')
    else:
        replacement = input(f'Enter a {part_of_speech.lower()}: \n')

    s = part_of_speech_regex.sub(replacement, s, count=1)

print(s)