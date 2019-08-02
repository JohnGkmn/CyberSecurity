n=37415923547017213098893819652088052694795252162093236205030866324359578830858399212088135936525894972381
# Python program to print prime factors 
  
import math 

# A function to print all prime factors of  
# a given number n 
def find_cube_root(n):
	low = 0
	high = n
	while low < high:
		mid = (low+high)//2
		if mid**3 < n:
			low = mid+1
		else:
			high = mid
	print(low)
print(find_cube_root(n))
