import re

class symbol:
    def __init__(self,col,row):
        self.col = col
        self.row = row
    
class numb:
    def __init__(self,s_col,e_col,row,val):
        self.s_col = s_col
        self.e_col = e_col
        self.row = row
        self.val = val

def main():
    engineSN = open("puzzleInput.txt","r")
    # engineSN = open("subset.txt","r")

    symList = []
    numlist = []

    totalSum=0

    rowArr = []
    for enRow in engineSN:
        rowArr.append(enRow)

    i = 0
    for i in range(len(rowArr)):
        print(rowArr[i])
        for sym in re.finditer(r"[^\d|\.|\n]",rowArr[i]):
            if sym is not None:
                s = symbol(sym.start(),i)
                symList.append(s)

        for num in re.finditer(r"(\d+)",rowArr[i]):
            if num is not None:
                n = numb(num.start(),num.end(),i,num.group(0))
                numlist.append(n)
        
        i += 1  

    j=0
    for j in range(len(numlist)): 
        # print(numlist[j].val)
        k=0
        for k in range(len(symList)):
            if (numlist[j].row-1 <= symList[k].row) and \
                (numlist[j].row+1 >= symList[k].row) and \
                (numlist[j].s_col-1 <= symList[k].col) and \
                (numlist[j].e_col >= symList[k].col):
                    # print("col") 

                print(numlist[j].val)
                totalSum += int(numlist[j].val)
                break

            k += 1

        j += 1

    print(totalSum)
    engineSN.close()

if __name__ == "__main__":
    main()