    def sum_of_smaller(self, now):
        self.total=0
        self.SUM(now)
    def SUM(self, now):
        self.SUM(now.left)
        self.total += now.val
        self.SUM(now.right)
        self.total += now.val

#留言板