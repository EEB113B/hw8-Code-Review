    def sum_of_smaller(self, now):
        self.switch_list(now)   #呼叫switch_list方法
        self.change(now)        #呼叫change方法


    def switch_list(self,now):  #為了在change方法時可以用list
        self.List=[]            #設List是空的list
        if now:                 #防止now==None
            self.List=self.switch_list(now.left)    #走訪左節點
            self.List.append(now.val)               #節點的值append進List
            self.List=self.List+self.switch_list(now.right) #走訪右節點
        #print(self.List)
        return self.List        
    def change(self,now):           #加總自己與所有比自己小的節點值   
        total=0
        if now:                     #防止now==None
            self.change(now.left)   #遞迴，走訪左節點
            for val in self.List:   #取出List的值
                if val<=now.val:    #假如lst的值(val)小於等於節點的值
                    total+=val      #val加進total
            now.val=total           #節點的值用total取代掉
            self.change(now.right)  #走訪右節點
        
        
        #total=0
        #if now:  
            #self.sum_of_smaller(now.left)  #走訪左節點
            #for val in lst:        #取出lst的值
                #if val<=now.val:   #假如lst的值(val)小於等於節點的值
                    #total+=val     #val加進total
            #now.val=total          #節點的值用total取代掉
            #self.sum_of_smaller(now.right) #走訪右節點

#留言板