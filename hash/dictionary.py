

class hash:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for c in key:
            h+=ord(c)
        return h%self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        self.arr[h]=value
        return

    def __getitem__(self, item):
        h=self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None

if __name__ == '__main__':
    ha=hash()
    ha['karam']='baqa'
    print(ha.arr)
    del ha['karam']
    print(ha.arr)