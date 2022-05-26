    def sum_of_smaller(self, now):
        def add_sum(root, sum):
            
            if root != None:
                add_sum(root.left, sum)
                sum[0] = sum[0] + root.val
                root.val = sum[0]
                add_sum(root.right, sum)
        
        sum = [0]
        now == self.root
        add_sum(now, sum)

#留言板