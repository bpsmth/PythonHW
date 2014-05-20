'''HW4.py is written to fulfill the requirements for the fourth HW in CS1
    Fall 2013 semester. Written by Braden Smith. 
    It imports the functions file and then calls the functions using their outputs
    and inputs to display desired chart.
    '''
import HW4funcs
#The code above imports the functions written for the HW.

chosenleague=HW4funcs.leagueinput()
#The code above calls the league input function and assigns the result to chosenleague for use later

chosenyear=HW4funcs.yearinput()
#The code above calls the year input function and assigns the result to chosenyear for use later

data=HW4funcs.calculation(chosenleague,chosenyear)
#The code above calls the calculation function and uses the stored results for inputs, it stores the resulting data for use later.

HW4funcs.plot(data,chosenleague,chosenyear)
#The code above calls the plot function and uses the earlier stored results as inputs, this function finally displays desired chart.
