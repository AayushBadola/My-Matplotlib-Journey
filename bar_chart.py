import numpy as np 
import matplotlib.pyplot as plt

# allows to compare quantities based on the height of bar (usually the width of bar for other quantities remain same)

# a basic exmample will be given below :

'''
top military in the world 

USA    
##     Russia  
##      ##     China
##      ##      ##     India
##      ##      ##      ##
##      ##      ##      ##
'''
# from this graph we can see how each country performs Military wise 
# thats why a bar graph is very informative when we see it at first since it provides us a clear perspective 

# to use bar graph we will use data based on food pyramid that is 
# Grains (Bread, Cereal, Rice, Pasta) > Vegetables & Fruits > Dairy (Milk, Yogurt, Cheese) & Proteins (Meat, Poultry, Fish, Beans, Eggs, Nuts) > Fats, Oils & Sweet

# we have to produce the same result in form of bar graph 
# but to distinguish how much importance that category has lets label them on a scale of 1->5 

categories = np.array(["Dairy", "Meat", "Fats", "Grains", "Vegetable", "oils"])

# category wise we do this 5 importance 
# 1-> lowest importance 

importance = np.array([4, 4, 1, 5, 3, 1 ])
# dairy meat has same importance 
# oils , fats has same importance thus same number 

################################## USING A BAR GRAPH #################################
# to use a bar graph we have to use the function "plt.bar()"
# in plt.bar() we have to provide the value of X axis -> categories and Y axis-> importance level 

plt.bar(categories,importance)

##### AS THE GRAPH SHOWS THE TOP VALUE AS 5 SINCE IT SHTE MAX WE ADDED IN Y-AXIS 
####  WE CAN ALSO PROVIDE OUR CUSTOM MAX Y AND MIN Y VALUE SO THE "bar" DOESNT REACH THE TOP OF "GRAPH"

plt.ylim(0,7) # sets the Y axis bottom and top limit \
# we can so provide specific arguments like "plt.ylim(top=7)" OR "plt.ylim(bottom=0)"

plt.show()

################################# PROVIDING TITLE TO THE GRAPH #########################
# same concept same execution just do plt.title()

plt.bar(categories,importance)
plt.ylim(0,7) # sets the Y axis bottom and top limit
plt.title("Food category importance")

# SAME CONCEPT WITH LABELS 

label_style = dict(
    fontsize = 11,
    fontweight = 90,
    fontfamily = "Arial",
    color = "Black"
)

plt.xlabel("Food Category", **label_style) # same concept of storing our desired style and then unpacking it 
plt.ylabel("Category Importance", **label_style)

plt.show()


#################################### CUSTOMIZING BAR GRAPH ###################################
# we can custoize how the bar chart is visibile 
#  some of the customizeable options are:
'''
width (how thicc the actual bar is ) 
colo of graph (color)
color perimeter of bar (edgecolor)
width of line (how thicc the perimeter of bar is ) -> linewidth
contol the style of the "Perimeter" of bar (linestyle) 
hatch -> the actual patter of bar (inside perimeter)
alpha ocntrols the transpirancy of bar compared to background -> 0 <= alpha <= 1

'''

bar_style = dict(
    width = 0.5, # by default its 0.8
    color = "Blue",
    edgecolor = "Yellow", # same coor will also be applied to hatch or the extra patterns we are making inside the graph
    linewidth = 2,
    linestyle = "dotted",
    hatch = "||",
    alpha = 0.5
)

plt.bar(categories,importance, **bar_style)

plt.xlabel("Categories", **label_style)
plt.ylabel("Importance of Category", **label_style)

plt.show()