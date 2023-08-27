# You have the list fruits = ['apple','banana','cherry']. How can you reverse the order of the items in the list?can you use to remove and return the last item from the list?

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
last_fruits = fruits.pop()
print(last_fruits)