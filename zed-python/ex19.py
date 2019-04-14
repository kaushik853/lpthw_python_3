def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
print(" We will try to get the input directly")
cheese_and_crackers(20,50)
print("we will get it with variables")
x = 90
y = 100
cheese_and_crackers(x,y)
print(" we will try to get it from user")
count_of_cheese_input = input('please enter the cheese count\n')
count_of_cheese = int(count_of_cheese_input)
count_of_crackers_input = input('please enter the cracker count\n')
count_of_crackers = int(count_of_crackers_input)
cheese_and_crackers(count_of_cheese,count_of_crackers)
