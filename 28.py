    def sum_of_smaller(self, now):
        self.sum = 0          #設定初始的加總值為0
        bst.inorder(bst.root) #呼叫inorder

    def inorder(self,node):   #以中序走訪的方式遞迴
        if node :             #如果node不是None
            bst.inorder(node.left) 
            self.sum += node.val  #將讀到值加到sum
            node.val = self.sum   #將node的值變為累加比自己小的值後的sum
            bst.inorder(node.right)

#留言板