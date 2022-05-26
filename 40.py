    def sum_of_smaller(self, now):
        # global total
        if now==bst.root:                 ##當傳入的根結點==原本的根結點進入
            self.total=0                  ##設立self.total，並賦值為0
        if now:                           ##如果now不等於None，進入
            self.sum_of_smaller(now.left) ##仿中序走訪，找小節點
            self.total+=now.val                         ##將self.total+=現在當前節點
            now.val=self.total                          ##再將self.total賦值給當前節點
            self.sum_of_smaller(now.right)

#留言板