#ICPC 2023 GNY Question I

import sys

input = sys.stdin.readline 

def main():
    n = int(input())
    curr = []
    validity = []

    isbns = []
    for i in range(n):
        isbns.append(input().strip())

    for i in range(1, n+1):

        hyphen_count = 0
        currDigit = 0
        sum = 0
        invalid = False



        for j in range(0, len(isbns[i-1])):

            if( (j==0 and isbns[i-1][0]=='-') or (j==len(isbns[i-1])-1 and isbns[i-1][-1]=='-') ):
                print("invalid")
                invalid = True
                break
            if(isbns[i-1][j] == '-'):
                hyphen_count +=1
                if(hyphen_count > 3):
                    print("invalid")
                    invalid = True
                    break
            if(j>0 and isbns[i-1][j-1]=='-' and isbns[i-1][j]=='-'):
                print("invalid")
                invalid = True
                break

            if(hyphen_count == 3):
                if(isbns[i-1][-2] !='-'):
                    print("invalid")
                    invalid = True
                    break
            
            if(isbns[i-1][j]!='-'):
                if(isbns[i-1][j]=='X' and currDigit ==9):
                    sum +=10
                    currDigit +=1
                elif(isbns[i-1][j]=='X' and currDigit !=9):
                    print("invalid")
                    invalid = True
                    break
                elif(isbns[i-1][j].isdigit()):
                    sum = sum + (10-currDigit) * int(isbns[i-1][j])
                    currDigit +=1
                else:
                    print("invalid")
                    invalid = True
                    break

        if(invalid == True):
            continue 

        isbn = isbns[i-1].replace("-", "")

        if(len(isbn)!=10):
            print("invalid")
            invalid = True
            continue
 
        if(sum%11!=0):
            print("invalid")
            continue
        else:
            sum = 0
            isbns[i-1] = '978-'+isbns[i-1][:-1]
            tracker = 0
            for j in range(0, len(isbns[i-1])):
                if(isbns[i-1][j].isdigit()):
                    if(tracker%2==0):
                        sum = sum + int(isbns[i-1][j])*1
                        tracker +=1
                    elif(tracker%2==1):
                        sum = sum + int(isbns[i-1][j])*3
                        tracker +=1
            digit = (10 - sum%10) % 10
            isbns[i-1] = isbns[i-1] + str(digit)

            print(isbns[i-1])

main()



                



    #check each isbn-10
        #less than or equal to 3 hyphens
        #no consecutive hyphens
        #cannot begin / end with hyphen
        #if 3 hyphens, checksum digit separated with hyphen

        #checksum rule S%11 ==0

    
