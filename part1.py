'''
The part1 module is written to have
a number values function, a random list function,
a sorted median function, a heap median function,
a timing function, and a plotting function. 
See their individual docstrings for further info.
These functions were written by Braden Smith, Fall 2013.
'''

def numvals(k,l,m):
    '''The numvals function is a function that, when
        called takes 3 values used to create a range, and returns a list 
        created from that range. 
    '''
    vals=list(range(k,l,m)) #This line produces a list based on range given.
    return vals #This returns list.

def ranlist(a):
    '''The ranlist function is a function that, when
        called takes a value (list) and creates a list of lists full of random
        numbers using the values in the list passed in. It then returns that 
        list. 
    '''
    import random
    M=[] #Code initializes empy list for accumulation.
    for i in a: #This loop iterates over values passed into function. 
        M.append( [ random.random() for i in range(0,i,1) ] ) 
        # Code produces a list of randoms that is as long as value passed into function.
        
    return M #This returns a list of lists of random numbers
    
            
def togmed(c):
    '''The togmed function is a function that, when
        called takes 1 value (List of lists) then iterates through that and 
        calculates the time it takes to calculate the median using the sorted 
        method.
        It then finds the average time it took to calculate the median and 
        returns that.
    '''
    import time
    times=[] #This code initializes a list for accumulation.
    for i in range(1,6,1): #For loop which iterates over range of 5 for the 5 experiments.
        start=time.clock() #This code "starts" the stopwatch.
        median=sorted(c) [len(c)//2] 
        #This code, which was given to us, calculates median of list that was passed into function.
    
        end=time.clock() #This code "stops" the stopwatch. 
        elapsed=(end-start) #This code calculates elapsed time for each experiment.
        times.append(elapsed)#This code stores the elapsed time for every experiment.
        
    results=(sum(times)/len(times))  #This code calculates average time for all of the experiments.
    
    return results  #This returns the average time.

def heap(nums):
    '''The heap function is a function that, when
        called takes 1 value (List of lists) then iterates through that and 
        calculates the time it takes to calculate the median using the heap 
        method.
        It then finds the average time it took to calculate the median and 
        returns that.
    '''
    import time
    times=[]#This code initializes a list for accumulation.
    for i in range(1,6,1):#For loop which iterates over range of 5 for the 5 experiments.
        start=time.clock()#This code "starts" the stopwatch.
        import heapq
        heapq.heapify(nums)
        for n in range(len(nums)//2):
            heapq.heappop(nums)
        median=heapq.heappop(nums)
        #This code, which was given to us, calculates median of list that was passed into function.
        end=time.clock()  #This code "stops" the stopwatch.
        elapsed=end-start #This code calculates elapsed time for each experiment.
        times.append(elapsed)#This code stores the elapsed time for every experiment.
    
    average=(sum(times)/len(times))#This code calculates average time for all of the experiments.
    return average #This code returns the average time.

def gettimess(lists):
    '''The gettimess function is a function that, when
        called takes 1 value (List of lists) then iterates over all of the lists
        and passes the list within the list into the median calculation functions        
        It then collects all of the times for the different methods and returns
        that list.
    '''
    heaps=[] #This code initializes a list for accumulation.
    togs=[]#This code initializes a list for accumulation.
    for i in lists: #This loop iterates over the passed through lists of lists.
        heaps.append(heap(i)) #This appends the results of the "heap" function to the list.
        togs.append(togmed(i))#This appends the results of the "togmed" function to the list.
    return [heaps,togs] #This returns those results in a list of two lists.
    
def plot(xvals,yvals):
    '''The plot function is a function that, when
        called takes 2 values (yvals is a list of two lists) then uses matplot
        lib to plot those results.
    '''
    import matplotlib.pyplot as plt
    y=yvals[1] #This seperates the list of two lists created above.
    z=yvals[0] #This seperates the list of two lists created above.
    
    
    figure=plt.figure() #This initalizes the figure.
    subfig=figure.add_subplot(111) 
    subfig.set_title("Sort Median (Blue) vs Heap Median (Red)") #This adds the title for chart.
    subfig.set_xlabel("List Length") #This adds XLabel.
    subfig.set_ylabel("Computing Time (In Seconds)")#This adds YLabel.
    
    subfig.plot(xvals,y,linewidth=4.0,color="blue")#This plots the Sort Median Line.
    subfig.plot(xvals,z,linewidth=4.0,color="red")#This plots the Heap Median line.
    
    
    
    plt.show()#This shows the plot.
   
#The above code is the entire function library for part1.py.

#The below code is the functional part of part1 which utilizes the above library.
  
numvalues=numvals(2**10,2**19,2**15) #This creates a list of values which the lists of randoms will be based on.
randl=ranlist(numvalues)#This creates the random lists using the values created and stored in numvals.
results=gettimess(randl)#This uses the random lists stored in randl to get the computing time and stores in "results".
plot(numvalues,results)#This plots the data using the values created earlier and the results from above.