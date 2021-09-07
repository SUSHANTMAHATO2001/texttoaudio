import time
import os
import sys


try:
     import gtts

except ImportError:
       os.system('python2 -m pip install gTTs')

os.system('clear')
os.system('apt install play-audio -y')
os.system('clear')
from gtts import *

class color:
       g = '\x1b[;33m'
       r = '\x1b[;32m'

def susan(s):
    for a in s + '\n':
       sys.stdout.write(a)
       sys.stdout.flush()
       time.sleep(1./12)
class text:
       p = 'Program By Sushant Mahato:2021-09-07th'
       d = 'Devlop By Nepal'
susan(color.g + text.p +'\n'+ color.r + text.d)

t = raw_input('Inter The Letter:-')
f = raw_input('Inter The Adio Name:-')

a = gTTS(t)
#a.save(f+'.mp3')
v = a.save(f)
os.system('play-audio v.mp3')
