people = 90
cars = 40
trucks = 15

if cars > people and people > trucks:
    print("We should take the car")
elif people > cars or truck > 10:
    print("We should not take the cars")
else:
    print("We are not able to decide")

#if trucks > cars:
    #print("There are too many trucks")
#elif cars > trucks:
    #print("why we need cars,lets take trucks")
#else:
    #print("can't decide")

if people > trucks and trucks > 20:
    print("Alright we go with trucks")
else:
    print("lets stay home")
