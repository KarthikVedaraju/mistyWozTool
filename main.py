from mistyPy.Robot import Robot
import utils.files as files
import utils.robot as robot

mistyID = 1
misty = None
menu = None
actions = None

if(mistyID == 1):
    misty = Robot("192.168.0.73")
else:
    misty = Robot("192.168.0.41")

menu = files.readMenuFile(mistyID)
actions = files.readActionFile(mistyID)

def printMenu():
    for n, command in menu.items():
        print(f"{n}: {command}")


if __name__ == '__main__':
    while True:
        print("-------------------------------")
        printMenu()
        action = input("Action: ")
        robot.doAction(misty, actions, action)
        
