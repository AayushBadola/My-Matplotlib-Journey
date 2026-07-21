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

val_x1 = np.array(range(0,100))
val_y1 = np.array(range(0,100))
# this graph should be a straight line 

val_x2 = np.array(range(0,100))
val_y2 = val_x2**2 # will automaticaly be numpy array since duhh faster 
# this one should be exponential increasing

figure, axes = plt.subplots(2,2)
# we basically are storing our "canvas" and our "plots" basically we are creaitng an np 2D array contianing 4 plots so we can access them like normal 2D arrays

############# PLOTTING SUBPLOT 1 (0,0)

axes[0,0].plot(val_x1,val_y1)
axes[0,0].set_xticks([])
axes[0,0].set_yticks([])

axes[0,1].plot(val_x2, val_y2)
axes[0,1].set_xticks([])
axes[0,1].set_yticks([])

##### IMPORTANT NOTICE: WHEN WE WANT TO CHANGE THE TICKS WHEN WORKING WITH MULTIPLE PLOTS WE CAN DO 
#PLOT1.set_xticks() and so on 
# here since our plot1 is basically a value in a numpy array so we access that value first by axes[indx1, indx2]

plt.show()

##################################### CUSTOMIZING THE SUBPLOTS ###########################

# customizing plots is as simple as customizing normal plots (refer to "plot_customization.py")

# to customize the subplots 
# first access those subplots in the 2-D numpy array 
# then just pass in the arguments say subplot_style 
# the arguments for customizing is same as normal plots 

subplot_style = dict(
                    marker="o",ms=5,mec="green", mfc="cyan", # marker specifications
                    ls = "dashed",lw=2,c= "black" # line specifications
                    )    

# now we can just put those specification while we plot those 


subplot_style2 = subplot_style | {"c" : "blue",
                                  "ls" : "dotted",
                                   "marker" : "x" }

figure2, axes2 = plt.subplots(2,2)

axes2[0,0].plot(val_x1, val_y1, **subplot_style)
axes2[0,1].plot(val_x2, val_y2, **subplot_style2)

plt.show()


####### IMPORTANT NOTICE WHEN WE DO axes[0,0].plot(val_x1, val_y1, **subplot_style) {the original one we are trying to modify}
# THAT WILL NOT BE MODIFIED IT WILL JUST CREATE A NEW LINE ON TOP OF THE ORIGINAL SO WE WONT BE ABLE TO SEE THE CHANGES 
# TO BYPASS THIS WE CREATE AN ENTIRELY NEW FIGURE AND AXES OBJECT BASICALLY A NEW "CANVAS" TO SHOW CUSTOMIZATION OF SUBPLOTS 

# we arent changing the original object we are creating a new "line" on top of the original not changing hte original 

####################### CONGRATS THE CONFUSING PART AND THIS MODULE IS COMPLETED ##############################

'''
⠀⠀⠀⠀⣄⠀⠀⢰⡆⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢀⢀⢠⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡄⠀⣾⡇⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⢒⣭⠉⠥⢌⡋⠐⠀⠠⠦⠍⢉⡃⢴⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⢸⡇⠀⢀⡆⠀⠀⠀
⠈⣦⠀⠀⢻⡇⠀⣿⡇⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⠈⠔⠀⣉⣥⣶⣶⣬⣭⣼⣿⣿⣶⣤⣄⠰⠶⠐⠀⢁⡀⠀⠀⠀⠀⠆⡀⢀⣀⡀⠀⣶⣒⡀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣿⡀⠀⢸⡇⠀⣸⡇⠀⠀⠀
⠀⠸⣇⠀⢸⣧⠀⣿⡇⠀⣿⠇⠀⠀⣀⣀⣀⣀⣀⣀⣚⣒⣒⣋⣛⣚⣡⡤⠁⠴⠠⠗⣸⣿⣿⣿⡟⣻⣿⣿⣿⣿⣿⡿⣿⣿⣿⣶⣿⣷⣄⠁⢀⢼⡴⢰⣾⣷⣿⣿⣿⣶⣶⣶⣿⣭⣿⣿⣿⣿⣤⣤⣙⣀⢹⣇⠀⢸⡇⠀⣿⠁⠂⣰⠃
⠀⠀⢻⣆⣸⣿⣶⣿⣷⣾⣿⠀⣴⡞⢋⣨⡍⢻⣿⣿⣿⣿⣿⣿⣿⣿⠟⣠⠃⣰⣿⣿⡟⣻⣿⣿⢡⣿⣿⣿⣿⣿⣿⡇⢻⣿⣿⣿⣿⣏⢻⣿⠰⠖⠀⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⡛⠻⣿⣿⢸⣿⣄⣼⣇⣸⣿⠘⢰⡏⣸
⠀⠀⠈⣿⣿⠿⢛⣋⣵⡿⢛⡀⠊⣰⡿⢃⣴⣿⣿⣿⣿⣿⣿⣿⡿⠏⣰⡟⣰⣿⣿⡟⣰⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⡇⡌⠿⢿⣇⢻⡿⠂⢿⣷⠖⠀⠰⠀⠀⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣷⡌⠻⢸⣿⣛⠻⢿⣿⣿⣦⡙⢰⣿
⠀⠀⡆⣾⣷⣾⣿⣿⢋⣴⣿⣿⣿⡟⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿⠁⡁⡌⢻⢃⡿⡀⣿⡇⣿⣿⣿⣿⣿⣿⣿⡇⣿⣄⢠⡤⠀⠀⠺⠘⣿⠀⠀⠀⠀⠀⡄⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⣿⣦⣶⣭⠻⣿⣶⣬⣝⣿⡇⣿⣿
⢸⢹⡇⠸⣿⣿⣿⣯⣾⣿⣿⣿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢰⡏⣤⣃⣴⣾⢸⣷⣶⣿⢰⣿⣿⣿⣿⡇⣿⣿⢇⣿⣿⣆⠀⣴⢸⣶⡆⣿⠀⠈⠀⠀⠈⠁⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⣿⣿⣿⣷⠸⣿⣿⣿⣿⢀⣿⣿
⢸⢻⣿⡀⢻⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡄⣿⠃⣿⣿⣿⣿⢸⡇⣿⣿⢸⣿⣿⣿⣿⡇⣿⣿⢠⣴⣶⣮⣤⠹⡌⣿⡇⣿⡏⠀⡆⠀⠐⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡘⢿⣿⣿⣷⣿⣿⣿⡏⣸⣿⣿
⢸⢿⣿⣷⠠⢉⣩⣽⣿⡷⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⠁⣿⠀⣿⣿⡏⣿⢸⡇⣿⣿⢸⢿⣿⣿⣿⠇⣿⡇⣜⣩⠽⠻⠿⣷⡀⣿⡇⣿⡧⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠙⣉⣽⣟⠻⠏⣰⣿⣿⣿
⣾⡿⠟⣋⠀⣿⣿⣿⡿⠇⣀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠀⣿⡇⣿⣿⡇⣿⢸⣷⢸⣿⡘⡘⣿⣿⣿⢰⣿⢱⢃⡀⠀⠀⠀⠈⠃⢹⠇⣿⠇⠆⡆⢰⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣀⠀⢿⣿⣿⣿⠀⠿⣿⣿⣿
⣩⣴⠾⠛⣀⣭⡥⠶⠖⠋⠁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠀⢻⡇⢸⡟⣿⢸⡌⣿⡈⣿⡇⠇⣿⣿⣿⢸⠇⣾⣿⡇⢀⠀⠀⡷⢰⠸⢰⡿⠈⠀⡇⠘⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠈⠙⠒⠦⣭⡛⠸⣶⣬⡙⠿
⣭⠴⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠰⠘⣇⠈⢧⠹⡄⠳⣘⣃⣹⣃⣀⣹⣿⣟⣘⣸⣿⣿⣿⣦⣭⣼⣷⡏⠂⠁⠠⠘⢰⠃⢀⡄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉⠓⠦⣍⡛⢷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠹⡐⡈⢆⠱⠸⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣷⢄⣀⠔⡀⡜⠀⢈⡇⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⡀⠈⢦⣀⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣬⠁⠌⠀⣰⠀⣼⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠍⢣⡈⢿⣿⣿⣿⣿⣝⣛⣿⣿⣻⣿⣿⣿⣿⡿⢋⡼⠃⠘⣠⣾⣿⠀⢿⣷⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣦⣀⡑⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠛⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣴⣷⣦⡙⢿⣿⣿⣿⣿⣿⡆⢀⡀⣌⡉⠛⠿⠛⣋⣥⡆⡨⠐⢶⣿⣿⣿⣿⣿⣿⠟⣋⣥⣦⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣄⢛⠛⢿⣿⣿⡆⢆⢡⣬⡙⠗⣒⠻⢋⣥⡅⠔⠁⣾⣿⣿⡿⠿⠟⣡⣾⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿
⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠿⠿⣿⣿⣿⣿⣿⠟⡉⢡⡌⣿⣿⣿⣿⡇⣾⣿⡆⢨⣄⠲⢮⡀⢿⣿⣆⣿⣠⣿⠟⠁⣢⣶⣶⡌⡅⣶⣿⡆⣿⣿⣿⠿⡏⣼⢙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿
⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢡⡞⠡⢤⣆⢈⠍⣷⣬⡁⠙⢿⡇⡜⣿⣿⡦⠉⠀⡁⠀⠀⠀⢀⠈⠛⢿⣿⣿⢃⢣⣿⠟⠐⣋⣿⠀⢄⣤⣙⣀⠳⣌⣛⡛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿
⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⢿⣿⣿⣿⡶⢸⡆⢼⣿⣿⡟⠀⣿⣷⡐⡘⢿⡀⠰⠟⠀⠀⣆⠀⠈⠻⠆⢀⡿⢃⢂⣾⣿⠀⢺⣿⣿⣷⠸⣿⠩⣥⣶⣾⣦⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿
⢸⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣯⣅⠰⣿⣇⠘⣿⣿⡇⠀⢨⠍⣿⣬⡊⠑⠄⢠⠆⢠⣿⠀⢣⡀⠀⡊⢔⣡⣟⢛⡁⠀⢸⣿⣿⠃⣾⣿⣷⠌⣩⣿⡙⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⢸⣿⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢛⠿⠝⢋⡬⠵⣷⠌⡃⠁⠀⣿⣷⣌⣛⡛⢶⣬⣤⠀⣀⣀⡀⢐⣢⣥⡖⠿⠿⢋⣼⣧⠀⢈⣬⠠⣄⣛⣛⠰⠾⠿⠟⢛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
⢸⣿⢿⣿⣿⣿⣷⣤⣶⣶⣴⣦⣤⣄⣀⣀⣀⣀⣊⡙⢷⡌⢭⣭⣤⡈⢰⣿⠀⣸⣿⣿⣿⣿⣿⣦⣭⡅⠀⣈⣋⡀⠨⣙⣩⣴⣾⣿⣿⣿⣿⡄⠸⣿⠆⠛⣛⣛⣛⠂⣴⡾⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣾⣿⣿⣿⣿⣿
⠠⠉⠉⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣶⣤⣼⣿⣿⣿⡄⠛⠀⣡⣬⣉⣴⣌⢛⣛⠻⣷⣴⠻⡟⣡⣶⡿⠿⠻⢛⣩⡙⣋⣍⠃⠀⡋⠐⣀⣿⣿⣇⣚⣡⣴⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠑⠂⠈⠹⢻⣿⣿⣿⣿⣿⣿⣻⣿⣾⣿⣻⣿⣿⣿⣿⣿⣿⣷⠀⣴⣿⣿⣿⣿⣿⣿⣿⣧⣉⣍⠃⠁⣫⣭⣰⣿⣿⣿⣿⣿⣿⣿⣿⡀⡔⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠈⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⡿⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠃⠈⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⡿⣿⠿⠿⠿⠟⠛⠋⠉⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠉⠉⠛⠛⠋⠛⢻⡿⢻⠻⠆⠰⣨⠻⡏⣿⣿⣿⣿⣿⣿⣿⣀⡄⢦⣴⣿⣿⣿⣿⣿⣿⣿⢻⣿⠟⡀⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠉⠙⠋⠙⠂⠐⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡁⠀⠀⢀⣀⣉⣁⡂⠨⢉⣩⣭⣁⢶⠆⢈⣠⣤⣁⠉⡙⣛⢛⣛⣋⡉⣈⢡⠞⢀⡈⠉⣉⣉⣉⣉⠉⢉⣉⣉⣉⠙⠙⠉⠉⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⢹⡀⠀⢸⣇⣀⣀⠗⠀⢺⣄⣂⠙⠀⢰⡏⠀⠀ ⣇⠀⣻     ⣿⠈⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠤⠬⣧⠀⢸⡏⠉⠉⣷⠀⣀⠈⠉⢹⡆⠸⣇   ⡏⠀⢿⠀⠀⠀⠀⣿⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠘⠂⠘⠛⠛⠛⠁⠀⠈⠛⠒⠋⠀⠀⠈⠓⠚⠋⠀⠀⠘⠛⠛⠛⠀⠈⠓⠒⠋⠀⠀⠀⠘⠃⠀⠀⠘⠛⠛⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣶⣦⣄⠀⠀⠀⢰⣶⣶⡆⠀⠀⣶⣶⣶⣄⠀⠀⠀⠀⠀⣶⣶⡆⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀⣶⣶⣶⣶⡄⠀⠀⠀⠀⢰⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⡿⠉⠀⠀⠈⠙⢿⣿⣧⠀⠀⢸⣿⣿⡇⠀⠀⣿⣿⣿⣿⣆⠀⠀⠀⠀⣿⣿⠀⠀⠀⢸⣿⣿⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⣿⣿⡟⣿⣷⠀⠀⠀⠀⣾⣿⢻⣿⣿⠀⠀⠀⠀⠀⠀⣼⣿⠏⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⠀⠘⠛⠛⠃⠀⢸⣿⣿⡇⠀⠀⣿⣿⡇⠹⣿⣦⠀⠀⠀⣿⣿⡇⠀⠀⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣿⣿⡇⢹⣿⡆⠀⠀⢰⣿⡏⢸⣿⣿⠀⠀⠀⠀⠀⣸⣿⡟⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸⣿⣿⡇⠀ ⣿⣿⣧ ⠹⣿⣧⡀ ⣿⣿⡇⠀  ⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀ ⠀⠀⣿⣿⡇⠀⣿⣿⠀⠀⣾⣿⠁⢸⣿⣿⠀⠀⠀⠀⢠⣿⣿⠃⠀⠈⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣷⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⢸⣿⣿⡇⠀⠀⣿⣿⡟⠀⠀⠘⣿⣷⡀⣿⣿⡇  ⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀     ⣿⣿⡇⠀⠸⣿⡇⢠⣿⡏⠀⢸⣿⣿⠀⠀⠀⠀⣾⣿⣯⣤⣤⣤⣼⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⢿⣿⣧⣀⠀⠀⠀⣀⣼⣿⡟⠀⠀⢸⣿⣿⡇⠀⠀⢿⣿⣿⠀⠀⠀⠘⢿⣿⣿⣿⡇  ⢸⣿⣿⠀⠀           ⣿⣿⡇⠀⠀⢿⣷⣾⣿⠁⠀⢸⣿⣿⠀⠀⠀⣸⣿⡿⠻⠿⠿⠿⠿⢿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⢸⣿⣿⠇⠀ ⢼⣿⡿⠀⠀⠀⠀⠈⢿⣿⣿⡇⠃ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠘⣿⣿⡏⠀⠀⢸⣿⣿⠀⠀⢰⣿⣿⠇⠀⠀⠀⠀⠀⠘⣿⣿⣇⠀⠀⠀⠀⠀


'''