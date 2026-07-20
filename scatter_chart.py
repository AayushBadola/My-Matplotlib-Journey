# scatter chart shows us the relation ships of 2 variables or categories 
# it helps us verify correlation of it 
# exmaple study hrs vs test scores 
# we know more study will MOST LIKELY give us better/higher test scores 

import matplotlib.pyplot as plt 
import numpy as np 

study_hours = np.array([0,1,1,2,3,4,5,6,7,7,8])

grades = np.array([55, 60, 65,62, 68, 70, 75, 78, 82, 85, 87]) # grades corresponding to the hours student put to his studies 

############################ CREATING A SCATTER PLOT ##########################
# to create a scatter plot just call the scatter function and provide x and y values respectively 

plt.scatter(study_hours,grades)
plt.show()

######################### ADDING LABELS TO SCATTER PLOT ######################
# Adding labels is a standar feature of matplot lib it does not follow a specific process for a specific graph 
# for any graph we can add a x , y label by using "plt.xlabel" AND "plt.ylabel"

plt.scatter(study_hours,grades)
plt.xlabel("Hours studied")
plt.ylabel("Grades Student Got")

plt.show()

######################### CUSTOMIZING SCATTER PLOTS ##############################

# we can customize the scatter plots by these certain arguments 

'''
SCATTER PLOT CUSTOMIZATION CHEAT SHEET

ARGUMENT         | What it Does
--------------------------------------------------------------------
x                | X-axis values.

y                | Y-axis values.

s                | Size of the markers.

c                | Color of the markers.

marker           | Shape of the markers.

alpha            | Transparency of the markers.
                 | (0 = Invisible, 1 = Fully Opaque)

edgecolors       | Border color of the markers.

linewidths       | Thickness of the marker borders.

label            | Label used when creating legends.

cmap             | Colormap used when 'c' contains numerical values.

vmin             | Minimum value mapped by the colormap.

vmax             | Maximum value mapped by the colormap.

zorder           | Drawing priority.
                 | Higher value = Drawn on top.

plotnonfinite    | Plots NaN and infinite values instead of
                 | ignoring them.
'''

# again for the sake of easier useage we will create a dict containing the styles and then unpacking them 

scatter_style = dict(
    s = 40, # marker size
    c = "Black", # color of marker
    alpha = 0.5,
    edgecolor = "Green",
    zorder = 5,
    plotnonfinite = False # by default its false but to show the customization we will explicitally write it 
)

# for more use zorder is basically say we have scatter plot and a normal line chart then if zorder for scatter is higher then that plot 
# will appear on TOP of the line chart 

plt.scatter(study_hours, grades, **scatter_style)
plt.show()

################################# COMPARING 2 SCATTER PLOTS ##############################

# to compare 2 scatter plots we just have to plot both of them as one 
# we have done this in our "plot_customization.py"


study_hours_grp1 = np.array([0,1,1,2,3,4,5,6,7,7,8])
grades_grp1 = np.array([55, 60, 65,62, 68, 70, 75, 78, 82, 85, 87])


study_hours_grp2 = np.array([0,1,2,5,5,6,6,6,7,8,8])
grades_grp2 = np.array([60, 62, 66, 69, 72, 72, 73, 82, 80, 89, 90])

scatter_style_grp1 = scatter_style | {"label" : "Group 1 "} # we will be having black color for group 1

scatter_style_grp2 = scatter_style | {"c" : "Red", "alpha" : 0.5, "zorder" : 5, "label" : "Group 2"} # we will have red color for gorup 2 and same priority as it 

plt.scatter(study_hours_grp1, grades_grp1, **scatter_style_grp1)

plt.scatter(study_hours_grp2, grades_grp2, **scatter_style_grp2)

plt.legend() # COMPULSORY TO SHOW THE LABEL FOR EACH DIFFERENT CHART

plt.xlabel("Study Hours")
plt.ylabel("Grades Scored")

plt.show()







