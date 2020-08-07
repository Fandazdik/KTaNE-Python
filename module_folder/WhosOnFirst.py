
import random

class WhosOnFirst:
        
    def __init__(self, serial_parse = ''): # serial parse if necessary
            
        self.current_stage = 0
        self.total_stages = 5
        
        temp_words = WhosOnFirst.create_display()
        
        self.displayed_code = temp_words[0], temp_words[1]
        self.displayed = temp_words[0] + ': ' + ' '.join(temp_words[1])
        self.correct = str(temp_words[2] + 1)
        self.is_defused = False
        
    # ITEMS HERE PLEASE ===========================================
    position_dict ={
        "YEAH": 4,
        "YES": 2,
        "YE": 3,
        "MHMM": 1,
        "ERM": 3,
        "HM": 4,
        "NO": 5,
        "NAH": 2,
        "READ": 4,
        "RED": 5,
        "SEEN": 4,
        "SCENE": 2,
        "YOU": 1,
        "YOU ARE": 2,
        "U R": 2,
        "YOURE": 3,
        "THEYRE": 4,
        "THEY": 5,
        "THERE": 1,
        "THEIR": 0,
        "THEY ARE": 1,
        "THEY R": 4,
        "   ": 4,
        "NOTHING": 2
    }
    
    answer_list = ['UHHH', 'WHAT', 'WHAT?', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT', 'U', 'LIKE']


    label_dict = {
        "UHHH": [
            "READY",
            "MIDDLE",
            "U",
            "WHAT?",
            "NO",
            "OKAY",
            "YES",
            "FIRST",
            "LEFT",
            "NOTHING",
            "PRESS",
            "LIKE",
            "WAIT",
            "WHAT",
            "UHHH",
            "RIGHT",
            "BLANK"
        ],
        "WHAT": [
            "BLANK",
            "WAIT",
            "NOTHING",
            "MIDDLE",
            "LEFT",
            "RIGHT",
            "WHAT",
            "NO",
            "UHHH",
            "FIRST",
            "OKAY",
            "LIKE",
            "YES",
            "READY",
            "WHAT?",
            "U",
            "PRESS"
        ],
        "WHAT?": [
            "PRESS",
            "WHAT",
            "U",
            "WHAT?",
            "YES",
            "FIRST",
            "NO",
            "LEFT",
            "LIKE",
            "WAIT",
            "UHHH",
            "READY",
            "BLANK",
            "MIDDLE",
            "RIGHT",
            "OKAY",
            "NOTHING"
        ],
        "LEFT": [
            "LEFT",
            "LIKE",
            "U",
            "WHAT?",
            "YES",
            "RIGHT",
            "WHAT",
            "MIDDLE",
            "NO",
            "PRESS",
            "BLANK",
            "NOTHING",
            "UHHH",
            "OKAY",
            "READY",
            "WAIT",
            "FIRST"
        ],
        "NOTHING": [
            "OKAY",
            "NOTHING",
            "U",
            "LEFT",
            "FIRST",
            "WHAT",
            "PRESS",
            "NO",
            "MIDDLE",
            "RIGHT",
            "LIKE",
            "UHHH",
            "WHAT?",
            "READY",
            "WAIT",
            "BLANK",
            "YES"
        ],
        "READY": [
            "U",
            "WHAT",
            "YES",
            "LIKE",
            "UHHH",
            "NOTHING",
            "WAIT",
            "NO",
            "OKAY",
            "BLANK",
            "LEFT",
            "PRESS",
            "READY",
            "FIRST",
            "MIDDLE",
            "WHAT?",
            "RIGHT"
        ],
        "BLANK": [
            "UHHH",
            "YES",
            "WAIT",
            "LEFT",
            "READY",
            "NO",
            "WHAT",
            "BLANK",
            "U",
            "WHAT?",
            "FIRST",
            "MIDDLE",
            "OKAY",
            "PRESS",
            "LIKE",
            "NOTHING",
            "RIGHT"
        ],
        "MIDDLE": [
            "FIRST",
            "WHAT",
            "OKAY",
            "UHHH",
            "U",
            "LEFT",
            "YES",
            "READY",
            "NOTHING",
            "NO",
            "WHAT?",
            "LIKE",
            "WAIT",
            "PRESS",
            "RIGHT",
            "BLANK",
            "MIDDLE"
        ],
        "NO": [
            "PRESS",
            "OKAY",
            "MIDDLE",
            "BLANK",
            "WAIT",
            "NOTHING",
            "FIRST",
            "WHAT",
            "UHHH",
            "NO",
            "LEFT",
            "U",
            "LIKE",
            "WHAT?",
            "YES",
            "RIGHT",
            "READY"
        ],
        "OKAY": [
            "NO",
            "FIRST",
            "NOTHING",
            "U",
            "BLANK",
            "OKAY",
            "WHAT?",
            "MIDDLE",
            "WHAT",
            "LEFT",
            "UHHH",
            "READY",
            "YES",
            "PRESS",
            "WAIT",
            "LIKE",
            "RIGHT"
        ],
        "FIRST": [
            "LIKE",
            "RIGHT",
            "MIDDLE",
            "U",
            "BLANK",
            "READY",
            "NOTHING",
            "UHHH",
            "YES",
            "NO",
            "PRESS",
            "WHAT?",
            "WAIT",
            "LEFT",
            "FIRST",
            "OKAY",
            "WHAT"
        ],
        "WAIT": [
            "BLANK",
            "MIDDLE",
            "OKAY",
            "YES",
            "LIKE",
            "LEFT",
            "WHAT",
            "PRESS",
            "U",
            "WHAT?",
            "FIRST",
            "READY",
            "RIGHT",
            "UHHH",
            "NOTHING",
            "WAIT",
            "NO"
        ],
        "YES": [
            "WAIT",
            "RIGHT",
            "PRESS",
            "NOTHING",
            "LEFT",
            "BLANK",
            "WHAT?",
            "WHAT",
            "YES",
            "U",
            "FIRST",
            "LIKE",
            "NO",
            "MIDDLE",
            "READY",
            "OKAY",
            "UHHH"
        ],
        "PRESS": [
            "READY",
            "OKAY",
            "RIGHT",
            "BLANK",
            "WAIT",
            "LIKE",
            "NOTHING",
            "YES",
            "WHAT",
            "U",
            "NO",
            "FIRST",
            "MIDDLE",
            "UHHH",
            "LEFT",
            "WHAT?",
            "PRESS"
        ],
        "RIGHT": [
            "UHHH",
            "NOTHING",
            "LIKE",
            "LEFT",
            "YES",
            "OKAY",
            "RIGHT",
            "FIRST",
            "WHAT?",
            "NO",
            "READY",
            "U",
            "PRESS",
            "BLANK",
            "WHAT",
            "WAIT",
            "MIDDLE"
        ],
        "U": [
            "YES",
            "BLANK",
            "PRESS",
            "WHAT",
            "RIGHT",
            "OKAY",
            "NOTHING",
            "WAIT",
            "UHHH",
            "LEFT",
            "READY",
            "MIDDLE",
            "FIRST",
            "LIKE",
            "U",
            "WHAT?",
            "NO"
        ],
        "LIKE": [
            "OKAY",
            "WAIT",
            "U",
            "READY",
            "MIDDLE",
            "NO",
            "YES",
            "WHAT",
            "WHAT?",
            "PRESS",
            "RIGHT",
            "FIRST",
            "LIKE",
            "NOTHING",
            "BLANK",
            "LEFT",
            "UHHH"
        ]
    }
        

    
    # MECHANICS HERE
    def create_display():
        
        # Choose random word from possible lists
        big_word = random.choice(list(WhosOnFirst.position_dict.keys()))
        
        # Find the corresponding position (pythonic position)
        big_position = WhosOnFirst.position_dict[big_word]
        
        # Generate random list of 6 words
        small_words = random.sample(WhosOnFirst.answer_list, k = 6)
        
        # Find the word in the position dictated by big_word
        eye_word = small_words[big_position]
        
        # Find the list of words corresponding to the eye_word
        word_list = WhosOnFirst.label_dict[eye_word]
        
        
        # CHECK IF THERE ARE ANY WORDS IN THE WHOLE LIST IN THE 6 LIST
        if set(word_list) & set(small_words) == set():
            
            #If there is, replace a random word other than the eye word
            to_remove = small_words
            to_remove.remove(eye_word)
            word_to_remove = random.randchoice(to_remove)
            word_to_remove_index = small_words.index(to_remove)
            small_words[word_to_remove] = random.choice(word_list)
        
        # OTHERWISE! Find the first word that occurs in the 6 small_words
        else:
            matching_word = ''
            for word in word_list:
                if word in small_words:
                    matching_word = word
                    break
        
        # Find position where that first word occurs
        matching_index = small_words.index(matching_word)
                
        return big_word, small_words, matching_index
    
    def generate_new(self):
        temp_words = WhosOnFirst.create_display()
        
        self.displayed = temp_words[0], temp_words[1]
        self.correct = temp_words[2]
    
    def next_stage(self):
        
        WhosOnFirst.generate_new(self)
    
        self.current_stage += 1
        if self.current_stage == 5:
            WhosOnFirst.defused(self)
    
    def defused(self):
        self.is_defused = True
