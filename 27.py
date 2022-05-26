    def sum_of_smaller(self, now):
       self.inorderlst = []                     #建立一中序走訪的list
       self.inorder(now)                        #執行中序走訪
       self.plus_and_change(now)                #將list中的元素加起來並取代原本

    def inorder(self, now):
        if now:                                 #如果這元素有值的話
            self.inorder(now.left)              #向左走訪
            self.inorderlst.append(now.val)     #將此元素加入list中
            self.inorder(now.right)             #向右走訪

    def plus_and_change(self, now):
        self.total = 0                          #設定一值
        if now:                                 #如果這元素有值的話
            self.plus_and_change(now.left)      #向左走訪
            for val in self.inorderlst:          
                if val <= now.val:              #如果這元素大於list中的值的話
                    self.total += val           #將total加入這一值
            now.val = self.total                #將這一元素更換成total
            self.plus_and_change(now.right)     #向左走訪   

#留言板