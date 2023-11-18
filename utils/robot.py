from time import sleep

def dispatch(misty, actionType, value):
    print(f"Sending -> {actionType} with value: {value}")
    if(actionType == "speach"):
        misty.speak(value)
    if(actionType == "action"):
        misty.start_action(value, False)

    if(actionType == "moveForward"):
        misty.drive(10,0)
        sleep(value)
        misty.stop()

    if(actionType == "moveBackward"):
        misty.drive(-10,0)
        sleep(value)
        misty.stop()

    if(actionType == "turnRight"):
        misty.drive(0,-100)
        sleep(value)
        misty.stop()
    
    if(actionType == "turnLeft"):
        misty.drive(0,100)
        sleep(value)
        misty.stop()


    if(actionType == "reset"):
        misty.start_action('body-reset', False)


def doAction(misty, actions, actionNum):
    action = actions[actionNum]
    for actionType, value in action.items():
        dispatch(misty, actionType, value)
    #dispatch(misty, "reset", value)
