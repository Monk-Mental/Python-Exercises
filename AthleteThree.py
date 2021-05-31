#athletethree.py
#Arya Peer
#April 6 2020
#tells a team of two wrestlers their classification (whether they are heavy weight, light weight or medium weight)


#introduction
print("--------------------------------------------------------------------------------------------------")
print("This program tells a team of two wrestlers their weight classification")
print("--------------------------------------------------------------------------------------------------")

#Ask for and get wrestler weights in KG
wrestlerWeightInKg1=float(input("\nWrestler 1, Input your weight in kilograms: ") )
wrestlerWeightInKg2=float(input("Wrestler 2, Input your weight in kilograms: ") )

#ensure the weight is a positive integer for wrestler1 (code will not run otherwise)
if wrestlerWeightInKg1 > 0:


#ensure the weight is a positive number for wrestler 2 (code will not run otherwise)
    if wrestlerWeightInKg2 > 0:


#Weight Division if statement for wrestler 1 
        if wrestlerWeightInKg1 > 80:
            print ("\nWrestler 1 you are in Heavy Weight Division")
        elif wrestlerWeightInKg1 <60:
            print("\nWrestler 1 you are in the Light Weight Division")
        else:
            print("\nWrestler 1 you are in the Medium Weight Division")
        #end if

#Weight Division if statement for wrestler 2
        if wrestlerWeightInKg2 > 80:
            print ("\nWrestler 2 you are in Heavy Weight Division")
        elif wrestlerWeightInKg2 < 60:
            print("\nWrestler 2 you are in the Light Weight Division")
        else:
            print("\nWrestler 2 you are in the Medium Weight Division")
        #end if

#(if they inputted negative values it will prompt them to put in their actual weight and run the program again)
if wrestlerWeightInKg1 < 0:
    print("\nPlease run the program again and PLEASE use your actual weight Wrestler 1!!!")
#end if
    
if wrestlerWeightInKg2 < 0:
    print("\nPlease run the program again and PLEASE use your actual weight Wrestler 2!!!")
#end if

#end
print("-----------------------------------------------------------")   
print("THANK YOU, for using my program !!!")
print("-----------------------------------------------------------") 
