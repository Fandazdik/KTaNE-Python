from datetime import datetime
import Bomb
# There's an annoying import thing where relative paths
# don't work when imported from another program
import ClockRoman

bomb = Bomb.Bomb(4)

divider_length = 60

def show_modules():
    print('Serial Code: ' + bomb.serial)
    print()
    print('=' * divider_length)
    for module in bomb.bomb_modules:
        print('[' + str(module[0]) + ']')
        print('Defused: ' + str(module[1].is_defused))
        print()
        print(module[1].displayed)
        print()
        print('=' * divider_length)
        
def show_module(num):

    global bomb
    global divider_length

    print('=' * divider_length)
    print('[' + str(num) + ']')
    print('Defused: ' + str(bomb.bomb_modules[num][1].is_defused))
    print()
    print(bomb.bomb_modules[num][1].displayed)
    print()
    print('Strikes: ' + str(bomb.strikes))
    print('=' * divider_length)

def spacer(amount):
    while amount != 0:
        print()
        amount -= 1
        
def lose():
    spacer(100)
    input('you\'re lose game over sorry')
    quit()

start_time = datetime.now()
in_module = False
module_num = ''
while 1:
    if not in_module:
        show_modules()
        module_num = int(input('> '))
        
        if module_num in list(range(len(bomb.bomb_modules))):
            in_module = True   
            
    elif in_module:
        show_module(module_num)
        input_ = input('> ')
        if input_ == 'leave':
            in_module = False
        elif input_ == bomb.bomb_modules[module_num][1].correct:
            bomb.bomb_modules[module_num][1].is_defused = True
            in_module = False
        else:
            bomb.strikes += 1
        
    
    if bomb.strikes == 3:
        lose()
    
    won = True
    for module in bomb.bomb_modules:
        if module[1].is_defused == False:
            won = False
            
    spacer(50)    
    if won == True:
        total_time = datetime.now()
        print('YEAH YOU WON')
        print('YOU FUCKING DID IT')
        print('IN ONLY ' + str((total_time - start_time).seconds) + ' SECONDS')
        print('WOOOOOOOOOO\n' * 10)
        input()
        quit()
    