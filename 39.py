    def sum_of_smaller(self, now):
        if now != None: #節點不為無時執行中序走訪
            totle = 0
            self.sum_of_smaller(now.left) #走訪左節點
            for i in lst:             #計算值
                if i <= now.val:      #計算值
                    totle = totle + i #計算值
            now.val = totle #替換
            self.sum_of_smaller(now.right) #走訪右節點

#留言板