#	Question
# 	Find the runtime of the below code

def powersOf2(n):                       
    # print("n:"+str(n))
    if n < 1:
        return 0                        # ------ Time complexity of this line = O(1)
    elif n == 1:
        print(1)                        # ------ Time complexity of this line = O(1)
        return 1
    else:
        prev = powersOf2(int(n/2))      # ------ Time complexity of this line = O(logN) because if you are geeting the runtime by halfing the equation, we get O(logN)
        # print("prev:"+str(prev))
        print(prev)
        curr = prev*2                   
        print(curr)                    
        return curr                     # ------ Time complexity of this line = O(1)

powersOf2(50)

#Summing up the time complexity of each line = O(logN)