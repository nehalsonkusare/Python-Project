class Book:
    def __init__(self,bid=0,bnm="nm",bath="ath",status=1):
        self.bid=bid
        self.bname=bnm
        self.bauthor=bath
        self.status=status

    def __str__(self):
        data=str(self.bid)+","+self.bname+","+self.bauthor+","+str(self.status)
        return data    

#if(__name__=="__main__"):
 #   b=Book(101,"dk","shrma")
  #  print(b)

