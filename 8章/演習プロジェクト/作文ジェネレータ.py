# テキストの品詞を書き換える

import re

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

part_of_speech_regex = re.compile(r'ADJECTIVE|ADVERB|NOUN|VERB')

s = text
while part_of_speech_regex.search(s):
    mo = part_of_speech_regex.search(s)
    part_of_speech = mo.group()
    
    if part_of_speech.startswith(('A', 'I', 'U', 'E', 'O')):
        replacement = input(f'Enter an {part_of_speech.lower()}: \n')
    else:
        replacement = input(f'Enter a {part_of_speech.lower()}: \n')

    s = part_of_speech_regex.sub(replacement, s, count=1)

print(s)
