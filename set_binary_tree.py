from binary_tree import BinaryNode, BinaryTree

class BST_Node(BinaryNode):

    def subtree_find(self, k):
        if k < self.item.key:
            if self.left:
                return self.left.subtree_find(k)
        elif k > self.item.key:
            if self.right:
                return self.right.subtree_find(k)
        else:
            return self
        
        return None
    
    
    def subtree_find_next(self, k):
        if self.item.key <= k:
            if self.right:   return self.right.subtree_find_next(k)
            else:            return None
        
        elif self.left:
            node = self.left.subtree_find_next(k)
            if node:         return node

        return self
    

    def subtree_find_prev(self, k):
        if self.item.key >= k:
            if self.left:    return self.right.subtree_find_prev(k)
            else:            return None

        elif self.right:
            node = self.right.subtree_find_prev(k)
            if node:         return node

        return self
    

    def subtree_insert(self, node):
        if node.item.key < self.item.key:
            if self.left:    self.left.subtree_insert(node)
            else:            self.subtree_insert_before(node)

        elif node.item.key > self.item.key:
            if self.right:   self.right.subtree_insert(node)
            else:            self.subtree_insert_after(node)
        
        else:
            self.item= node.item