def sumnumber(n):
	if n==1:
		ans=n+sumnumber(n-1)
		return ans
n=int(input("enter value:"))
print(sumnumber(n))		