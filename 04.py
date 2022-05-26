    def sum_of_smaller(self, now):
        a = []
        self.inorder(now, a)
        for i in range(1, len(a)): #for迴圈將list整理成每一項都是前面的所有項相加
            a[i] = a[i] + a[i-1]
        self.trans_(now, a)
        
    def inorder(self, p, list_): #中續走法，照順序將數字寫入list中
        if p:
            self.inorder(p.left, list_)
            list_.append(p.val) #將數字寫入list中
            self.inorder(p.right, list_)
    def trans_(self, p, list_): #中續走法，照順序將改好的list依序傳回給p.val
        if p:
            self.trans_(p.left, list_)
            p.val = list_[0] #將改好的list依序傳回給p.val
            list_.pop(0)
            self.trans_(p.right, list_)

#留言板