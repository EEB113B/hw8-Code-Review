    def sum_of_smaller(self, now):
        def cumsum_rec1(node, L):
            L.append(node.val)
            if node.left != None:
                cumsum_rec1(node.left, L)  

            if node.right != None:
                cumsum_rec1(node.right, L)
            count = 0  #做累積
            for val in L:
                if val < node.val:
                    count += val   #比她小的加進來
            node.val +=count

        L = []
        cumsum_rec1(self.root, L)

#留言板