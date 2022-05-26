    def sum_of_smaller(self, now):

        self.after_inorder_lst = []                     # 先設一個空的 list 好讓等等中序走訪後修改完可以放進去
        self.inorder(now)                               # 呼叫 inorder 方法
        self.after_inorder(now)                         # 呼叫 after_inorder 方法

    def inorder(self,now):                              # 傳入 self 跟 now 參數
        if now != None:                                 # 如果 now 為 True，就開始進行中序走訪
            self.inorder(now.left)                      # 先去左邊
            self.after_inorder_lst.append(now.val)      # 再把中間的值先暫存進 after_inorder_lst 裡
            self.inorder(now.right)                     # 最後再去右邊
    
    def after_inorder(self,now):                        # 傳入 self 跟 now 參數
        self.sum = 0                                    # 設 sum 變數為 0
        if now != None:                                 # 如果 now 為 True 
            self.after_inorder(now.left)                # 先進去左邊
            for num in self.after_inorder_lst:          # 開始重新排序
                if num <= now.val:                      # 如果 now 裡面的值大於 num 
                    self.sum += num                     # 把 num 加到 sum 裡去
            now.val = self.sum                          # 最後把 sum 的值回傳給 now
            self.after_inorder(now.right)               # 最後才去右邊重新整理

#留言板