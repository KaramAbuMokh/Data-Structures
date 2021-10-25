'''
implementing tree with title for each node
'''

class nodeTree:
    def __init__(self, data,title):
        self.parent = None
        self.children = []
        self.data = data
        self.title=title

    def add_child(self, node):
        node.parent=self
        self.children.append(node)

    def prnt(self):
        sp='  '*self.get_level() + '|__'
        print(sp+self.data+' '+self.title)
        for child in self.children:
            child.prnt()

    def prnt_title(self):
        sp='  '*self.get_level() + '|__'
        print(sp+self.title)
        for child in self.children:
            child.prnt_title()

    def prnt_data(self):
        sp = '  ' * self.get_level() + '|__'
        print(sp + self.data)
        for child in self.children:
            child.prnt_data()

    def get_level(self):
        lev = 0
        node = self.parent
        while node:
            lev += 1
            node = node.parent
        return lev


if __name__ == '__main__':
    a = nodeTree('Nilupul','CEO')

    b = nodeTree('Chinmay','CTO')

    v = nodeTree('Vishwa', 'Infrastructure Head')
    v.add_child(nodeTree('Dhaval','Cloud Manager'))
    v.add_child(nodeTree('Abhijit','App Manager'))

    w = nodeTree('Aamir', 'Application Head')

    b.add_child(v)
    b.add_child(w)

    c = nodeTree('Gels','HR Head')
    c.add_child(nodeTree('Peter', 'Recruitment Manager'))
    c.add_child(nodeTree('Waqas', 'Policy Manager'))


    a.add_child(b)
    a.add_child(c)

    a.prnt()
    print('-------------------------------------------------')
    a.prnt_title()
    print('-------------------------------------------------')
    a.prnt_data()