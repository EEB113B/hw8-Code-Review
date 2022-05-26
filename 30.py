    def sum_of_smaller(self, now):
        self.total = 0
        self.count(now)
    def count(self,now):#另建一個function來做計算  
        if now:#用inorder走訪
            self.count(now.left)
            self.total += now.val#計算總合
            now.val = self.total#將原來的值改變
            self.count(now.right)                 

#留言板