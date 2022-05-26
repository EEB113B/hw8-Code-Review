    def sum_of_smaller(self, now):
        new_lst = []                                 # 用new_lst來存放新的數字
        tmp = [now]          
        while tmp!=[]:                               # 外層的迴圈用來選要改變的數字
            add = 0
            queue = [now]
            while queue!=[]:                         # 內層的用來判斷那些數字小於它
                if queue[0].val < tmp[0].val:
                    add += queue[0].val
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
            add += tmp[0].val
            new_lst.append(add)                     # 把算完的結果存到new_lst
            if tmp[0].left:
                tmp.append(tmp[0].left)
            if tmp[0].right:
                tmp.append(tmp[0].right)
            tmp.pop(0)
        bstNew = BST()                              # 創一個新的二元樹來讀新的lst
        for val in new_lst:
            bstNew.insert(val)
        bst.root = bstNew.root                      # 把舊的根指到新的二元樹上

#留言板