def toh(n,source,spare,target):
  
	if n == 1:
		print("move from {} to {}".format(source,target))
	else:
		toh(n-1,source,target,spare)
		print("move from {} to {}".format(source,target))
		toh(n-1,spare,source,target)


n=int(input("Enter number of Discs:"))
toh(n,'A','B','C')
