food_list=["salad","paneer","pizza","sevpuri"]
print(food_list)
print(food_list[0])  #fetch particular value from list
print(food_list[-1]) #last value from list
print(food_list[1:])
print(food_list[:1])

print(len(food_list)) #to find the length of list

'''for iteams in food_list:
    print(iteams)'''

#print(food_list.index("paneer"))

#food_list.append("chips")
#food_list.insert(2,"kurkure")
#print(food_list)

#food_list.remove("pizza")
#print(food_list)

food_list.pop()
#print(food_list) #to remove the last iteam

food_list.pop(2)
#print(food_list)  #to remove the iteam from index value

food_list.reverse()
#print(food_list)  #to reverse the list

#food_list.sort()
#print(food_list)   #to sort the list

#food_list.clear()
#print(food_list)    #to empty list

#del food_list
#print(food_list)    #to delete whole list and give error



restaurant_list=["macd","hocco","subway"]
print(restaurant_list)

print(restaurant_list+food_list)

restaurant_list.extend(food_list)