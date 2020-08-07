import random

word_dict = [
    'YEAH',
    'YES',
    'YE',
    'MHMM',
    'ERM',
    'HM',
    'NO',
    'NAH',
    'READ',
    'RED',
    'SEEN',
    'SCENE',
    'YOU',
    'YOU ARE',
    'U R',
    'YOU\RE',
    'THEYRE',
    'THEY',
    'THERE',
    'THEIR',
    'THEY ARE',
    'THEY R',
    '   ',
    'NOTHING'
    ]

answer_list = ['UHHH', 'WHAT', 'WHAT?', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT', 'U', 'LIKE']

'''
place_dict = {}
for item in word_dict:
    place_dict[item] = random.randrange(6)
'''


final_dict = {}
for item in answer_list:
    final_dict[item] = random.sample(answer_list, k=len(answer_list))