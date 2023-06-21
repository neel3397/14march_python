#normal code without exception
#print a
#code with exception
'''try:
    print(a)
except:
    print("invalid input!")'''

try:
  a=int(input("enter number1:"))
  b=int(input("enter number2:"))

  ans=a/b
  print(ans)

#except:
 #print("cant divide by zero")

except ValueError:
  print("only 0-9 allowed")

except ZeroDivisionError:
  print("cant divide by zero")

