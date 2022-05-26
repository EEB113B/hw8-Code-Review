    def sum_of_smaller(self, now):
        self.total = 0              #設此遞迴一個類別變數total
        self.sum(now, self.total)   #呼叫sum()方法
            
    def sum(self, cur, total):
        if cur:                     #使用中序走訪
            self.sum(cur.left, self.total)
            self.total += cur.val   #將total加上走到的數
            cur.val = self.total    #將此跟節點設為total
            self.sum(cur.right, self.total)
            return self.total       #回傳self.total做累加
            
#留言板