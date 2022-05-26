    def sum_of_smaller(self, now):
        if now is None: return #如果現在的節點是空的，直接回傳
        self.sum_of_smaller(now.left) #走訪左節點
        now.val = sum(filter(lambda x: x<=now.val, lst))#filter()會將串列中的每個元素傳入Lambda函式進行條件判斷，最後回傳符合條件的元素，執行結果為串列中大於小於等於now.val的元素
        print(now.val) #印出走訪到的節點
        self.sum_of_smaller(now.right)#走訪右節點

#留言板