#!/usr/bin/python3

from mistyPy.Robot import Robot
import utils.files as files
import utils.robot as robot

mistyID = int(input("Misty ID: "))
misty = None
menu = None
actions = None

if(mistyID == 1):
    misty = Robot("192.168.0.73")
else:
    misty = Robot("192.168.0.41")

#menu = files.readMenuFile(mistyID)
actions = files.readActionFile(mistyID)

def printMenu():
    for n, action in actions.items():
        print(f"{n}: {action['description']}")


if __name__ == '__main__':
    while True:
        print("-------------------------------")
        printMenu()
        action = input("Action: ")
        robot.doAction(misty, actions, action)
        
