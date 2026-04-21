#!/usr/bin/env python3

import os
import sys
import socket

import time
import random
from multiprocessing import Process

__all__ = []
    
### Combination guessing functions

class CombinationMechanics:
    def __init__(self, length, chars):
        self.length = length
        self.chars = chars
        
    def risky_combo(self):
        each_digit = lambda: random.choice(list(self.chars)) # has a 1/A^nl chance of giving the same combination n times
        element = [each_digit() for i in range(self.length)] # has a 0% chance of giving O(∞)
        out = ''
    
        for elem in element:
            out += str(elem)
    
        return out

    def make_combo(self):
        # base = list(self.chars)
        self.risky_combo()

def check_combo(combo, username):
        if ...: # TODO: Make this if statement work
            return True
        return False

def main(length, chars):
    original_guess = CombinationMechanics(length, chars).make_combo() 
    guess = original_guess
    tries = 0
    already_guessed = []

    while not check_combo(guess):
        already_guessed.append(guess)
        guess = CombinationMechanics(length, chars).make_combo()
        tries += 1

        if guess in already_guessed:
            guess = CombinationMechanics(length, chars).make_combo()
            tries += 1
            if guess in already_guessed:
                return None # this has a 1/A^2l chance of failing (makes the gamble that if the same value appears multiple times then all ohers have been ran through)

# Has a 100% chance of finding the answer
def find_answer(length, chars, username):
    fvalstore = []
    bvalstore = []
    POTENTIAL_ANSWERS = []
    
    def forward():
        newlength = length + 1
        fvalstore.append(newlength)
        
    def backward():
        newlength = length
        bvalstore.append(newlength)
    
    p1 = Process(target=forward)
    p2 = Process(target=backward)

    number_of_times_tried = 0
    
    while True: # P(never getting the right answer) = 0
        i = 0
        
        out1 = main(fvalstore[0], CHARS); out2 = main(bvalstore[0], CHARS); POTENTIAL_ANSWERS.extend([out1, out2])
        fvalstore.clear(); bvalstore.clear()
        i += 1
        number_of_times_tried += 1
        
        if i == 100:
            for ans in POTENTIAL_ANSWERS:
                if check_combo(ans, username):
                    return [ans, number_of_times_tried]
                POTENTIAL_ANSWERS.remove(ans)

### Displaying data remotely

def client(port, info):
    HOSTNAME = '127.0.0.1'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOSTNAME, port))
        s.sendall(info.encode('utf-8')) # Encodes into binary
        print("Success")

### Runs program

if __name__ == '__main__':

    MOST_COMMON_LENGTH = 8
    CHARS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    if sys.argv[1] is None or sys.argv[2] is None: sys.exit(1) 
    
    name = sys.argv[1]
    port = sys.argv[2]
    length = MOST_COMMON_LENGTH
    
    out = find_answer(length, CHARS, name)
    client(port, out[1])
    time.sleep(1)
    client(port, out[2])