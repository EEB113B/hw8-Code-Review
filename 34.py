    def sum_of_smaller(self, now):
        def inorder(now):  
            if now:  
                inorder(now.left)  #now.left中序走訪
                total[0] += now.val  #將now和前方的值加入total
                now.val = total[0]  
                inorder(now.right)  #now.right中序走訪
        total = [0]  #預設total=0
        inorder(now) #中序走訪

#留言板