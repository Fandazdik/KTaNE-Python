from numpy import array, where
from colorama import Fore, Back
import random

class Colorblindness:
        
    def __init__(self, serial_parse): # serial parse if necessary
        
        temp_grid = Colorblindness.create_grid()
        self.displayed = temp_grid[0]
        self.correct = temp_grid[1]
        self.is_defused = False
    
    # MECHANICS HERE
    def create_grid():
        
        
        
        def shuffle_keyval(dict_):
            keys = list(dict_.keys())
            values = list(dict_.values())
            
            values = random.sample(values, len(values))
            
            return dict(zip(keys, values))

        symbols = ['oe', 'ae', 'ai', 'oo', 'uu', 'ie', 'uo']
        symbols = random.sample(symbols, 4)

        num_colors = {
            0: Back.BLACK + Fore.WHITE + symbols[0] + Fore.RESET + Back.RESET,
            1: Back.WHITE + Fore.BLACK + symbols[1] + Fore.RESET + Back.RESET,
            2: Back.YELLOW + Fore.BLUE + symbols[3] + Fore.RESET + Back.RESET,
            3: Back.BLUE + Fore.YELLOW + symbols[2] + Fore.RESET + Back.RESET
            }

        #num_colors = shuffle_keyval(num_colors)

        grids = [
            array([
                [0, 1, 0, 3, 1],
                [2, 3, 2, 0, 0],
                [1, 2, 0, 2, 1],
                [2, 3, 3, 1, 2],
                [0, 2, 3, 1, 0]
                ]),
            
            array([
                [1, 2, 0, 2, 0],
                [1, 1, 1, 0, 3],
                [3, 3, 3, 3, 3],
                [3, 0, 1, 1, 1],
                [0, 2, 0, 2, 1]
                ]),
            
                array([
                [2, 2, 2, 0, 0],
                [0, 2, 1, 0, 0],
                [0, 1, 1, 1, 2],
                [0, 3, 3, 3, 2],
                [0, 2, 3, 2, 2]
                ]),
            
            array([
                [2, 0, 3, 3, 2],
                [3, 0, 2, 0, 2],
                [3, 2, 0, 3, 0],
                [1, 3, 2, 3, 1],
                [2, 1, 1, 1, 2]
                ]),
            
            array([
                [0, 1, 0, 1, 3],
                [3, 2, 0, 0, 2],
                [2, 2, 0, 3, 3],
                [3, 1, 1, 3, 2],
                [2, 0, 1, 0, 1]
                ]),
            
            array([
                [3, 1, 3, 2, 1],
                [2, 1, 0, 2, 3],
                [2, 1, 0, 1, 3],
                [0, 3, 2, 1, 2],
                [0, 3, 0, 0, 2]
                ]),
            
            array([
                [1, 0, 3, 0, 3],
                [0, 3, 0, 3, 2],
                [2, 0, 3, 2, 1],
                [3, 1, 2, 1, 2],
                [0, 3, 1, 2, 1]
                ]),
            
            array([
                [2, 2, 0, 3, 3],
                [2, 1, 3, 1, 3],
                [0, 0, 1, 3, 0],
                [2, 1, 1, 1, 0],
                [0, 1, 3, 1, 2]
                ]),
            
            array([
                [3, 2, 0, 3, 1],
                [2, 1, 3, 1, 3],
                [0, 3, 2, 3, 0],
                [1, 2, 1, 1, 2],
                [3, 0, 1, 0, 2]
                ]),
        ]
            
            
        chosen_list_index = random.randrange(9)
        chosen_list = grids[chosen_list_index]
        
        
        # 0:R, 1:G, 2:B, 3:W
        chosen_color = random.randrange(3)
        
        true_color_dict = {
            0: 'Red',
            1: 'Green',
            2: 'Blue',
            3: 'White'
        }
        
        chosen_color_text = true_color_dict[chosen_color]
        
        occurences = where(chosen_list == chosen_color)
        occurences = occurences[0][0], occurences[1][0]
        
        symbol_code = chosen_list[occurences[0]][occurences[1]]


        final_grid = ''
        for row in chosen_list:
            for item in row:
                final_grid += num_colors[item]
            
            final_grid += '\n'
            
        final_grid = chosen_color_text + '\n\n' + final_grid
        
        
        return final_grid, symbols[symbol_code]
        
    
    
    def defused(self):
        self.is_defused = True
