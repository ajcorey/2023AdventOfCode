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
        for sym in re.finditer(r"[\*]",rowArr[i]):
            if sym is not None:
                s = symbol(sym.start(),i)
                print("g")
                symList.append(s)

        for num in re.finditer(r"(\d+)",rowArr[i]):
            if num is not None:
                n = numb(num.start(),num.end(),i,num.group(0))
                numlist.append(n)
        
        i += 1  

    #part 1

    # j=0
    # for j in range(len(numlist)): 
    #     # print(numlist[j].val)
    #     k=0
    #     for k in range(len(symList)):
    #         if (numlist[j].row-1 <= symList[k].row) and \
    #             (numlist[j].row+1 >= symList[k].row) and \
    #             (numlist[j].s_col-1 <= symList[k].col) and \
    #             (numlist[j].e_col >= symList[k].col):
    #                 # print("col") 

    #             print(numlist[j].val)
    #             totalSum += int(numlist[j].val)
    #             break

    #         k += 1

    #     j += 1

    
    j=0
    for j in range(len(symList)):
        k=0
        cnt = 0
        r_arr = []
        for k in range(len(numlist)):
            if (numlist[k].row-1 <= symList[j].row) and \
                (numlist[k].row+1 >= symList[j].row) and \
                (numlist[k].s_col-1 <= symList[j].col) and \
                (numlist[k].e_col >= symList[j].col):
                cnt += 1  
                r_arr.append(numlist[k])       

            k += 1
        if cnt == 2:
            m=int(r_arr[0].val)*int(r_arr[1].val)
            totalSum += m
            r_arr = []
            cnt=0
        else:
            r_arr = []
            cnt=0

        j += 1


    print(totalSum)
    engineSN.close()

if __name__ == "__main__":
    main()