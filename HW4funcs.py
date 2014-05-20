'''
The HW4funcs module is written to have
a leagueinput function, a year input function,
a computational function, and a plotting function. 
See their individual docstrings for further info.
These functions were written by Braden Smith, Fall 2013.
'''


def leagueinput():
    '''The leagueinput function is a function that, when
        called it prompts for user input, then validates that input
        and returns it once validated in upper case to match salaries.csv.
        If it is invalid it continues to prompt for correct user input.
    '''

    #Code below prompts user for league to obtain salaries from and stores it.
    league = raw_input("Enter Desired League (NL or AL): ")
    
    #Code below initializes the error condition to 0.
    error=0
    
    #If statement validates user input for league, if valid error condition is set to 1.
    if league.upper() == "AL" or league.upper() == "NL":
        
        error=1
        
    #While loop that will run until the input is valid and error condition is 1.    
    while error==0:
        
	#Since league was not valide it prompts user for league info again.
        league=raw_input("Please enter a valid league (AL or NL): ")
        
        #The below if statement checks validity of input, if valid sets error condition to 1.
        if league.upper() == "AL" or league.upper() == "NL":
            
            error=1

    #below code returns league in upper format to match salaries.csv when input is vald.                    
    return league.upper()
    
def yearinput():
    '''The yearinput function is a function that prompts for user 
        input, then validates that input against salaries.csv and 
        returns it once validated.If it is invalid it continues
        to prompt for correct user input.
    '''
    #Code below imports a module to handle csv files.
    import csv
    
    #Code below initializes the error condition to 0.
    error=0
    
    #The code below prompts user for year input and stores it.
    year=raw_input("Please enter a desired year:")
    
    #While loop that executes until error condition is no longer 0. 
    while error ==0:
        #Code below opens salaries.csv, then reads it into a dictionary which is stored.
        salaryfile= csv.DictReader(open(r"C:\Users\Interviews\Desktop\CS1-HW4\Salaries.csv"))
        
        #For loop below iterates through every record in the stored dictionary.
        for line in salaryfile:
            #The below if statement compares the user input to the record from salaries.csv
            if line.get("yearID")==year:
               error=1
                #If user's year is found the error condition is set to 1.
        
        #If the year was not validated this if executes and prompts for input again.
        if error == 0:
            year=raw_input("Please enter a valid year (1985-2012):")
            #Prompts user with a different message with more information. 
            
    #Code below returns validated year.        
    return year
    
def calculation(league,year):
    '''The calculation function accepts the year and league input validated
        in the preceeding functions. It then locates those inputs in salaries.csv
        after locating it accumulates all relevant records. Then it proceeds to 
        calculate averages and totals. It returns an accumulated dictionary using 
        teamID as key and percent of total salary as value
        returns - {"teamID":Percent of league salary}
    '''
    import csv
    #The above code imports a module to handle CSV files.
    
    #The below code opens salaries.csv and then reads it into a dictionary which it stores.
    salaryfile= csv.DictReader(open(r"C:\Users\Interviews\Desktop\CS1-HW4\Salaries.csv"))
    #The below code initializes an empty list to store records in.
    years=[]
    #The below for loop iterates through every record in the dictionary.
    for line in salaryfile:
        #The below if condition checks to see if the record matches what the user is looking for.
        if line.get("yearID")==year and line.get("lgID")==league:
            #If the record matches it appends the record to the list created earlier.    
            years.append(line)
    #Code below initializes an empty dictionary to store data in.
    averages={}
    #The Code below initializes a total to 0 for use later.
    lgtotal=0
    #The below for loop iterates over all the records which matched user inputs.
    for record in years:
        #If the teamID from the record is not in the dictionary, this if condition trips.
        if record.get("teamID") not in averages:
            #Code below adds the teamID to the dictionary if it was not there.
            averages[record.get("teamID")]=0
        #After the teamID is added, it then adds the records salary to the value already in the dictionary.
        averages[record.get("teamID")]=averages[record.get("teamID")]+int(record.get("salary"))
        #The code below adds the salary to the league total as well.
        lgtotal=lgtotal+int(record.get("salary"))

    #The code below initializes a dictionary for storing the percentages.
    percentage={}
    #This for loop iterates through all the team's total salaries.
    for team in averages:
        #The code below calculates the teams percentage of that years league salaries.
        percent=averages.get(team)/float(lgtotal)
        #The code below takes the calculate number and formats it for percentage.
        percentage[team]=int(percent*100)
        
    #The code below returns the data dictionary created in this function.
    return percentage
    
def plot(selectdata,league,year):
    '''The plot function is a function that accepts data created using the calculation
    function of the module. It imports plotting modules, and uses the inputs to format 
    the chart. When finished it displays the chart created.
    '''
    import matplotlib.pyplot as plot
    #The above code imports the plotting modules.
    piechart=plot.figure()
    #The code above instantiates a figure.
    subplot=piechart.add_subplot(111)
    #The above code instantiates a subplot for the figure.
    subplot.set_title("Average Salary chart for "+ league+" in "+year)
    #The above code creates a figure title and uses user input for the dynamic information.
    values=list(selectdata.values())
    #The above code uses the values from the data dictionary used as an input for the figure values.
    labels=list(selectdata.keys())
    #The above code uses the keys from the data dictionary used as an input for the figure keys.
    plot.pie(values,labels=labels)
    #The above code creates a pie chart using the labels and values from above.
    plot.show()
    #The above code displays the figure created above.