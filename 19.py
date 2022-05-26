    def sum_of_smaller(self, now):
        self.total = 0                   #$設定全域變數
        self.SUM(now)                    #把節點放到SUM中
        
        
    def SUM(self, now):                  #用遞迴中序走訪方式找截點
        if now:                          #判斷截點是否為None
            self.SUM(now.left)           #往左截點走
            self.total += now.val        #if now=None就把此截點的直加上total
            now.val = self.total         #改變此截點的直
            self.SUM(now.right)          #再望右邊尋找截點

#留言板