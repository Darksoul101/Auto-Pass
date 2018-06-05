#                                                                                                                                                                                          AutoPass OpenSource Password Maker

#                                                                                                                        Lock Your Password File

#                                                                                                                                                                                                                                                                                   Auto Create or user type password were created

#                                           |////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                           |     FOLLOW US ON :--                                                                                                                                                                                                                                                 /
#                                           |             Twitter itz_yazz_singh                                                                                                                                                                                                                                /
#                                           |             Instagram itz_yash_singh                                                                                                                                                                                                                YAsh Creation
#                                           |            website www.yashhelp.cf                                                                                                                                                                                                                    /
#                                           |            blog www.yashdailyblogs.blogspot.com                                                                                                                                                                                    /
#                                           |                                                                                                                                                                                                                                                                              /
#                                           |                                                                                                                                                                                                                                                                           /
#                                           |/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# YAsh Creation

import string

import csv

import os

import random

# creating a string varfor saving passwd from array
ri ="pass: "

# asking user to unlock his pass file
starting = input("Do You Want To Unlock Your File(Y/N): ")

#if yes then we use cacls to use this
if starting == "y" or starting == "Y":
    
    os.system("cacls AutoPass.csv /E /P everyone:f") # Full Role To File

    exit()

#Asking The User For Using Which Type Of List
defaultOrMAde = input("Do You Like To Use Our Created Password ? Y/N: ")

#How Long He Want
length_of_pass = int(input("How Long You Want:  "))

# if Use His Own List Then
if defaultOrMAde == "N" or defaultOrMAde == "n":

    print("Example: "+string.ascii_lowercase) #Example For Input

    User_need = input("Content Which will use for password creating: ") #Taking Input

    r = random.choices(User_need,k=length_of_pass) # Making It Random


# if use our list then
else:

    s = string.printable # Getting All Printable Chr OF ascii

    r = random.choices(s,k=length_of_pass) # random

#print("Here Is Your Password:",end="") # here is passwd

# Printing
for i in range (length_of_pass):

    ri += r[i]  #Saving In A Var.

    #print(r[i])# printing the passwd
print(ri)

# Asking User To Save The File Or Not
Saving = input(""""

Do You Want To Save It In A File(Y/N):""")

#if Yes Then
if Saving == 'Y' or Saving == 'y':
    
    Ask_For = input("For What Your Using It (Don't Worry We Don't SAve It In Our Database ): ") # Asking For What

    file = open("AutoPass.csv",'a') # Creating A File 

    writer = csv.writer(file) # Wrinting in file

    file.write( Ask_For) # write in row

    # pressing enter
    file.write("""
""")
     
    file.write(ri+"""

""") # passwd using var in top

    file.close() # closing the file

#Exit The program
else:
    exit()

# Asking User to lock that file
encr = input("Do You Want To Lock That File:(Y/N) ")

# if yes then
if encr == "y" or encr == "Y":

    os.system("cacls AutoPass.csv /E /P everyone:n") #using cacls to lock the file

    print("""Thanks Created By Yash
          Follow Me On Twitter- itz_yazz_singh
          instagram-itz_yash_singh""")

else:

    print("""Thanks Created By Yash
          Follow Me On Twitter- itz_yazz_singh
          instagram-itz_yash_singh""")

# Thanks For Reading Created By YAsh
#Visit: www.yashhelp.cf
