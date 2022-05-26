    def sum_of_smaller(self, T):
  
        
            
        def cumsum_rec2(node, initial):
            if node is None:  
                return initial
            left = cumsum_rec2(node.left, initial)
            node.val = left + node.val #先加左子樹的值
            right = cumsum_rec2(node.right, node.val) #再加右子樹的值
            return right #回傳
        
        #L = []
        #cumsum_rec1(self.root,L) 
    
        cumsum_rec2(self.root, 0)

#留言板