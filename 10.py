    def sum_of_smaller(self, now): #這個函式我用遞迴呼叫的寫法，一開始判斷當下節點是否為None，不是None的話，就往下執行，把樹上比當下節點的值小的值加起來，最後把當下節點的值和收集到的值加起來指定給當下節點的值，然後最後兩行以中序走訪的方式度回呼叫      
        if now != None: #'if'原先是中序走訪的寫法，再加上把當下節點的值改成自己與比自己小的樹葉相加
            collect = 0 #初始化一個值collcet來收集樹上比now的值小的值
            for i in range(len(lst)): #此迴圈是把樹上的值跑一遍
                if lst[i] < now.val: #比now的值小的值，加進collect
                    collect += lst[i]
            now.val = now.val + collect #把now的值與比now的值小的值相加
            self.sum_of_smaller(now.left) #遞迴呼叫，跟中序走訪的寫法一樣
            self.sum_of_smaller(now.right) #遞迴呼叫，跟中序走訪的寫法一樣

#留言板