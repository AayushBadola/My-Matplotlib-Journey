import numpy as np
import matplotlib.pyplot as plt 

######################### Labeling the Graph #######################
# labeling the graph means providing a "title" to the graph 
# the title we provide should be discriptive enough to know at the first look what it shows 

students = np.array([15,25,30,20]) # student strenth per year
years =np.array([2023,2024,2025,2026]) # yearwise data

plt.title("Student strength vs Years") # since our grpah is basically student number and years comparision
plt.plot(years,students)
plt.show()

####################### Labelling the X-Axis and Y-Axis ###################
# in normaly form of plt.plot(x,y) we only get the data plotted on the x-y axis BUT we cant make out what the axis represent
# any time we see the graph we just see in X-AXIS as 2023, 2023.5,2024, 2024.5, . . . .
# similarly for Y-Axis we get data as 15, 20, 25, 30, 35 . . . .
# we dont know what that data means in the graph 

# HERE WE START LABELLING THE AXIS
# to label x-Axis -> plt.xlabel("Label Name", fontsize=N, fontweight="bold or normal or light or heavy", family="Arial", color="Blue")
# to label y-axis -> plt.ylabel("Label Name", fontsize=N, fontweight="bold or italics or something", family="Arial", color="Blue")

plt.plot(years,students) # we know we are plotting the "years" as X-Axis and "students" as Y-Axis beacsue of variable names
# but for matplot lib its just data so to label that data we use the labelling 

plt.xlabel("Years", fontsize=11, fontweight="heavy", fontfamily="Arial", color="black")
plt.ylabel("Students", fontsize=11, fontweight="normal", fontfamily="Arial", color="black")

plt.show()

######## NOTICE : AGAIN WE ARE JUST DOING THE SAME SPECIFICATIONS SO WE CAN STORE IT IN A DICTIONARY AND UNPACK IT WHILE PUTTING IN THE SPECIFICATION 

graph_labels = dict(
    fontsize=11, # the actual size of the x-y label
    fontweight=80, # fontweight basically tells us how much bold it should be (can be numeric or string)
    fontfamily="Arial", # the style of font which should be used 
    color="black" # color of the text for x-y label 
)

plt.plot(years,students)
plt.title("Student vs Years using A single format for X-Y axis")
plt.xlabel("Years", **graph_labels)
plt.ylabel("students",**graph_labels)

plt.show()

############################# CHANING THE TICKS / MARKS FOR DATA IN X -Y AXIS #####################
# the ticks are basically "Markers" or permanent "Markers"(refer to plot_customization.py) for the data points 
# in reality by default these markers are there for every data point visible on graph 
# say there is a data point called 2023, 2024, 2025, 2026
# but in graph its like this 2023, 2023.5 , 2024, 2024.5 . . . .
# so by deafult the ticks / markers would be applied to 2023, 2023.5 , 2024 . . . since they are visible on the X-Y axis line 



# to make it such that the ticks are ONLY visible on the data points which WE PROVIDED 
## chaning the x-ticks so they only apply to the data we provided 

plt.xticks(years) # ticks only on the years data WE PROVIDED 
plt.yticks(students) # ticks only on teh student data

plt.tick_params(axis="x",color="purple") # chaning / customizing our "ticks" for X-Axis

'''

TICK PARAMETERS AND ITS USAGE

axis         -> "x", "y", "both"
                Selects which axis to customize.

which        -> "major", "minor", "both"
                Selects which ticks to modify.

direction    -> "in", "out", "inout"
                Controls the direction of tick marks.

length       -> Length of the tick marks.

width        -> Thickness of the tick marks.

colors       -> Changes BOTH the tick marks and their labels.

labelsize    -> Font size of the tick labels.

labelcolor   -> Color of only the tick labels.

pad          -> Distance between the tick mark and its label.

bottom       -> True / False
                Show or hide bottom tick marks.

top          -> True / False
                Show or hide top tick marks.

left         -> True / False
                Show or hide left tick marks.

right        -> True / False
                Show or hide right tick marks.

labelbottom  -> True / False
                Show or hide bottom tick labels.

labeltop     -> True / False
                Show or hide top tick labels.

labelleft    -> True / False
                Show or hide left tick labels.

labelright   -> True / False
                Show or hide right tick labels.

Example:

plt.tick_params(
    axis="both",
    which="major",
    direction="out",
    length=6,
    width=2,
    colors="black",
    labelsize=12,
    labelcolor="red",
    pad=5
)

'''
