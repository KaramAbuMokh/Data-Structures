from stack import stack

s=stack()
left=['[','{','(']
right=[']','}',')']
square=['[',']']
se=['{','}']
circular=['(',')']
x=None

for i in "[a+b]*(x+2y)*{gg+kk}":
    if i in left:
        s.push(i)
    if i in right:
        out=s.pop()
        if out==None:
            x=False
            break
        if all(x in square for x in [i,out]):
            continue
        elif all(x in se for x in [i,out]):
            continue
        elif all(x in circular for x in [i,out]):
            continue
        else :
            x=False
            break
if x== None:
    print('True')
else:
    print('False')