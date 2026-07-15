import matplotlib.pyplot as plt # provides user friendly interface for plotting 

# we know for plotting we need X and Y axis mostly (for a 2D plot)
# so for any plot we can do plot(x-axis ,y-axis)

# for say X data we create a data 
x = [2023,2024,2025,2026] # years
y = [15,25,30,20] # class size per year

# MAKE SURE NUMBER OF X VALUES = NUMBER OF Y VALUES

#################### PLOTTING THE DATA #######################
plt.plot(x,y) # plots the data of x and y 

################### SHOWING THE DATA ########################
# internally the data is plotted but it has yet to be shown 
# WE CAN NOT DO print(plt.plot(x,y)) as plt.plot is an object of our 2d line 

#TO show the data we do 
plt.show()

################### plotting data for a single variable ###############
# if we do plt.plot(x) OR plt.plot(y) the difference would b matplot will automatically select y = [0,1,2,3] for plot(x)
# and for plot(y) it will select x = [0,1,2,3]

plt.plot(x) # x becomes the "Y-axis", Assumes the "X-Axis" values as (0,1,2,3) since number of vals in x is 4 
plt.show() 

plt.plot(y) # y becomes duhh "Y-axis", and matplot lib assumes x axis values as [0,1,2,3] (for 4 values 0,1,2,3) (for N values 1,2,3,4,5 . . . N)
plt.show()  

########################## NOTICE ###########################
# NUMPY ARRAYS ARE FAST SO WHEN CREATING A LIST OF DATA JUST CONVERT IT TO A NUMPY ARRAY LIKE np.array([2023,2024,2025,2026]) etc

