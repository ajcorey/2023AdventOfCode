import re

def main():
    calDoc = open("puzzleInput.txt","r")
    # calDoc = open("subset.txt","r")
    sum = 0
    for line in calDoc:
        nums = re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))',line)
        for i in range(len(nums)):
            match nums[i]:
                case "zero":
                    nums[i]="0"
                case "one":
                    nums[i]="1"
                case "two":
                    nums[i]="2"
                case "three":
                    nums[i]="3"
                case "four":
                    nums[i]="4"
                case "five":
                    nums[i]="5"
                case "six":
                    nums[i]="6"
                case "seven":
                    nums[i]="7"                    
                case "eight":
                    nums[i]="8"
                case "nine":
                    nums[i]="9"

        sum += (int)(nums[0]+nums[-1])
    print(sum)

    calDoc.close()

if __name__ == "__main__":
    main()