def create():
    text = open("Life Progress.txt","w+")
    text.write(
    """Current progress:

Carrers:
Nuclear Engineering 0; Programming 0; Astronomy 0; Physics 0; Mathematics 0

Hobbies:
Philosophy 0; Literature 0; Alt Rock Music 0; Jazz Music 0; Classic Music 0; Musical Theory 0; Cine 0; English 0; Russian 0

Techniques:
Gym 0; Swim 0; Guitar 0; Sing 0; Piano 0; Snowboard 0""")
    text.close()

def show(subjects, matters_all):
    scores_career = get_scores(matters_career)
    scores_hobbies = get_scores(matters_hobbies)
    scores_techniques = get_scores(matters_techniques)
    scores_all = [scores_career, scores_hobbies, scores_techniques]

    for i in range(len(subjects)):
        print(subjects[i] + "\n")
        for j in range(len(matters_all[i])):
            print("{: <25}".format(matters_all[i][j]) + " " + "[" + "{: <9}".format("#"*scores_all[i][j]) + "]")
        print("")

def get_scores(matters_list):
    list_of_scores = []
    text = open("Life Progress.txt","r+")
    str1 = text.read()

    for i in range(len(matters_list)):
        list_of_scores.append(int(str1[(re.search(matters_list[i],str1).end() + 1):(re.search(matters_list[i],str1).end() + 2)]))
        text.seek(0)

    text.close()
    return list_of_scores
    
def change_values(matters_specific):
    n1 = None
    n2 = None
    n1_range = []
    for i in range(len(matters_specific)+1):
        n1_range.append(i-1)
    
    while True:
        try:
            print("Choose: ")
            for i in range(len(matters_specific)):
                print("'{}' to {}.".format(i+1, matters_specific[i]))
            print("'0' to undo.\n")
            n1 = ((int(input()) - 1))
            clear()
            if n1 not in n1_range:
                print("Input out of bounds. Try again")
                continue

            if n1 == -1:
                clear()
                break
            n2 = input("To what value do you want to change it? From 1 to 9. Press '0' to undo.\n\n")
            clear()
            if int(n2)<0 or int(n2)>10:
                print("Input out of bounds. Try again")
                continue

            if n2 == "0":
                n2 = None
                continue
            return n1, n2

        except:
            clear()
            print("Error, invalid input. Try again.")

def change_text(n1, n2, matters_specific):
    text = open("Life Progress.txt","r+")
    str1 = text.read()
    str1 = str1[:(re.search(matters_specific[n1],str1).end() + 1)] + n2 + str1[(re.search(matters_specific[n1],str1).end() + 2):]
    text.seek(0)
    text.write(str1)
    text.close()

import re
import os
clear = lambda: os.system('cls')

if not os.path.isfile("Life Progress.txt"):
    create()
end = 0

subjects = ["Careers: ", "Hobbies: ", "Techniques: "]
matters_career = ("Nuclear Engineering", "Programming", "Astronomy", "Physics", "Mathematics")
matters_hobbies = ("Philosophy", "Literature", "Alt Rock Music", "Jazz Music", "Classic Music", "Musical Theory", "Cine", "English", "Russian")
matters_techniques = ("Gym", "Swim", "Guitar", "Sing", "Piano", "Snowboard")  
matters_all = [matters_career, matters_hobbies, matters_techniques]

while end != 1:
    ch2 = None
    show(subjects, matters_all)
    ch = input("Choose:\n'1' to change subject progress.\n'2' to close.\n\n")
    clear()


    while True:
        try:
            if ch == "1":
                while True:
                    ch2 = input("Choose: \n'1' to Careers.\n'2' to Hobbies.\n'3' to Techniques.\n'0' to undo.\n\n")
                    clear()

                    if ch2 == "1":
                        (n1, n2) = change_values(matters_career)
                        change_text(n1, n2, matters_career)
                    elif ch2 == "2":
                        (n1, n2) = change_values(matters_hobbies)
                        change_text(n1, n2, matters_hobbies)
                    elif ch2 == "3":
                        (n1, n2) = change_values(matters_techniques)
                        change_text(n1, n2, matters_techniques)
                    elif ch2 == "0":
                        pass
                    else:
                        clear()
                        print("Input out of bounds. Please try again.\n")
                    break
            elif ch == "2":
                end = 1
            else:
                print("Input out of bounds. Please try again.\n")
            break
        except:
            continue
