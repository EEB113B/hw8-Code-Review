    def sum_of_smaller(self, now):
        self.List = []
        self.total = 0
        self.SUM(now)
    
    def SUM(self,now):
        if now:
            self.SUM(now.left)
            self.List.append(now.val)
            self.total =  self.total + now.val
            now.val=self.total
            self.SUM(now.right)

#留言板