d={}
with open('poem.txt','r') as f:
    for line in f:
        for word in line.split():
            if word in d:
                d[word]+=1
            else:
                d[word]=1
print(d)