    def sum_of_smaller(self, now):
        def inorder(now): #now中序走訪
            if now: #if now 存在
                inorder(now.left)  #now.left中序走訪
                sum[0] += now.val  #依據中序走訪，把now與前方的值都會加入sum
                now.val = sum[0]   #把小於等於now的總和指定為now
                inorder(now.right) #now.right中序走訪
        sum = [0]  #預設sum = 0
        inorder(now)  #中序走訪

#留言板