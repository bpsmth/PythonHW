'''
The part2 module is written to have
a uniform random function, a normal random function,
a exponential random function, a total median function,
a specific median function, an experiment function 
and a plotting function. 
See their individual docstrings for further info.
This assignment was written by Braden Smith, Fall 2013.
'''
import random
def unirandom(ran):
    '''The unirandom function is a function that, when
        called takes a value used to create random list with the same length
        and returns a list created from that range. This uses the Uniform random
        method.
    '''
    M = [ random.random() for i in range(ran) ] 
    #This creates a random list using the uniform code snippet given to class.
    return M #This returns the random list.
def normran(ran):
    '''The normran function is a function that, when
        called takes a value used to create random list with the same length
        and returns a list created from that range. This uses the normal random
        method.
    '''
    M = [ random.gauss(mu=10.0,sigma=3.0) for i in range(ran) ] 
    M = [ round(val*10.0)/10.0 for val in M ]
    #The above creates a normalized random list, using the code given to class.
    return M #This code returns the list.
    
def expran(ran):
    '''The expran function is a function that, when
        called takes a value used to create random list with the same length
        and returns a list created from that range. This uses the Exponential 
        random method.
    '''
    M = [ random.expovariate(1/10.0) for i in range(ran) ]
    M = [ round(val*10.0)/10.0 for val in M ]
    #The above code creates an exponential list using the code given in class.
    return M
    
def medians(lis, vals):
    '''The medians function is a function that, when
        called takes two values, one list and one value it then randomly selects
        items from the list. The number of items selected is derived from the 
        value passed into the function. It then uses the values to calculate the
        sample median.
    '''
    medians=[] #This code initializes a list to be used in accumulation.
    for i in range(vals): #This for loop iterates over the range of values given for number of experiments.
        medians.append(random.choice(lis)) #This grabs a random value from the entire list and stores it.
    final=sorted(medians) [len(medians)//2] #This code snippet uses the values given above to calculate the median.
    
    return final #This returns the median calculated above.
    
    
def med(lis):
    '''The med function is a function that, when
        called takes a value, one list and then calculate a population median.
    '''
    final=sorted(lis) [len(lis)//2] #This calculates the median using the entire list.
    return final #This returns the above calculation.
    
def experiment(results,val):
    '''The experiment function is a function that, when
        called takes two values, one list and one value it then calls the other 
        function and passes it values, it then uses that result to score the 
        sample median.
    '''
    score=[]
    for i in range(20):
        final=medians(results,val) #This calls the medians function and passes it the list and the number of experiments needed.
        score.append(abs(final - med(results))/float(med(results)))#This calculates the score for the median compared to the real median.
    
    res=(sum(score)/len(score))
    return res #This code returns that score.

def plotte(val1,val2,val3):
    '''The plotte function is a function that, when
        called takes 3 values (three lists) then uses matplot
        lib to plot those results on a line graph.
    '''
    import matplotlib.pyplot as plt
    xvals=range(4,128,4) #This creates all  of the X Values needed for the graph.
    figure=plt.figure() 
    subfig=figure.add_subplot(111)
    subfig.set_title("Uniform (Blue) vs Normal (Red) vs Exponential (Green) Median Estimators") #This adds the title for the figure.
    subfig.set_xlabel("Sample Size for Median Estimate") #This adds the X Label.
    subfig.set_ylabel("Score (Smaller is Better)") #This adds the Y label.
    
    subfig.plot(xvals,val1,linewidth=4.0,color="blue") #This plots the uniform line.
    subfig.plot(xvals,val2,linewidth=4.0,color="red")#This plots the Normal line.
    subfig.plot(xvals,val3,linewidth=4.0,color="green")#This plots the Exponential line.
    
    plt.show() #This shows the plot.


#The above code is the function library for the code below.

#The below code is the functional component of part2, and utilizes the above library.

unran=[] #This initializes a list for accumulation below.
norran=[] #This initializes a list for accumulation below.
exran=[] #This initializes a list for accumulation below.

for i in range(4,128,4): #This for loop iterates over the range of experiment values.
        resultsuni=unirandom(16384) #This generates a random list using the uniform method for each experiment number.
        unran.append(experiment(resultsuni,i)) #This uses the list and experiment value to call the above functions and store the values.
        
        resultsnorm=normran(16384)  #This generates a random list using the normal method for each experiment number.
        norran.append(experiment(resultsnorm,i)) #This uses the list and experiment value to call the above functions and store the values.
    
        resultsexp=expran(16384) #This generates a random list using the Exponential method for each experiment number.
        exran.append(experiment(resultsexp,i))#This uses the list and experiment value to call the above functions and store the values.
        
plotte(unran,norran,exran) #This pass
#ran will usually be 16384
    