    def sum_of_smaller(self, now):
        total =0        #計算比較此節點小的值加總
        self.recursive(now,total)

                 
    def recursive(self,now,total):#中序走訪
        if now:
            if now.left:
                self.recursive(now.left,total)

            if now.left:#如果左節點不是空的
                if now.left.right:#如果左節點的次右節點邊有值，就取代掉現在的total
                    total = now.left.right.val
                else:               #如果上述沒有值(None)，total就用左節點的值取代
                    total = now.left.val  
            total = total + now.val #把比此節點小的值加上自己
            now.val = total         #用total取代掉原本的值
            # print(now.val)
            if now.right:
                self.recursive(now.right,total)

#留言板