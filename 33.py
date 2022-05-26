    def sum_of_smaller(self, now):

        self.total=0#類別內全域變數
        self.SUM(now)
        def SUM(self,now):
            self.SUM(now.left)
            self.total+=now.val
            self.SUM(now.right)

#留言板