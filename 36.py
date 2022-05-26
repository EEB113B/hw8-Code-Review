    def sum_of_smaller(self, now):
        if now is None: #假如節點是空的，回傳
             return
        self.sum_of_smaller(now.left)#走訪左節點
        self.sum_of_smaller(now.right)#走訪右節點
        now.val = sum(filter(lambda x: x<=now.val, lst)) #過濾出自己與所有比自己小的節點值作加總

#留言板