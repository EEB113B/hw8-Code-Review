    def sum_of_smaller(self, now):
        # <將你的程式碼寫在這邊>
        self.List = []
        self.SUM(self.root)

        for i in self.List:
            total = 0
            if i < now:
                total = total + i
            now = total


    
    def SUM(self, now): # 存取走訪路徑
        if now:
            self.SUM(now.left)
            self.List.append(now.val)
            self.SUM(now.right)

#留言板