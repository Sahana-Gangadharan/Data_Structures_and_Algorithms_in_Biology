# def coinChange(arr,m):
# 	a= m
# 	n = len(arr)
# 	c=[]
# 	while a>arr[-1]:
# 		a-=arr[-1]
# 		c.append(arr[-1])

# 	while a>0:
# 		for i in range(n):
# 			print(i,arr[i])
# 			if arr[i]>a:
# 				a-=arr[i-1]
# 				c.append(arr[i-1])
# 				break
# 		print(a)
# 	print(c)

# def coinChange(amt,denom):
#     if amt in denom:
#         return 1
#     amount=[]
#     n=len(denom)
#     for i in range(n):
#         amount.append(coinChange((amt-denom[i]),denom))
#     return min(amount)

INF = 100000

def min(x, y):
  if x < y:
    return x
  return y

#k is number of denominations of the coin or length of d
def coinChange(d, n, k):
  M = [0]*(n+1)

  for j in range(1, n+1):
    minimum = INF

    for i in range(1, k+1):
    	if j >= (d[i]+1):
    		minimum = min(minimum, 1+M[j-d[i]])
		M[j] = minimum
	print(M)
	return M[n]

denom=[1,4,5]
coinChange(denom,8,3)
