import json

def readMenuFile(mistyID):
    with open(f"config/misty{mistyID}/menu.json", 'r') as f:
        menu = json.load(f)
        return menu

def readActionFile(mistyID):
    with open(f"config/misty{mistyID}/actions.json", 'r') as f:
        menu = json.load(f)
        return menu