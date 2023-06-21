mystr="hello, hi this is python"

print(mystr) #print the string
print(mystr[0]) #to print the string at character at index 0
print(mystr[1]) #to print the character at index 1
print(mystr[0:5]) #slicing of the string from index 0 to 4


print(len(mystr)) # to find the length of string

print(mystr.strip()) #to remove the space from first and last
print(mystr.upper()) #to convert string in upper case
print(mystr.lower()) #to convert string in lower case

print(mystr.replace('hi','bye')) #//to replace the word

print(mystr.capitalize()) #to make first character in capital

print(mystr.casefold())  #to make the last word character in lower case


print(mystr.count('hello')) #repition of word

print(mystr.startswith('n'))#to check if the string is starting with the given character or not
print(mystr.endswith('n'))#to check if the string is ending with the given character or not

print(mystr.index('h'))  #to check the index value  of an character

print(mystr.isalpha())  #to check string alphabet or not

print(mystr.isdigit())  #to check the string contains digit or not

print(mystr.isalnum())  #to check the string alphabet numeric

print(mystr.lower())   #to check the string lower case or not

print(mystr.upper())   #to check the string upper case or not

print(mystr.title())   #to write the string in title format