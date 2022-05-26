    def sum_of_smaller(self, now):
        def inorder(now): 
            if now: 
                inorder(now.left) 
                total[0] += now.val 
                now.val = total[0] 
                inorder(now.right) 
        total = [0] 
        inorder(now) 

#留言板