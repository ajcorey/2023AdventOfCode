import re

def main():
    gameList = open("puzzleInput.txt","r")
    # gameList = open("subset.txt","r")

    #for part 1
    # redLimit = 12
    # greenLimit = 13
    # blueLimit = 14

    # possibleSum = 0
    powerSum = 0
    for game in gameList:
        gBreakdown = re.split(r":|;",game)
        gameNum = int(re.split(r" ",gBreakdown[0])[1])

        # possibleRound = True
        redMax = 0
        greenMax = 0
        blueMax = 0

        for round in range(1,len(gBreakdown)):
            color = re.split(r",",gBreakdown[round])
            redNum = 0
            greenNum = 0
            blueNum = 0

            for c in color:
                if "red" in c:
                    redNum=int(re.split(r" ",c)[1])
                elif "green" in c:
                    greenNum=int(re.split(r" ",c)[1])
                elif "blue" in c:
                    blueNum=int(re.split(r" ",c)[1])

            # possibleRound = possibleRound and (redNum <= redLimit and greenNum <= greenLimit and blueNum <= blueLimit)
            redMax = max(redMax,redNum)
            greenMax = max(greenMax,greenNum)
            blueMax = max(blueMax,blueNum)

        gamePower = redMax * greenMax * blueMax

        powerSum += gamePower   

        # if possibleRound:
            # possibleSum += gameNum

    # print(possibleSum)
    print(powerSum)
    gameList.close()
if __name__ == "__main__":
    main()