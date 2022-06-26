import os.path
import secrets


def duplicates(s):
    s1=''
    for i in s:
        if i not in s1:
            s1+=i
    if len(s)==len(s1):
        return True
    return False


def createWordlist(wordfile):
    with open(wordfile+".txt", 'r') as f:
        lines = f.read().split("\n")
    wordlist=[]
    for i in range(len(lines)):
        x=lines[i]
        check=duplicates(x)
        if check==True and len(x)==5 and x[len(x)-1]!='s':
            wordlist.append(x)
    n=len(wordlist)
    return wordlist,n

s="Welcome to WORDLE, the popular word game. The goal is to guess a\n"\
"five letter word chosen at random from our wordlist. None of the\n"\
"words on the wordlist have any duplicate letters.\n\n"\
"You will be allowed 6 guesses. Guesses must be from the allowed\n"\
"wordlist. We'll tell you if they're not.\n\n"\
"Each letter in your guess will be marked as follows:\n\n"\
"   x means that the letter does not appear in the answer\n"\
"   ^ means that the letter is correct and in the correct location\n"\
"   + means that the letter is correct, but in the wrong location\n\n"\
"Good luck!\n"
print(s)
while True:
    wordfile = input("Enter the name of the file from which to extract the wordlist: ")
    file_exists = os.path.exists(wordfile+".txt")
    if file_exists==True:

        break
    else:
        print("File does not exist. Try again!")
wordlist,count=createWordlist(wordfile)
#x='frank'
x=secrets.choice(wordlist)
k=1
check=True
print()
while k<=6:
    s=input(f"Enter your guess ({k}): ")
    if s not in wordlist:
        print("Guess must be a 5-letter word in the wordlist. Try again!")
        continue
    c=0
    l=[]
    for j in range(len(s)):
        if x[j]==s[j]:
            c+=1
            l.append("^")
        elif s[j] in x:
            l.append("+")
        else:
            l.append("x")
    for i in s:
        print(i.upper(),end="  ")
    print()
    for i in l:
        print(i, end="  ")
    print()
    if c==5:
        print("CONGRATULATIONS! You win!")
        check=False
        break
    k+=1

if check:
    print("Sorry! The word was tacky. Better luck next time!")
