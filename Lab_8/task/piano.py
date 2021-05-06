#Midi Through:Midi Through Port-0 14:0

import keyboard
import mido
 
print(mido.get_output_names()) 
stringP = input("Enter a port - ")

port = mido.open_output(stringP)
keys = keys = {'1': 48, '2': 49, '3': 50, '4': 51, '5': 52, '6': 53, '7': 54, '8': 55, '9': 56, '0': 57, '-': 58, '=': 59, 'q': 60, 'w': 61, 'e': 62, 'r': 63, 't': 64, 'y': 65, 'u': 66, 'i': 67, 'o': 68, 'p': 69, '[': 70, ']': 71, 'a': 72, 's': 73, 'd': 74, 'f': 75, 'g': 76, 'h': 77, 'j': 78, 'k': 79, 'l': 80, ';': 81, "'": 82, 'enter': 83}
pressed_keys = {key: False for key in keys.keys()}
 
def hook(key):
    if key.event_type == "down":
        if key.name in keys:
            if not pressed_keys[key.name]:
                port.send(mido.Message('note_on', note=keys[key.name]))
                pressed_keys[key.name] = True
 
    if key.event_type == "up":
        if key.name in keys:
            port.send(mido.Message('note_off', note=keys[key.name]))
            pressed_keys[key.name] = False
 
keyboard.hook(hook)
keyboard.wait()