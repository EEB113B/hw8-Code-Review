    def sum_of_smaller(self, now):
        def inorder(now): #now中序走訪
            if now: 
                inorder(now.left) #now.left中序走訪
                total[0] += now.val #按照中序走訪的順序，now與前方的值都會加入total
                now.val = total[0] #將小於等於now的總和指定為now
                inorder(now.right) 
        total = [0] #預設total = 0
        inorder(now)

#留言板