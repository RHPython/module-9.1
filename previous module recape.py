people = ['Ananto','Rezwan','Hamid','Asif','Kabir','mohashin']
print(people[0])
# List
thislist = ["Apple","Banna","Cherry"]
print(thislist)
# Allow Duplicates
thislist = ["Apple","Banna","Cherry","Apple","Cherry"]
print(thislist)
# List Length
thislist = ["Apple","Banna","Cherry"]
print(len(thislist))
# List Items - Data Types
# List items can be of any data type:
list1 = ["Apple","Bananna","Cherry"]
list2 = [1,2,3,4,5]
list3 = [True,False,False]
# A list with strings, integers and boolean values:
list1 = ["abc",34,True,40,"male"]
# type()
mylist = ["apple","bananna","cherry"]
print(type(mylist))
print(type(list2))
thislist = list (("apple","bananna","cherry"))# note the double round-bracket
print(thislist)
specify_list = ["apple","bananna","cherry","orange","kiwi","melon","mango"]
print(specify_list[2:5])
remove_element = ["Apple","bananna","Cherry","Orange","kiwi","melon","mango"]
print(remove_element[:4])
start_element = ["Apple","bananna","Cherry","Orange","kiwi","melon","mango"]
print(start_element[2:])
list_exists = ['apple','bananna','cherry']
if 'apple' in list_exists:
    print("Yes,'apple' is in the fruit list")
    