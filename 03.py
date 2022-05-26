    def inorder(self,p):        #遞迴演算
        if p:
            self.inorder(p.left)
            self.s += p.val     #將中序走訪先後走到的值進行加總
            p.val = self.s      #將節點原本的值改為加總後的值
            self.inorder(p.right)
     
    def sum_of_smaller(self, now):
        self.s = 0       #設一變數s用來放加總值
        self.inorder(now)#進入遞迴演算

#留言板