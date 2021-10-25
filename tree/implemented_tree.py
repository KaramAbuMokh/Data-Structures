'''
implementing a tree
'''


class nodeTree:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def add_child(self, node):
        node.parent=self
        self.children.append(node)

    def prnt(self):
        sp='  '*self.get_level() + '|__'
        print(sp+self.data)
        for child in self.children:
            child.prnt()

    def get_level(self):
        lev = 0
        node = self.parent
        while node:
            lev += 1
            node = node.parent
        return lev

if __name__ == '__main__':
    a=nodeTree('a')

    b = nodeTree('b')
    b.add_child(nodeTree('c'))
    b.add_child(nodeTree('d'))
    b.add_child(nodeTree('e'))
    b.add_child(nodeTree('f'))

    g = nodeTree('g')
    g.add_child(nodeTree('h'))
    g.add_child(nodeTree('i'))
    g.add_child(nodeTree('j'))

    k = nodeTree('k')
    k.add_child(nodeTree('l'))
    k.add_child(nodeTree('m'))
    k.add_child(nodeTree('n'))

    a.add_child(b)
    a.add_child(g)
    a.add_child(k)

    a.prnt()
