    def sum_of_smaller(self, now):
        if now is none: #節點是空的就回傳
            return
        #遞迴
        self.sum_of_smaller(now.left) #走訪左節點
        now.val = sum(filter(lanbda x: x<=now.val, list))#在filter中使用lambda篩選出lst中小於now的數,再用sum將符合的數相加
        self.sum_of_smaller(now.right)#走訪右節點

#留言板