
from os import system, listdir
from pynput import keyboard
from colorama import Back, Fore, Style
from time import sleep
from random import Random, choice
print('***_TYPING_PRACTICE_***')


def getting_key():
    with keyboard.Events() as events:
    # Block for as much as possible
        event = events.get(1e6)
    return event.key

#    if event.key == keyboard.KeyCode.from_char(teste[0]):
#        print("YES")
path = 'texts/'
files_lst = listdir(path)
random_txt = choice(files_lst)
file = path + random_txt
txt=''
with open(file,'r') as f:
    for line in f:
        txt += line.lower()

total = len(txt)
count = 0
key = '' 
mytime = .05
while total > count:
    print(f'{Fore.GREEN}{txt[:count]}|{Fore.BLUE}{txt[count:]}')
    print('\n\n')
    # print('key:', key)
    print(f'score: {round(count*100/total)}%')
    key =  getting_key()
    if key == keyboard.KeyCode.from_char(txt[count]): 
        count +=1
        sleep(mytime)
        system('clear')
    elif key == keyboard.Key.space and txt[count] == ' ':
        count +=1
        sleep(mytime)
        system('clear')
    else: system('clear') 

print('over')