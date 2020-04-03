#Josh Stiller Chameleon Coding Challenge 3
#This one was a bit of a brainbender. This takes the sets of the programs and takes the characters that the two have in common
#and prints them for the user. 
def common_character(a, b): #this gives our matching characters comparisons for each other
    a_set = set(a) #denoting set a
    b_set = set(b) #denoting set b
    if (a_set & b_set):  #this is saying if there are common characters to then
        print(a_set & b_set) #print the said characters. 
    else: #or itgoes into this 'else' loop which give the message below
        print("There are no common elements")  
           
a = [4, 3, 4, 29, 99, 13, 19, 23, 34] #Chameleon Provided Arrays. 
b = [3, 45, 57, 0, 94, 23, 24, 34] 
common_character(a, b) #common characters. 