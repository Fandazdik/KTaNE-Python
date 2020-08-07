symbols = 'ß¶ϞϿѮѦѬ҂ѰҖҪҨҢӕ฿⅞⅜↑3ƕƻ♂₨₸ԩᴥѪ'
letters = 'abcdefghijklmnopqrstuvwxyz8'

conv_dict = {}

for i in range(27):
    conv_dict[letters[i]] = symbols[i]
    
grid = [['a','f','j','o','q','u','k'],
    ['b','a','k','l','s','u','v'],
    ['c','g','l','p','t','j','s'],
    ['d','h','m','q','p','v','y'],
    ['e','i','m','k','h','w','z'],
    ['d','b','n','r','e','z','8']]

for list_ in grid:
    print([conv_dict[letter] for letter in list_])