import numpy as np
import matplotlib.pyplot as plt

# grid lines are basically refrence lines added to our graph making the data easier to read

############################# CREATING GRIDLINES FOR GRAPH ##########################
x_data = np.array([1,2,3,4,5])
y_data = np.array([5,10,15,20,25])

plt.plot(x_data,y_data)

plt.grid() # creates grid lines for both x and y axis by deafult 
# CAN BE CHANGED TO ONLY SHOW Y-AXIS LINES OR X-AXIS LINES BY DOING (axis='x') OR (axis="y") 

plt.show()

############################ customizing gridlines ##############################

# for customizing grid lines we can customize them based on 
'''
Element         | FUNCTION
-----------------------------------
axis            |   plt.grid(axis="y) OR plt.grid(axis="x) OR plt.grid(axis="both")
width of line   |   plt.grid(linewidth = 3)
color           |   plt.grid(color="blue)
line style      |   plt.grid(linestyle = "dashed") OR "dotted OR dashdot
'''

plt.plot(x_data,y_data)

# storing grid style specifications in dictionary so onwe can "unpack"(by using **) later 
grid_style = dict(
    axis="both",
    linewidth= 3,
    color = "purple",
    linestyle="dashed"
)

plt.grid(**grid_style)

plt.show()