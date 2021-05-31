# averagespeed.py
# a.peer
# March 5, 2020
# To calculate the average speed of a car

#title
print("-----------------------------------")
print("Average Speed Of Vehicle Calculator")
print("-----------------------------------")

#user input
startingTime = float( input("Enter starting time hour - in 24 hour format: "))
endingTime = float( input("Enter ending time hour - in 24 hour format: "))
startingTime2 = float( input("Enter starting time minute: "))
endingTime2 = float( input("Enter ending time minute: "))


#calculating time
timeTaken=endingTime-startingTime
timeTaken2=endingTime2-startingTime2
time=(timeTaken+(timeTaken2/60))*60

#display time and ask for km
print("Minutes taken:",time)
km= float( input("Enter km travelled: "))

#calculating speed
speed=km/(time/60)
print("The speed of your vehicle is:",speed,"km/h")


#ending statement
print("\n")
print("Thank you for using our software :)")
    

      

