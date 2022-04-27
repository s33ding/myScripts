import os
from pynput import keyboard
from colorama import Back, Fore, Style
from time import sleep
from random import Random, choice

def gettingKey():
    with keyboard.Events() as events:
    # Block for as much as possible
        event = events.get(1e6)
    return event.key

#    if event.key == keyboard.KeyCode.from_char(teste[0]):
#        print("YES")
            
def typingWord(word):

    total = len(word)
    count = 0
    key = '' 
    mytime = .05
    while total >= count:
        print(f'{Fore.GREEN}{word[:count]}|{Fore.BLUE}{word[count:]}')
        print('\n\n')
        # print('key:', key)
        score = round(count*100/total)
        print(f'score: {score}%')
        key =  gettingKey()
        if score == 100:
            break 
        
        elif key == keyboard.KeyCode.from_char(word[count]): 
            count +=1
            sleep(mytime)
            os.system('clear')
        elif key == keyboard.Key.space and word[count] == ' ':
            count +=1
            sleep(mytime)
            os.system('clear')
        else: os.system('clear') 
