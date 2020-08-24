import random
from colorama import Fore, Back
class CrazyTalk:
        
    def __init__(self, serial_parse): # serial parse if necessary
              
        temp_result = CrazyTalk.create_display(serial_parse)
        self.displayed = temp_result[0]
        self.correct = temp_result[1]
        self.is_defused = False
        
        
    CTData = {
        '← ← → ← → →': (5,4),
        '1 3 2 4': (3,2),
        'LEFT ARROW LEFT WORD RIGHT ARROW LEFT WORD RIGHT ARROW RIGHT WORD':   (5,8),
        'BLANK':   (1,3),
        'LITERALLY BLANK': (1,5),
        'FOR THE LOVE OF ALL THAT IS GOOD AND HOLY PLEASE FULLSTOP FULLSTOP.': (9,0),
        'AN ACTUAL LEFT ARROW LITERAL PHRASE': (5,3),
        'FOR THE LOVE OF - THE DISPLAY JUST CHANGED, I DIDNT KNOW THIS MOD COULD DO THAT. DOES IT MENTION THAT IN THE MANUAL?':   (8,7),
        'ALL WORDS ONE THREE TO FOR FOR AS IN THIS IS FOR YOU':    (4,0),
        'LITERALLY NOTHING':   (1,4),
        'NO, LITERALLY NOTHING':   (2,5),
        'THE WORD LEFT':   (7,0),
        'HOLD ON ITS BLANK':  (1,9),
        'SEVEN WORDS FIVE WORDS THREE WORDS THE PUNCTUATION FULLSTOP': (0,5),
        'THE PHRASE THE WORD STOP TWICE':  (9,1),
        'THE FOLLOWING SENTENCE THE WORD NOTHING': (2,7),
        'ONE THREE TO FOR':    (3,9),
        'THREE WORDS THE WORD STOP':   (7,3),
        'DISREGARD WHAT I JUST SAID. FOUR WORDS, NO PUNCTUATION. ONE THREE 2 4.':  (3,1),
        '1 3 2 FOR':   (1,0),
        'DISREGARD WHAT I JUST SAID. TWO WORDS THEN TWO DIGITS. ONE THREE 2 4.':   (0,8),
        'WE JUST BLEW UP': (4,2),
        'NO REALLY.':  (5,2),
        '← LEFT → LEFT → RIGHT':   (5,6),
        'ONE AND THEN 3 TO 4': (4,7),
        'STOP TWICE':  (7,6),
        'LEFT':    (6,9),
        '..':  (8,5),
        'PERIOD PERIOD':   (8,2),
        'THERE ARE THREE WORDS NO PUNCTUATION READY? STOP DOT PERIOD': (5,0),
        'NOVEBMER OSCAR SPACE, LIMA INDIGO TANGO ECHO ROMEO ALPHA LIMA LIMA YANKEE SPACE NOVEMBER OSCAR TANGO HOTEL INDEGO NOVEMBER GOLF': (2,9),
        'FIVE WORDS THREE WORDS THE PUNCTUATION FULLSTOP': (1,9),
        'THE PHRASE: THE PUNCTUATION FULLSTOP':    (9,3),
        'EMPTY SPACE': (1,6),
        'ONE THREE TWO FOUR':  (3,7),
        'ITS SHOWING NOTHING':    (2,3),
        'LIMA ECHO FOXTROT TANGO SPACE ALPHA ROMEO ROMEO OSCAR RISKY SPACE SIERRA YANKEE MIKE BRAVO OSCAR LIMA':   (1,2),
        'ONE 3 2 4':   (3,4),
        'STOP.':   (7,4),
        '.PERIOD': (8,1),
        'NO REALLY STOP':  (5,1),
        '1 3 TOO 4':   (2,0),
        'PERIOD TWICE':    (8,3)
    }


    

    def create_display(serial_parse):
        
        '85.425.3-y2'
        ['90', '755', '4', 'd', '1']
        
        # Choose random item from list
        chosen_display = random.choice(list(CrazyTalk.CTData.keys()))
        lowercase_display = Fore.YELLOW + chosen_display.lower() + Fore.RESET
        
        # Get the tuple corresponding
        answer_tuple = CrazyTalk.CTData[chosen_display]
        
        # Calculate the answer from the tuple and the serial
        calculated_answer = (answer_tuple[0] * int(serial_parse[0]), answer_tuple[1] * int(serial_parse[1]))
        
        calculated_answer = calculated_answer[0] + calculated_answer[1]
        
        
        # Convert to A0J9
        calculated_answer = ''.join([chr(int(char) + 65) for char in str(calculated_answer)])
        
        return lowercase_display, calculated_answer
    
    
    def defused(self):
        self.is_defused = True

