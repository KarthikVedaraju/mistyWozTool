def dispatch(misty, actionType, value):
    print(f"Sending -> {actionType} with value: {value}")
    # if(actionType == "speach"):
    #     misty.speak(value)

def doAction(misty, actions, actionNum):
    action = actions[actionNum]
    for actionType, value in action.items():
        dispatch(misty, actionType, value)

