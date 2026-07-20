# a pie chart is a circular chart which divides the "Categories" or data into slices to show perecntages 
# its good for visualization for "Specific categories" inside the data
import matplotlib.pyplot as plt
import numpy as np

# for representing the graph  we will use college structue of seprating students that is 
# sophomores , freshmen , senior , junior

student_category = np.array(["freshmen", "sophomores", "juniors", "seniors"]) # student category

student_distribution = np.array([300, 250, 275, 255])  # their distribution

# if we only pass the "values" that is how students are distributed then the piw will be created based on those values but wont contain the labels we passed 

################################ CREATING A PIE CHART ####################################
# to create a pie chart call the plt.pie(values, labels="the labels we want")
# here the data of how students are distributed is student_distribution 
# the labels of the distribuition that we want to show in pie chart is student_category

plt.pie(student_distribution, labels=student_category)
plt.show()

## with this a pie chart will be created but only contain colors and labels those colors represent 

############################# ADDING PERCENTAGE TO PIE CHART CATEGORIES #####################################

# with pie charts we can also have them the percentages those colors represent and their labels as well 

# to have the pie charts contain the percentages we use the autopct("")
# it will automatically provide the percentage of each category 

plt.pie(student_distribution,labels=student_category, autopct="%1.1f") # 1 decimal values 
plt.show()

###################################### CUSTOMIZING PIE CHARTS ##########################################

# the default colors for categories is Red , green blue and others 
# to make the pie chart contain the colors of our choosing we can just pass a list contianing our color to an argument called "colors" 

color = np.array(["Red", "Orange", "Purple", "Cyan"])
# these color correspond to the categories we passed 
# student_category = np.array(["freshmen", "sophomores", "juniors", "seniors"])
# so freshmen = red
# sophmores = orange 
# junios = purple 
# cyan = seniors 

plt.pie(student_distribution,labels=student_category, colors=color )
plt.show()


####################### TAKING A PIECE OUT OF THE PIE #####################

# FOR ANY PIE CHART WE HAVE 
'''
    ####
    ####
    ####
    ####

'''
# now we want to take out a part of the pie to "highlight it "

'''
    ####
    ####
    ####

    #### <-- Hightlighted part which is right now NOT PART of the pie 

'''

# to get that "Effect" we use something called "explode" argument 
# think of it as that part exploding and now getting seprated from the main pie 

plt.pie(student_distribution,
        labels=student_category, 
        explode=[0,0,0,0.1] # we highlighted the senior because why not 
        )

plt.show()

###################### ADDING SHADOWS TO PIE CHART ########################
# to add shadow we just make the argument "shadow" True 

plt.pie(student_distribution,
        labels=student_category, 
        explode=[0,0,0,0.1],
        shadow=True
        )
plt.show()