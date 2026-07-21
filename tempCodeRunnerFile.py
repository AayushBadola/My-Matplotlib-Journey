# a subplot is a plot which is inside a "figure"
# a figure can contain multiple "plots"
# a figure is like a canvas and plots are like diagram 
# we can create multiple "mountains", "houses" in our drawing sheet 
# similarly we can create multiple plots inside a figure


import numpy as np 
import matplotlib.pyplot as plt 

# when we call the "plt.subplot()" function it generally accepts 2 values (or more arguments for customizations)
# the general arguments for "subplot" is say Ax and Ay 
# if we do subplot(2,2) we get 4 graphs say 2 rows and 2 cols so 4 graphs (not the actu defination but easy for understanding)

# if we do subplot(1,2) then we get 1 row and 2 cols so 2 graphs 

###################################### CREATING A SUBPLOT #########################################
# use the function "plt.subplots()" REMEMBER ITS "subplots" NOT "subplot"

# Before we start plotting a subplot a Axes is considered 1 graph 
# the graphs lets say for subplot(2,2) is given below 

'''
    📊      📊
    (0,0)   (0,1)

    📊      📊
    (1,0)   (1,1)

basically similar to how we do indexing on a 2-D multi dimensional array and how we access it 

'''

# the result of a subplot or what it returns is a tuple( REMEMBER THEY ARE IMMUTABLE )
# the tuple contains a figure object and a 2-D numpy array of axes object 

val_x1 = [1,2,3,4,5]
val_y1 = [1,2,3,4,5]
# this graph should be a straight line 

val_x2 = [1,2,3,4,5]
val_y2 = [1,4,9,16,25] 
# this one should be 

figure, axes = plt.subplots(2,2)
# we basically are storing our "canvas" and our "plots" basically we are creaitng an np 2D array contianing 4 plots so we can access them like normal 2D arrays

############# PLOTTING SUBPLOT 1 (0,0)

axes[0,0].plot(val_x1,val_y1)
plt.xticks(range(0,7,1)) # ticks increase by 1 
plt.yticks(range(0,7,1)) # we will make sure the matplotlib wont automaticallly adjust ticks

axes[1,0].plot(val_x2, val_y2)

plt.xticks(range(0,7,1))
plt.yticks(range(0,27,1)) # making sure the matplot does NOT make Y-ticks to 1,5,10,15 but stay 0,1,2,3,4,. . . . .

plt.show()


