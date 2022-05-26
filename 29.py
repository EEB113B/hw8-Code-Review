# 助教留言：為了Review介面簡潔，省略其他內容，只放同學有更改的部分

    def __init__(self):
        self.root = None
        self.total = 0

    def sum_of_smaller(self, now):
        if now!=None:#使用前序走訪遞迴
            self.sum_of_smaller(now.left)#先走到最左邊元素
            self.total+=now.val#total預設為0，將total加上當前節點
            now.val=self.total#將當前節點轉為total
            self.sum_of_smaller(now.right)#往右走訪

#留言板