'''
6 across
7 down

27 symbols

---------------------------

'ß¶ϞϿѮѦѬ҂ѰҖҪҨҢӕ฿⅞⅜↑3ƕƻ♂₨₸ԩᴥѪ'

'ß', '¶','Ϟ', 'Ͽ', 'Ѯ', 'Ѧ', 'Ѭ', '҂', 'Ѱ', 'Җ', 'Ҫ', 'Ҩ', 'Ң', 'ӕ', '฿', '⅞', '⅜', '↑', '3', 'ƕ', 'ƻ', '♂', '₨', '₸', 'ԩ', 'ᴥ', 'Ѫ'
[
['ß', 'Ѧ', 'Җ', '฿', '⅜', 'ƻ', 'Ҫ'],
['¶', 'ß', 'Ҫ', 'Ҩ', '3', 'ƻ', '♂'],
['Ϟ', 'Ѭ', 'Ҩ', '⅞', 'ƕ', 'Җ', '3'],
['Ͽ', '҂', 'Ң', '⅜', '⅞', '♂', 'ԩ'],
['Ѯ', 'Ѱ', 'Ң', 'Ҫ', '҂', '₨', 'ᴥ'],
['Ͽ', '¶', 'ӕ', '↑', 'Ѯ', 'ᴥ', 'Ѫ']
]
'''

import random
class Keypad:
        
    def __init__(self, serial_parse = ''): # serial parse if necessary
             
        temp_symbols = Keypad.generate_keypad()
        
        self.displayed_code = temp_symbols[0]
        self.displayed = ' '.join(self.displayed_code)
        self.correct = ''.join([str(i) for i in (temp_symbols[1])])
        self.is_defused = False
    
    # MECHANICS HERE
    
    
    def generate_keypad():
        
        grid = [
                ['ß', 'Ѧ', 'Җ', '฿', '⅜', 'ƻ', 'Ҫ'],
                ['¶', 'ß', 'Ҫ', 'Ҩ', '3', 'ƻ', '♂'],
                ['Ϟ', 'Ѭ', 'Ҩ', '⅞', 'ƕ', 'Җ', '3'],
                ['Ͽ', '҂', 'Ң', '⅜', '⅞', '♂', 'ԩ'],
                ['Ѯ', 'Ѱ', 'Ң', 'Ҫ', '҂', '₨', 'ᴥ'],
                ['Ͽ', '¶', 'ӕ', '↑', 'Ѯ', 'ᴥ', 'Ѫ']
            ]
        
        # Choose a random line
        rand_line = random.randrange(6)
        chosen_line_grid = grid[rand_line]
        
        # Get 4 random symbols and their indexes
        symbols = random.sample(chosen_line_grid, k=4)
        indexes = [chosen_line_grid.index(char) for char in symbols]
        
        # Sort the indexes
        indexes = sorted(indexes)
        
        # And then convert them back to symbols
        answer = [chosen_line_grid[index] for index in indexes]
        
        # Add one for intuitivity
        answer = [symbols.index(symbol) + 1 for symbol in answer]

        return symbols, answer
        
    
    
    def defused(self):
        self.is_defused = True
