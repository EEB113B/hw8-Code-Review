    def sum_of_smaller(self, now):
    #判斷now有沒有東西
        if now:
            #走訪左節點
            self.sum_of_smaller(now.left) 
            #用filter過濾小於等於now節點值的數，並且加總
            #x小於now.val則存回lst中，最後加總
            now.val = sum(filter(lambda x: x<=now.val, lst)) 
            #走訪右節點
            self.sum_of_smaller(now.right)

#留言板