


class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if self.data==data:
            return
        if data<self.data:
            if self.left==None:
                self.left=BinaryTreeNode(data)
            else:
                self.left.add_child(data)

        if data > self.data:
            if self.right == None:
                self.right = BinaryTreeNode(data)
            else:
                self.right.add_child(data)

    def order_traversal(self):
        '''
        print the base node in order

        :return:
        '''
        if self.left!=None:
            self.left.order_traversal()

        print(str(self.data) + '---')
        if self.right != None:
            self.right.order_traversal()


    def pre_order_traversal(self):
        '''
        print the base node before the children
        :return:
        '''
        print(str(self.data) + '---')

        if self.left != None:
            self.left.post_order_traversal()

        if self.right != None:
            self.right.post_order_traversal()

    def post_order_traversal(self):
        '''
        print the base node after printing the children
        :return:
        '''

        if self.left != None:
            self.left.post_order_traversal()

        if self.right != None:
            self.right.post_order_traversal()

        print(str(self.data) + '---')

    def find_max(self):
        node=self
        while node.right !=None:
            node=node.right
        return node.data

    def find_min(self):
        node = self
        while node.left != None:
            node = node.left
        return node.data


    def print_reversed(self):
        '''
        print the tree in reversed order
        :return:
        '''
        if self.right!=None:
            self.right.print_reversed()

        print(str(self.data) + '---')
        if self.left != None:
            self.left.print_reversed()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
        '''if self==None:
            return 0
        if self.left != None and self.right!=None:
            return self.data+ self.left.calculate_sum()+self.right.calculate_sum()
        if self.left != None and self.right==None:
            return self.data+ self.left.calculate_sum()
        if self.left == None and self.right!=None:
            return self.data+self.right.calculate_sum()
        if self.left == None and self.right==None:
            return self.data'''

    def delete_val(self,val):
        if val < self.data:
            if self.left :
                self.left.delete_val(val)
                return

        elif val > self.data:
            if self.right :
                self.right.delete_val(val)
                return

        elif self.left is None and self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        mini=self.right.find_min()
        self.data=mini
        self.right=self.right.delete_val(mini)

    def delete_val1(self,val):
        if val < self.data:
            if self.left :
                self.left.delete_val(val)
                return

        elif val > self.data:
            if self.right :
                self.right.delete_val(val)
                return

        elif self.left is None and self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        max=self.left.find_max()
        self.data=max
        self.left=self.left.delete_val(max)




if __name__ == '__main__':
    t=BinaryTreeNode(17)
    t.add_child(4)
    t.add_child(1)
    t.add_child(9)
    t.add_child(20)
    t.add_child(18)
    t.add_child(23)
    t.add_child(34)
    t.order_traversal()
    t.delete_val1(20)
    t.order_traversal()
