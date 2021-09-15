def Solve (N):
    lim = N // 2
    sum=0
    for i in range(1,lim+1):
        if N % i == 0:
            if i!=(N/i) and (N/i) < N:
                sum += i + (N / i)
            else:
                sum+=i
        if sum==N:
            return "YES"    
    return "NO"

# # PYTHON program to find sum of all
# # divisors of a natural number
# import math
	
# # Function to calculate sum of all proper
# # divisors num --> given natural number
# def divSum(num) :
	
# 	# Final result of summation of divisors
# 	result = 0
	
# 	# find all divisors which divides 'num'
# 	i = 2
# 	while i<= (math.sqrt(num)) :
	
# 		# if 'i' is divisor of 'num'
# 		if (num % i == 0) :
	
# 			# if both divisors are same then
# 			# add it only once else add both
# 			if (i == (num / i)) :
# 				result = result + i;
# 			else :
# 				result = result + (i + num/i);
# 		i = i + 1
		
# 	# Add 1 to the result as 1 is also
# 	# a divisor
# 	return (result + 1);

# # Driver program to run the case


# # This code is contributed by Nikita Tiwari

if __name__ == "__main__":
    print(Solve(28))