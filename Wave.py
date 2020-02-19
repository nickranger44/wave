#!/bin/python3
import time

def user_input():
    while True:
        print("Enter a message that fits within 128 characters")
        msg = input("Message: ").strip()
        if len(msg) <= 128:
            break
        else:
            print("Your message is too damn long!")
    while True:
        while True:
            print("Enter how many times you want your message to wave (1-100)")
            try:
                num = int(input("Number: "))
            except ValueError:
                print("That's not a number silly")
            else:
                break
        if num > 100:
            print("Your number is too damn big!")
        elif num < 1:
            print("Okay... if that's what you want.")
            break
        else:
            break
    return msg, num

def print_wave(msg, num):
    msg_len = len(msg)
    for waves in range(num):
        for char in range(msg_len * 2):
            time.sleep(.05)
            if char < msg_len:
                print(msg[char:])
            else:
                print(msg[:char-(msg_len-1)])

msg, waves = user_input()
print_wave(msg, waves)
