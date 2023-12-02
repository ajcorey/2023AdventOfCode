import re

def main():
    calDoc = open("puzzleInput.txt","r")
    sum = 0
    for line in calDoc:
        nums = re.findall("\d",line)
        sum += (int)(nums[0]+nums[-1])
    print(sum)

    calDoc.close()

if __name__ == "__main__":
    main()