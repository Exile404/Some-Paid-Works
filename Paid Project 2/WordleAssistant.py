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
def containsAll(wordlist, include):
    sett=set()
    l=[]
    for i in include:
        l.append(i)
    #abc
    #["a","b","c"]
    for i in range(len(wordlist)):
        has_all = all([char in wordlist[i] for char in l])
        if has_all==True:
            sett.add(wordlist[i])
    return sett
def containsNone(wordlist, exclude):
    sett = set()
    for i in range(len(wordlist)):
        x=wordlist[i]
        check=True
        for i in range(len(x)):
            if x[i] in exclude:
                check=False
                break
        if check:
            sett.add(x)
    return sett

def containsAtPositions(wordlist, posInfo):
    sett = set()
    for i in range(len(wordlist)):
        x=wordlist[i]
        c=0
        for j in range(len(x)):
            if x[j] in posInfo.keys():
                if posInfo[x[j]]==j:
                    c+=1
        if c==len(posInfo):
            sett.add(x)
    return sett

def getPossibleWords(wordlist, posInfo, include, exclude):
    l1=containsAtPositions(wordlist, posInfo)
    l2=containsAll(wordlist, include)
    l3=containsNone(wordlist, exclude)
    intersection = set.intersection(l1, l2, l3)
    return intersection

