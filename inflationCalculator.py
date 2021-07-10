"""
This program is meant to take a year to convert from, a year to convert to,
as well as an amount, and provide you with the new amount of dollars in CAD
"""

def getCPI(year):
    """finds the CPI using text file"""
    
    offsetYear = 1914   #The year that the file starts at
    dataFile = open('CPI.txt')
    dataList = dataFile.read().split()
    CPI = dataList[year - offsetYear]
    CPI = CPI.strip()
    CPI = float(CPI)
    return CPI

def getInflationRate(fromCPI,toCPI,amountOfYears):
    rate = (((toCPI - fromCPI)/fromCPI) * 100) / amountOfYears 
    return rate

def getNewAmount(fromAmount,inflationRate):
    newAmount = fromAmount * inflationRate
    return newAmount

def main():
    print("\nThis program is an inflation calculator for 1914 to 2020. All amounts are in CAD "
              + "and based on the CPI. Also known as the Consumer Price Index\n")
    fromYear = int(input("What is the year you'd like to convert from? "))
    fromAmount = float(input("What is the amount in " + str(fromYear) + 
                       " CAD that you'd like to convert from? "))
    toYear = int(input("What is the year you'd like to convert to? "))
    amountOfYears = toYear - fromYear + 1
    
    # Get CPI and then inflation rate
    fromCPI = getCPI(fromYear)
    toCPI = getCPI(toYear)
    inflationRate = getInflationRate(fromCPI,toCPI,amountOfYears)
    
    # Calculate new amount in CAD given inflation rate and print it for user
    newAmount = getNewAmount(fromAmount, inflationRate)
    print("\nThe inflation rate for this time period from " + str(fromYear) +
          " to " + str(toYear) + " is " + str(inflationRate) + "%")
    
    print("\nThis means that ${:.2f} in {} CAD is equivalent to ${:.2f} in {} CAD".format(fromAmount,fromYear,newAmount,toYear))
    
main()
input()