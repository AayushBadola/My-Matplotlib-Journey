import matplotlib.pyplot as plt 
import numpy as np

years = np.array([2023,2024,2025,2026]) # numpy array is fast but matplot lib can take normal python list 
students = np.array([15,25,30,20])

######################## creating a marker #######################
## A marker visually represents the actual data points supplied to plt.plot(). 
# In layman terms : the data we are given that is 2023-15
#                                                 2024-25
#                                                 2025-30
#                                                 2026-20
# there exist a point in 2-D that is (2023,15) this data is specific value we were given hence a marker would represent it 
# (2024-25) -> MARKER REPRESENT IT AS WELL 
# (2025-30) -> AGAIN MARKER WILL REPRESENT IT 
# and so on 
# (2023.5,20) -> WONT REPRESENT BY MARKER SINCE IT WAS NEVER IN OUR DATA IT MERELY WAS PART OF THE LINE CONNECTING 2 MARKERS 

# to create a marker we simply add another argument in plot(x,y,marker="*")
# basically whatever is inside marker that would represent the marker could ONLY BE FROM A SELECT TYPE 

'''
marker="o"    Circle
marker="*"    Star
marker="+"    Plus
marker="x"    Cross
marker="D"    Diamond
marker="s"    Square
marker="^"    Triangle Up
marker="v"    Triangle Down
marker="."    Point
marker="p"    Pentagon
marker="h"    Hexagon
''' 


plt.plot(years,students,marker="o") # now each of that point will be represented by a circle 
plt.show()

# to change markersize we just add another argument called markersize
plt.plot(years,students,marker="o", markersize= 20) # for a bigger size marker
plt.show()

# tbh as we abbriviate everything(genz) , WE COULD say or use "ms" instead of "markersize"

########################### CHANGING MARKER COLOR ###########################
# to change the color of marker just add another argument which is markerfacecolor 
plt.plot(years,students,marker="o",ms=20,mfc="cyan") # we are degrading the actual full names into shortforms (NEVER DO IT FOR "marker")
plt.show()

################## CHANGING THE MARKER EDGE / PERIMETER COLOR #################
# again to change it just add an argument called "markeredgecolor" OR "mec"

#################################### CHANGING THE STYLE OF LINES ##################################
# just solid lines are by default but we can change the line type to be "dashed"(--------) or "dashdot"(--.--.--.--.--.) or "none"(removes the lines)
# to do that we add an argument that is "linestyle" OR "ls"
plt.plot(years,students, marker="o",ls="dashed")
plt.show()

################################## CHANING THE WIDTH OR THICKNESS OF LINE ##########################
# again to do that we just need to add another argument that is "linewidth" OR "lw"
# it basically increases or decreases the witdh of line IF WE PUT "lw = 0" IT CREATES THE SAME GRAPH AS ls="none"
# graphically same but conceptually diff as width = 0 means so small we can not see 
# ls="none" means no line "exist"
plt.plot(years,students,marker="o", lw=3)
plt.show()

################################ CHANGING THE COLOR OF LINE ###################################
# again for that we jsut add another argument that is "color" or "c"

plt.plot(years,students,marker="o",c="green") # if we dont specify the color of marker it will be same as line 
plt.show()

############################### SHOWING 2 VALUE GRAPHS IN 1 GRAPH ####################3
# the heading is confusing but bear with me 
# so every time we do plt.show() it shows a grpah individually but after close it it then openes another and then another 
# so we could how 2 graphs in a single "Image"
# say we need to compare 2 different values say years2 = [2027,2028,2029,2030] 

# to do that the graph 1 -> students,year
# and graph2 -> students,year2 
# DOESNT MATTER IF DATA IS COMMON OR NOT WE CAN HAVE SOME DIFFERENT DATA AS WELL 

# ANOTHER THING IS JUST PLOT 2 OR MORE GRAPHS AND THEN DONT INDIVIDUALLY plt.show()
# after plotting all the graphs then do plt.show()
years2 = np.array([2027,2028,2029,2030])

plt.plot(
        years,students, # data
        marker="o",ms=3,mec="green", mfc="cyan",# marker specifications
        ls = "dashed",lw=2,c= "black" # line specifications
        )

plt.plot(
        years2,students, # data
        marker="*",ms=3,mec="purple", mfc="yellow",# marker specifications
        ls = "solid",lw=0.7,c= "orange" # line specifications
        )

plt.show()




############################## CREATING COMMON STYLE FOR ALL PLOTS ###################

# writing the style of each plot is already teadious and when 2 plots contain the same specifications of marker and line 
# then we can just store those "specifications" in a dictionary and then unpack it using "**" for each plot


style = dict(marker="o",ms=5,mec="green", mfc="cyan", # marker specifications
            ls = "dashed",lw=2,c= "black" # line specifications
            )           


plt.plot(years,students,**style) # **style unpacks the dictionary and whatever the specification there is individually writes 
                                 # those specifications in the plt.plot() arguments

plt.plot(years2,students,**style) # using the same style for the new plot 

plt.show() # both will have the same style

################################ OVERRIDING OUR STYLE ###########################
# we can override our style by writing the color or width or any specification which is written by deafult in our style 
new_style = style | {"mfc" :"purple"}

# we basically over wrote the original style and megerd it with the new markerfacecolor = "Purple"
# basically merge 2 dict , style and new dict {"mfc" :"purple"} and so this new dict replaces the value of mfc in our original style
plt.plot(years,students,**new_style) # originally it was supposed to specification + markerfacecolor="cyan"
                                              # we changed cyan to "purple"
plt.show()