    def sum_of_smaller(self, now):
        
        if now is None: #節點是空的就回傳
            return 
        self.sum_of_smaller(now.left)    #走訪左節點
        now.val = sum(filter(lambda x: x<=now.val, lst)) #如果小於now的值就相加
        self.sum_of_smaller(now.right)   #走訪右節點

#留言板