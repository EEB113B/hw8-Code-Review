    def sum_of_smaller(self, now):
        self.list = []
        self.sum = 0
        self.SUM(now)

    def SUM (self,now):
        if now:
            self.SUM(now.left)
            self.List.append(now.val)
            self.sum = self.sum + now.val
            now.val = self.sum 
            print(now.val) 
            self.SUM(now.right)

#留言板