

class hash:
    def __init__(self):
        self.MAX=5
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for c in key:
            h+=ord(c)
        return h%self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        star=h
        while self.arr[h]!=None:
            h+=1
            h=h%self.MAX
            if star==h:
                print('hash is full')
                return
        self.arr[h] = (key,value)
        return

    def __getitem__(self, key):
        h = self.get_hash(key)
        star = h
        while self.arr[h]==None or self.arr[h][0]!=key:
            h += 1
            h = h % self.MAX
            if star==h:
                print('element not found')
                return
        return self.arr[h][1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        star = h
        while self.arr[h] == None or self.arr[h][0] != key:
            h += 1
            h = h % self.MAX
            if star == h:
                print('element not found')
                return
        self.arr[h]=None

if __name__ == '__main__':
    ha=hash()
    ha['karam']='baqa'
    print(ha.arr)
    del ha['karam']
    print(ha.arr)
    ha['karam']=7
    ha['marak']=6
    print(ha.arr)
    del ha['karam']
    print(ha.arr)
    ha['amrak'] = 6
    ha['mraak'] = 6
    ha['maark'] = 6
    ha['marka'] = 6
    ha['amark'] = 6
    print(ha.arr)
    del ha['marak']
    print(ha.arr)