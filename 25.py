    def sum_of_smaller(self, now):
    
        self.Inorder(now)   #建立一個list
        self.change(now)    #更改各節點的值
        
    def Inorder(self,now):  #因為想用list寫，但原本的函式參數沒有引入list，所以自己再建立一個
        self.InorderList = []   #先建立空字串
        if now:     #如果所在位置不是None就執行
            self.InorderList = self.Inorder(now.left)   #向左走訪，將左邊的數加入list
            self.InorderList.append(now.val)    #讀取現在的位置加入list
            self.InorderList = self.InorderList + self.Inorder(now.right)   #向右走訪，將右邊的數加入list
        return self.InorderList     #將list回傳至上一層
    
    def change(self,now):
        total = 0
        if now:     #如果所在位置不是None就執行
            self.change(now.left)   #向左走訪
            for val in self.InorderList:    #將list中小於自己的數加起來
                if val <= now.val:
                    total += val
            now.val = total     #比自己小的數字總和取代原本的位置
            self.change(now.right)   #向右走訪

#留言板