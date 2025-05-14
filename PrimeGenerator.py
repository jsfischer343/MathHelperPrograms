import math
import os
import datetime

def menu():
    print("1)Endless Primes")
    print("2)Limit")
    print("3)Prime Distribution")
    print("4)PrimeToCompositeRatio")
    print("5)Exit")
    menuOption = input("\n>>>")
    return menuOption

def endlessPrimes():
    a = 3
    primes = [2]
    while a<100000000000000:
        count = -1
        while 1==1:
            if math.sqrt(len(primes))<=(count+1):
                print(a)
                primes.append(a)
                break
            else:
                count = count + 1
            if a%primes[count]==0:
                break
        a=a+1
    primes = []

def limit():
    os.system("cls")
    limit = input("Print the largest prime less than: ")
    limit = int(limit)
    datetime1 = datetime.datetime.now()
    a = 3
    primes = [2]
    while a<limit:
        count = -1
        while 1==1:
            ##check if enough prime factors for the current
            ##...number has been check if so it is prime
            if math.sqrt(len(primes))<=(count+1):
                if(len(primes)%500==0):
                    os.system("cls")
                    print("Print the largest prime less than: "+str(limit))
                    print(a)
                primes.append(a)
                break
            ##else check more prime factors
            else:
                count = count + 1
            ##check if a is composite if so break out of loop and increment a
            if a%primes[count]==0:
                break
        a=a+1
    os.system("cls")
    print("Print the largest prime less than: "+str(limit))
    datetime2 = datetime.datetime.now()
    timeDif = calTimeDif(datetime1,datetime2)
    print(str(primes[len(primes)-1]))
    print("Time: "+timeDif)
    primes = []
    os.system("pause")

def calTimeDif(datetime1, datetime2):
    timeDif = datetime2-datetime1
    return str(timeDif)

def primeDistrbution():
    os.system("cls")
    limit = input("limit(grouped by 100s): ")
    limit = int(limit)+1
    datetime1 = datetime.datetime.now()
    a = 3
    primes = [2]
    ##number of primes in that row
    rowSum=1
    print("100s",end="")
    print("-*-",end="")
    while a<limit:
        count = -1
        if(a%100==0):
            print(str(rowSum),end="")
            print("\n"+str(a+100)+"s",end="")
            rowSum=0
        while 1==1:
            ##check if enough prime factors for the current
            ##...number has been check if so it is prime
            if math.sqrt(len(primes))<=(count+1):
                print("*",end="")
                rowSum=rowSum+1
                primes.append(a)
                break
            ##else check more prime factors
            else:
                count = count + 1
            ##check if a is composite if so break out of loop and increment a
            if a%primes[count]==0:
                print("-",end="")
                break
        a=a+1
    datetime2 = datetime.datetime.now()
    timeDif = calTimeDif(datetime1,datetime2)
    print("\nTime: "+timeDif)
    primes = []
    os.system("pause")

##compares average primes to composite numbers as a increases
def ratioPrimesToComposite():
    os.system("cls")
    limit = input("limit: ")
    limit = int(limit)
    datetime1 = datetime.datetime.now()
    a = 3
    primes = [2]
    ratioPtoCArray = []
    compositeCount=1
    while a<limit:
        count = -1
        ##cal current ratio of primes to composite numbers
        if(a%200==0):
            ratioPtoC=float(len(primes))/float(compositeCount)
            ratioPtoCArray.append(ratioPtoC)
            print(str(ratioPtoC))
        while 1==1:
            ##check if enough prime factors for the current
            ##...number has been check if so it is prime
            if math.sqrt(len(primes))<=(count+1):
                primes.append(a)
                break
            ##else check more prime factors
            else:
                count = count + 1
            ##check if a is composite if so break out of loop and increment a
            if a%primes[count]==0:
                compositeCount=compositeCount+1
                break
        a=a+1
    datetime2 = datetime.datetime.now()
    timeDif = calTimeDif(datetime1,datetime2)
    ratioPtoC=float(len(primes))/float(compositeCount)
    derivativeOfRatio = rateOfChangeOfRatio(ratioPtoCArray)
    print(str(ratioPtoC))
    print("Rate of Change of Primes to Composite Numbers Over "+str(a)+" Numbers:\n"+str(derivativeOfRatio))
    print("Time: "+timeDif)
    primes = []
    os.system("pause")

def rateOfChangeOfRatio(array):
    derivativeArray = []
    for x in range(len(array)-1):
        derivativeArray.append(array[x+1]-array[x])
    sum = 0
    for y in range(len(derivativeArray)):
        sum=sum+derivativeArray[y]
    average=sum/len(derivativeArray)
    return average
        

#Main Program
loop=1    
while(loop==1):
    os.system("cls")
    menuOption = menu()
    if(menuOption=="1"):
        endlessPrimes()
    elif(menuOption=="2"):
        limit()
    elif(menuOption=="3"):
        primeDistrbution()
    elif(menuOption=="4"):
        ratioPrimesToComposite()
    elif(menuOption=="5"):
        loop=0
    else:
        print("Invalid Input!")
        os.system("timeout 2")