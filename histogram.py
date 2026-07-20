# A histogram is a visual representaion of the distribution of quantitative data 
# they group values into intervals 
# say for interval 1-4 that goes into one bin 
# say for interval 4-9  that goes into another bin 

# they are great for statistics and other datas 
import numpy as np
import matplotlib.pyplot as plt 

# we can use numpy to create random values which will form a bell curve (NORMAL CURVE)
'''
y
^
|
|                            *
|                         *     *
|                      *           *
|                   *                 *
|                *                       *
|             *                           *
|          *                               *
|___*_*_*__*___________________________________*__*_*_____> x
'''

scores = np.random.normal(loc=70, scale=10, size=100) # here loc mean "Location of center" so it means basically 70 is mean 

# here these arguments mean 
'''
loc = mean 
scale = standard deviation so +- 10 so middle is 70 then sides are 60 or 80 or 40 or 90 and so on 
size = total number of data 
'''

####################################### CREATING HISTOGRAM ###################################
# we can create a histogram through the useage of "plt.hist()"

plt.hist(scores)
plt.show()

############################## LIMITING THE MAX NAD MIN VALUES IN HISTOGRAM #################################

# since we are using random we know that there can be scores that score more than 100 and less than 0 
# so we set an upper bound to it 

# we have 2 options 
# option 1 make it so that the lmit is set and the values never exceed 100 or less than 0

# option 2 make it so that even if they exceed the limits we cna just say if values less than 0 are there make them 0
#          make it so that values exceeding 100 are there just make them 100 

# for option 1 we will use the xlim and ylim funciton they jsut dont show the vales that are not in range
# for option 2 we will have "clip()" it just changes the data itself 
# the random function will still generate those "bad" values and put them in te graph after that the clip funciton will do the changes 

# option 1 is better as we wont have to do additional manipulation and the data we dont want will just be hidden 
plt.hist(scores)

plt.xlim(0,100) # 0 is lower bound and 100 is upper bound 

plt.show()

###################################### CREATING BINS #################################
# we will create "bins" (basically rectangular graps or bar charts but not bar charts 🤔)
# these "bins" will tell us how many people scored those scores or how many numebr of vlaues are there

# lets say for value 70 there are 80 values which scored 70 {mind my broken english 🥀}

# the bin containing values which scored 70 would be highest as in normal form the mean value (in this case 70) have the highest number

# for creating a specific ammount of bins we just have to provide the argument "bins = Number we wamt"

plt.hist(scores, bins=20)
plt.xlim(0,100)
plt.show()


########## NOTICE 
# we should never specify the ammount of bins (we can if we want to compare 2 datas)
# we should just let matplotlib decide but again DONT TRUST , 
# WE HAVE SPECIFIC RULES FOR SPECIFIC AMMOUNT AND SPREAD OF DATA 
# to make the bins follow those rules we use 
# bins = "the rule we want"

###### TAKE THESE RULES TO GRAVE ######

'''
HISTOGRAM BIN SELECTION RULES

RULE        | WHEN TO USE                         | HOW IT CHOOSES BINS
---------------------------------------------------------------------------------------
auto        | General-purpose (Recommended)       | Automatically chooses the best rule
            |                                     | (usually Sturges or FD).

sturges     | Small to medium datasets            | bins = ceil(log2(n) + 1)
            |                                     | (Depends only on number of observations)

scott       | Approximately normal data           | Uses standard deviation to calculate
            |                                     | an optimal bin width.

fd          | General data with possible outliers | Uses Interquartile Range (IQR) to
(Freedman-  | (Most Robust)                       | calculate an optimal bin width.
Diaconis)   |                                     |
'''

######################### CUSTOMIZING HISTOGRAMS ##################
# to customize histograms we have specific arguments we can use and provide values to those "arguments"

'''
MOST COMMONLY USED HISTOGRAM ARGUMENTS

ARGUMENT      | What it Does
------------------------------------------------------------
bins          | Number or method of creating bins.

range         | Lower and upper limit of the histogram.

color         | Fill color of the bars.

edgecolor     | Border color of the bars.

linewidth     | Thickness of the bar borders.

alpha         | Transparency of the bars.
               | (0 = Invisible, 1 = Fully Opaque)

density       | Shows probability density instead of
               | frequency counts.

label         | Label used when creating legends.

histtype      | Style of histogram.
               | ("bar", "barstacked", "step", "stepfilled")
'''

histogram_style = dict(
    bins = "scott", # our data is based on normal distribution 
    range = (0,100),
    color = "Blue",
    edgecolor = "Black",
    density = True, # now it will show probability density
    histtype = "bar" # the default value 
)

# barstacked -> stacks the histogram on top of each other 
# step -> just creates the outline of the histogram no fill inside 
# step filled -> creates the outline and then fills that outline 

plt.hist(scores, **histogram_style) # notice we didint need to use plt.xlim() since that job is done by range 

plt.show()



