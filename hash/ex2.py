d={}
with open('nyc_weather.csv','r') as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        try:
            temp=int(tokens[1])
            d[day]=temp
        except:
            print('invalid temperature, ignore line')

print(f'the temperature in jan 9 was {d["Jan 9"]}')
print(f'the temperature in jan 4 was {d["Jan 4"]}')