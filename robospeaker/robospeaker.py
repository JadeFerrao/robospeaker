import os
if __name__ == '__main__':
    print("This is Robo-Speaker")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q": #to quit
            os.system("say 'BYE BYE'")
            break
        command = f"say {x}"
        os.system(command)