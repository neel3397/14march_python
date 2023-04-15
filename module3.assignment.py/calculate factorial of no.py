def factiorial(n):
    if n==0:
        return 1
    else:
        return n*factiorial(n-1)
n=int(input ("a number to compute the factiorial:"))
print(factiorial(n))