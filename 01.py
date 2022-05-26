    def sum_of_smaller(self, now):
        def inorder(now): #now中序走訪
            if now: #if now 存在
                inorder(now.left) #now.left中序走訪
                total[0] += now.val #按照中序走訪的順序，now和先前的值都會加入total
                now.val = total[0] #將小於等於now的總和指定為now
                inorder(now.right) #now.right中序走訪
        total = [0] #將total的起始值定為 0
        inorder(now) #中序走訪

#留言板