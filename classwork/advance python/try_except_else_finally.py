"""
try:
    exception code
except:
    after exception statement
else:
    without exception
finally:
    it always occur"""

'''try:

    a=10
    b=30

    ans=a+b
    print(ans)

except:
    print("invalid input")

else:
    print("welcome to math word")

finally:
    print("welcome to my application")'''

'''l1=[3,6,8,9,1,7]

print(l1)

try:
    print(l1[9])

except:
    print("index out of range")

else:
    print(l1)'''

try:
    print(a)
except Exception as e:
    print(e)