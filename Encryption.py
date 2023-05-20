from tkinter import *
import random
import math
def generatePass(length):
    characters = list(map(chr, range(65, 123)))
    newPas = ''
    l = 1
    if(length < len(characters) and length < 10):
        l = length
    else:
        l = len(characters)
    for i in range(l):
        n = random.randint(0, len(characters) - 1)
        newPas += characters[n]
        characters.pop(n)
    print("Your password is- " + newPas)
    p.delete(0, END)
    p.insert(0, newPas)
    return newPas
def swap(string, i1, i2):
    newS = ""
    for i in range(0, len(string)):
        if(i != i1 and i != i2):
            newS += string[i]
        elif(i == i1):
            newS += string[i2]
        elif(i == i2):
            newS += string[i1]
    return newS

def swapIn2D(list, i1, i2):
    newL = []
    for i in range(0, len(list)):
        if(i != i1 and i != i2):
            newL.append(list[i])
        elif(i == i1):
            newL.append(list[i2])
        elif(i == i2):
            newL.append(list[i1])
    return newL

def sorting(s):
    for i in range(0, len(s) - 1):
        less = i
        for x in range(i+1, len(s)):
            if ord(s[x]) < ord(s[less]):
                less = x
        s = swap(s, i, less)
    return s

def encrypt():
    text = getInfo()
    pas = generatePass(len(text) + 1)
    newText = ""
    for i in range(0, len(text), len(pas)):
        newText += pas
    text += " " * (len(newText) - len(text))
    codeList = []
    for i in range(0, len(text)):
        codeList.append((ord(text[i]) + ord(newText[i])))
    blocks = []
    blockLen = int(len(codeList) / len(pas) + 0.5)
    if blockLen >= 1:
        for i in range(0, len(pas)):
            temp = []
            for x in range(0, blockLen):
                try:
                    temp.append(codeList[x + i*blockLen])
                except:
                    break
            blocks.append(temp)
    else:
        blocks = codeList
    pasChange = pas
    
    for i in range(0, len(pas) - 1):
        less = i
        for x in range(i+1, len(pasChange)):
            if ord(pasChange[x]) < ord(pasChange[less]):
                less = x
        pasChange = swap(pasChange, i, less)
        blocks = swapIn2D(blocks, i, less)
    ret = ""
    for i in range(0, len(blocks)):
       for x in range(0, len(blocks[i])):
            ret += str(blocks[i][x]) + " "
    #print("Your code is-" + ret)
    password.delete('1.0', END)
    password.insert('1.0', ret)
    return ret
def decipher():
    text = getInfo()
    pas = p.get()
    codeList = text.split(" ")
    blockLen = int(len(codeList) / len(pas) + 0.5)
    list = []
    for i in range(0, len(pas)):
        l = []
        for x in range(0, blockLen):
            l.append(codeList[i*blockLen + x])
        list.append(l)
    blocks = []
    for i in range(0, len(pas)):
        blocks.append([])
    sortedPas = sorting(pas)
    order = []
    for i in range(0, len(pas)):
        for x in range(0, len(pas)):
            if(pas[i] == sortedPas[x]):
                order.append([x, i])

    for i in range(0, len(pas)):
        blocks[order[i][1]] = list[order[i][0]]
    index = 0
    for i in range(0, len(pas)):
        for x in range(0, blockLen):
            blocks[i][x] = chr(int(int(blocks[i][x]) - ord(pas[index % len(pas)])))
            index += 1

    returnString = ""
    for i in range(0, len(pas)):
        for x in range(0, blockLen):
            returnString += blocks[i][x]
    #print("Your encrypted text is- " + returnString)
    password.delete('1.0', END)
    password.insert('1.0', returnString)
    return returnString
def getInfo():
    st = ""
    inputs_1 = password.get('1.0', END)
    lines = inputs_1.splitlines()
    for line in lines:
        if line:
            st += line
    return st
tk = Tk()
tk.title("Encription")
tk.geometry('700x600')
lblTxt = Label(tk, text = "Input text/code here", font='Calibri')
lblTxt.pack(padx= 0, pady = 0)
password = Text(tk, width=80)
password.pack(padx=0, pady = 10)

toEncrypt = Button(tk, text = "Encrypt", command = encrypt)
toEncrypt.pack(side = RIGHT, padx=100, pady = 60)

toDecipher = Button(tk, text = 'Decipher', command = decipher)
toDecipher.pack(side = LEFT, padx=100, pady = 60)
lbl = Label(tk, text = "Password: ", font = "Calibri")
lbl.pack(side=LEFT, padx=0, pady = 0)
p = Entry(tk, width = 200)
p.pack(side = RIGHT, padx=0, pady = 0)
tk.mainloop()
