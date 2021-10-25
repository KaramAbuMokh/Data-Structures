

class hash:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for c in key:
            h+=ord(c)
        return h%self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        for i,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][i]=(key,value)
                return
        self.arr[h].append((key,value))
        return

    def __getitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                return element[1]
        print('key not found')

    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                del self.arr[h][i]

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