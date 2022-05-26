    def sum_of_smaller(self, now):
        t = [0]                     #建立一個lst計算節點值加總
        def inorder(now):           #建立使now做中序走訪的方法
            if now:                 
                inorder(now.left)   #從左子樹開始做中序走訪
                t[0] += now.val     #按照走訪順序，now與父節點的值都會加入t
                now.val = t[0]      #將小於等於now的總和指定為新的now
                inorder(now.right)  #右子樹做中序走訪                    
    
        inorder(now)

#留言板