from click import getchar
from tabulate import tabulate
import pandas as pd
from speak import speak
from typingScript import gettingKey, typingWord
import os
from pynput import keyboard
from colorama import Back, Fore, Style
from time import sleep
import random
import subprocess
import re
import openpyxl

def mainFunction():
    df = pd.read_csv('verbs.csv')
    word = random.choice(df['Word'])
    wordSerie = [(a,b,c,d,f) for a,b,c,d,f in df.loc[df['Word'] == word].values]
    showing = df.loc[df['Word']==word]
    showTab = tabulate(showing, headers='keys')

    # showing.to_excel('exercise.xlsx')

    lst = []
    for x in  (str(showing.values).split(' ')):
        x = re.sub(r'\W','',x)
        lst.append(x)
    
    
    print(showTab)
    
    for i in range(2):
        speak(word)
        sleep(.3)

    os.remove('voice.mp3')
    for x in lst:
        typingWord(x)
        print(showTab)
        sleep(2)

power = True
while power==True:
    mainFunction()