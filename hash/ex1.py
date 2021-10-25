arr=[]
with open('nyc_weather.csv',mode='r') as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        try:
            temp=int(tokens[1])
            arr.append(temp)
        except:
            print('invalid temperature, ignore the row')

print(sum(arr[:7])/7)
print(max(arr))