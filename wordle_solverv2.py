import random
words=[]
wconfirm={}
wpr={}
with open("valid_wordle_answers.txt") as f:
    for line in f:
        words.append(line.strip())
def wsolver(words):
    print("Try the word SLATE")
    gword="slate"
    wrem=[]
    while True:
        result=input("Did it work? y or n ")
        result=result.lower()
        if result=='y':
            print("wordle solved!")
            return
        else:
            print("Enter the resulting color array [B,Y,G] -->")
            result=input()
            for i in range(5):
                    if result[i]=='B' and gword[i] not in wconfirm and gword[i] not in wpr:
                                wrem.append(gword[i])
                    elif result[i]=='Y':
                                wpr[gword[i]]=i
                    elif result[i]=='G':
                        wconfirm[gword[i]]=i
            temp=[]
            for i in words:
                  temp.append(i)
            print(temp)
            for i in words:
                for k in wconfirm:
                        if i[wconfirm[k]]!=k and i in temp:
                              temp.remove(i)
                for k in wrem:
                      if k in i and i in temp:
                            temp.remove(i)
                for k in wpr:
                    if i[wpr[k]]==k and i in temp:
                            temp.remove(i)
                    if k not in i and i in temp:
                          temp.remove(i)
            print(temp)
            if len(temp)==0:
                  randind=random.randint(0,len(words)-1)
            else:
                randind=random.randint(0,len(temp)-1)
                words=temp 
            gword=words[randind]
            print("Try the word ",words[randind])
wsolver(words)

