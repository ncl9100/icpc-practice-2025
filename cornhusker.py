#ICPC 2023 GNY Question A

import sys

input = sys.stdin.readline

def main():
    nums = list(map(int, input().split()))

    row_17_5, KWF = map(int, input().split())

    avg = 0
    curr = 0 

    for i in range(0, len(nums)):
        if(i%2==0):
            curr = nums[i]
        else:
            curr = curr * nums[i]
            avg +=curr
            curr = 0
    avg = avg//5

    print(avg * row_17_5 // KWF)


main()
