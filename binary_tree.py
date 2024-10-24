class BinaryNode:

    def __init__(self, item):
        self.item = item
        self.right = None
        self.left = None
        self.parent = None


    def subtree_traversal(self):

        if self.left:
            self.left.subtree_traversal()
        yield self
        if self.right:
            self.right.subtree_traversal()

        return array
    

    def subtree_first(self):

        if self.left:
            return self.left.subtree_first()
        else:
            return self
        
    
    def subtree_last(self):

        if self.right:
            return self.right.subtree_last()
        else:
            return self
        
    
    def successor(self):

        if self.right:
            return self.right.subtree_first()
        
        while self.parent:
            if self.parent.left == self:
                return self.parent
            else:
                self = self.parent
        else:
            return None
        
    
    def predecessor(self):
        
        if self.left:
            return self.left.subtree_last()
        
        while self.parent:
            if self.parent.right == self:
                return self.parent
            else:
                self = self.parent

        else:
            return None
        
    
    def subtree_insert_before(self, node):
        if self.left:
            self = self.left.subtree_last()
            self.right, node.parent = node, self

        else:
            self.left, node.parent = node, self

    
    def subtree_insert_after(self, node):
        if self.right:
            self = self.right.subtree_first()
            self.left, node.parent = node, self

        else:
            self.right, node.parent = node, self


    def subtree_delete(self):
        if self.left or self.right:

            if self.left: swap_node = self.predecessor()
            else: swap_node = self.successor()

            self.item, swap_node.item = swap_node.item, self.item

            return swap_node.subtree_delete()

        
        else:
            if self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None


class BinaryTree:

    def __init__(self, node_type = BinaryNode):
        self.root = None
        self.size = 0
        self.node_type = node_type

    def __len__(self):
        return self.size
    
    def __iter__(self):
        if self.root:
            for node in self.root.subtree_traversal():
                yield node.item


def build_subtree(array, a = 0, b = None):
    if b == None:
        b = len(array)

    if a + 1 >= b:
        return None
    else:
        c = (a + b) // 2
        root = BinaryNode(array[c])
        if c > a:
            root.left = build_subtree(array, a, c)
            root.left.parent = root

        if c < b:
            root.right = build_subtree(array, c, b)
            root.right.parent = root

    return root


array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(build_subtree(array))


