"""[ITC106 - Programming Principles]

Assignment A4 by Gavin Eke
"""

#Variables
#Program Metadata
__author__ = "Gavin Eke"
__version__ = "$Revision: 1.0 $"

# Car Names
car_name = ["Toyota Kluger","Nisson Patrol","Ford Territory"]
number_of_cars = len(car_name) # Calculate Number of Cars based on list length

# Configure Allowed Years Input
year_earliest_allowed = 1900
year_oldest_allowed = 2100

# Global Statements
welcome_message = "Aussie Best Car Software v1.0\n"
invalid_data = "Please enter all data as numbers only, E.g. Type 30000 if you want $30,000"
invalid_percent = "Please enter all data as decimal numbers only, E.g. Type 50.0 if you want %50"
invalid_menuresponse = "\nInvalid Response, Please enter A to ADD, S to SEARCH or Q to QUIT"
invalid_yearresponse = "\nInvalid Response, Year must be between %s and %s"
invalid_response = "\nInvalid Response, Please enter Y for YES or N for NO"

# Global Response List
response_add = ["A","ADD"]
response_search = ["S","SEARCH"]
response_quit = ["Q","QUIT"]
response_positive = ["Y","YES"]
response_negative = ["N","NO"]

# Database Information
database = {} # Initialize dictionary
database_filename = "sales.txt" # Choose the database txt file path

# Open the database txt file and store the contents as database
try: # Attempt to open the datebase file
    database_file = open(database_filename, 'r') # Open database txt file in read mode
    for line in database_file: # Store the contents of the database file in a dictionary
        database_line = line.strip('\n').split(', ')
        database[database_line[0]] = database_line[1:]
    database_file.close() # Close the database txt file
except: # If the database can not be opened possible due to the file not existing print error and exit
    print("\nError: Failed to open database txt file. \nPlease make sure the file", database_filename, "exists and is in the same path as the program file. \nIf the program continues to produce this error please contact your System Administrator.")
    raise SystemExit(1) # Exit with code 1 failure

# Display Welcome Message - Shown at the start of program launch
print(welcome_message)

#Functions
# Main Function
def main(): # Intentionally left blank
    print("\n") # Print new line to make it more pleasant on the eye

# Main Menu Function - Performs the tasks choosen by the user in the main menu
def mainMenu(main_menu_selection):
    if main_menu_selection in response_add: # If response is A do the following
        if yearrun in database: # If year is in database inform user
            print("\nDuplicate entry is not permitted")
            
            # Ask the user if they would like to search the datebase instead
            get_response = input("Would you like to use the data in the database instead (Y/N): ").upper()
            while not responseValidation(get_response): # Call responseValidation function to check that input is a valid response if not keep looping asking for valid input response
                print(invalid_response)
                get_response = input("Would you like to use the data in the database instead (Y/N): ").upper()
            
            # Perform actions as per users response
            if get_response in response_positive:
                print("\n") # Print new line to make it more pleasant on the eye
                mainMenu("S") # Call mainMenu function
            elif get_response in response_negative:
                main() # Call main function
            else:
                print("\nError: responseValidation function failed to catch invalid response. \nThis Error should have never occured please contact your System Administrator.")
                raise SystemExit(1) # Exit with code 1 failure
        
        else:# If year isn't in database do the following
            # Assignment A1
            car_sellprice = getSellingPrice() # Call getSellingPrice function and store the return as car_sellprice
            car_carssold = getCarsSold() # Call getCarsSold function and store the return as car_carssold
            car_totalincome = calculateCarsSold(car_sellprice,car_carssold) # Call calculateCarsSold function and store the return as car_totalincome
            displayTotalIncome(car_totalincome) # Call displayTotalIncome
            
            # Assignment A2
            awardbonus = abcAwardBonus(car_totalincome[3]) # Call abcAwardBonus function and store the return as awardbonus
            car_contribution = calculateCarContribution(car_totalincome,awardbonus) # Call calculateCarContribution function and store the return as car_contribution
            displayAwardBonus(awardbonus,car_contribution) # Call displayAwardBonus
            
            # Assignment A3
            car_additionalbonusrate = getAdditionalBonusRate() # Call getAdditionalBonusRate function and store the return as car_additionalbonusrate
            car_additionalbonus = calculateAdditionalBonus(car_contribution,car_additionalbonusrate) # Call calculateAdditionalBonus function and store the return as car_additionalbonus
            displayAditionalBonus(car_additionalbonus) # Call displayAditionalBonus
            totalbonus = calculateTotalBonus(awardbonus,car_additionalbonus) # Call calculateTotalBonus function and store the return as totalbonus
            displayTotalBonus(totalbonus)# Call displayTotalBonus
            
            # Create Database Strings
            db = car_sellprice + car_carssold + car_additionalbonusrate
            dbstr = yearrun + ", " + db[0] + ", " + db[1] + ", " + db[2] + ", " + db[3] + ", " + db[4] + ", " + db[5] + ", " + db[6] + ", " + db[7] + ", " + db[8] + "\n"
            
            # Update Database and Dictionary
            database_file = open(database_filename, 'a') # Open database txt file in read mode
            database_file.write(dbstr) # Append the Database stirng to the database txt file
            database_file.close() # Close the database txt file
            database[yearrun] = db # Add the data to the dictionary
    
    elif main_menu_selection in response_search: # If response is S do the following
        if yearrun in database: # If year is in database do the following
            # Get car_sellprice, car_carssold and car_additionalbonusrate for the year entered and run the calculations
            db = database[yearrun]
            car_sellprice = db[0:3]
            car_carssold = db[3:6]
            car_additionalbonusrate = db[6:9]
            
            # Assignment A1
            car_totalincome = calculateCarsSold(car_sellprice,car_carssold) # Call calculateCarsSold function and store the return as car_totalincome
            displayTotalIncome(car_totalincome) # Call displayTotalIncome
            
            # Assignment A2
            awardbonus = abcAwardBonus(car_totalincome[3]) # Call abcAwardBonus function and store the return as awardbonus
            car_contribution = calculateCarContribution(car_totalincome,awardbonus) # Call calculateCarContribution function and store the return as car_contribution
            displayAwardBonus(awardbonus,car_contribution) # Call displayAwardBonus
            
            # Assignment A3
            car_additionalbonus = calculateAdditionalBonus(car_contribution,car_additionalbonusrate) # Call calculateAdditionalBonus function and store the return as car_additionalbonus
            displayAditionalBonus(car_additionalbonus) # Call displayAditionalBonus
            totalbonus = calculateTotalBonus(awardbonus,car_additionalbonus) # Call calculateTotalBonus function and store the return as totalbonus
            displayTotalBonus(totalbonus)# Call displayTotalBonus
        else: # If year isn't in database inform user
            print("\n", yearrun, " is not in the databse.")
            
            # Ask the user if they would like to add the data to the datebase instead
            get_response = input("Would you like to add the data in the database instead (Y/N): ").upper()
            while not responseValidation(get_response): # Call responseValidation function to check that input is a valid response if not keep looping asking for valid input response
                print(invalid_response)
                get_response = input("Would you like to add the data in the database instead (Y/N): ").upper()
            
            # Perform actions as per users response
            if get_response in response_positive:
                print("\n") # Print new line to make it more pleasant on the eye
                mainMenu("A") # Call mainMenu function
            elif get_response in response_negative:
                main() # Call main function
            else:
                print("\nError: responseValidation function failed to catch invalid response. \nThis Error should have never occured please contact your System Administrator.")
                raise SystemExit(1) # Exit with code 1 failure
        
    else: # This should not be possible due to responseValidation but if it happens print error and quit
        print("\nError: menuValidation function failed to catch invalid response. \nThis Error should have never occured please contact your System Administrator.")
        raise SystemExit(1) # Exit with code 1 failure

# Data Validation Function - Checks if input is an integer and >= 0
def dataValidation(data):
    try: # Attempts to turn the data into an integer
        int(data)
    except: # If it cannot turn the data into an integer return False
        return False
    if (int(data) >= 0): # Makes sure value is >= 0 and returns True if it does
        return True
    else: # If it is an integer but not >= 0 return False
        return False

# Percent Validation Function - Checks if input is a float between 0 and 100
def percentValidation(data):
    try: # Attempts to turn the data into an float
        float(data)
    except: # If it cannot turn the data into a float return False
        return False
    if (float(data) >= 0) and (float(data) <= 100): # Makes sure value is between 0 and 100 and returns True if it does
        return True
    else: # If it is an float but not between 0 and 100 return False
        return False

# Menu Validation Function - Checks if input is a valid response for the menu selction
def menuValidation(data):
    if data in response_add or data in response_search or data in response_quit: # Returns True if data is in the response list
        return True
    else: # If value is not in list return False
        return False

# Year Validation Function - Checks if input is an integer between the years in the configurable allowed years
def yearValidation(data):
    try: # Attempts to turn the data into an integer
        int(data)
    except: # If it cannot turn the data into a integer return False
        return False
    if (int(data) >= int(year_earliest_allowed)) and (int(data) <= int(year_oldest_allowed)): # Returns True if data meets the conditions
        return True
    else: # If value does not meet the conditions return False
        return False

# Response Validation Function - Checks if input is a valid response for positive or negative questions
def responseValidation(data):
    if data in response_positive or data in response_negative: # Returns True if data is in the response list
        return True
    else: # If value is not in list return False
        return False

# Get Selling Price Function - Gets the price of each car
def getSellingPrice():
    sellingprice = 'Please enter the selling price of the %s: '
    invalidsellingprice = '\nInvalid Data, %s\nPlease enter the selling price of the %s: '
    
    car_sellprice = [None] * number_of_cars # Create a list the length of the amount of cars
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_sellprice[iteration_count] = input(sellingprice % car_name[iteration_count])
        while not dataValidation(car_sellprice[iteration_count]): # Call dataValidation function to check that input is an integer and is > 0
            car_sellprice[iteration_count] = input(invalidsellingprice % (invalid_data, car_name[iteration_count])) # Inform user of invalid data and ask for input again
    
    print("\n") # Print new line to make it more pleasant on the eye
    
    return car_sellprice

# Get Cars Sold Function - Gets the amount of cars sold
def getCarsSold():
    carssold = 'How many %s have been sold in %s?: '
    invalidcarssold = '\nInvalid Data, %s\nHow many %s have been sold in %s?: '
    
    car_carssold = [None] * number_of_cars # Create a list the length of the amount of cars
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_carssold[iteration_count] = input(carssold % (car_name[iteration_count], yearrun))
        while not dataValidation(car_carssold[iteration_count]): # Call dataValidation function to check that input is an integer and is > 0
            car_carssold[iteration_count] = input(invalidcarssold % (invalid_data, car_name[iteration_count], yearrun)) # Inform user of invalid data and ask for input again
    
    print("\n") # Print new line to make it more pleasant on the eye
    
    return car_carssold

# Calculate Cars Sold Function - Calculates the total income of each car and the grand total
def calculateCarsSold(car_sellprice,car_carssold):
    car_totalincome = [None] * (number_of_cars + 1) # Create a list the length of the amount of cars + 1
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_totalincome[iteration_count] = int(car_sellprice[iteration_count]) * int(car_carssold[iteration_count])
    car_totalincome[3] = car_totalincome[0] + car_totalincome[1] + car_totalincome[2] # Calculate the total income of all 3 cars and assign it to the 4th item on the list
    
    return car_totalincome

# Display Total Income Function - Displays the grand total and the total income of each car
def displayTotalIncome(abc_totalincome):
    totalincome = 'The total income of all cars for %s is $%s'
    print(totalincome % (yearrun, '{:0,d}'.format(abc_totalincome[3])))
    print("\n") # Print new line to make it more pleasant on the eye
    
    carincome = 'The %s had a total income of $%s in %s'
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        print(carincome % (car_name[iteration_count], '{:0,d}'.format(abc_totalincome[iteration_count]), yearrun))
    print("\n") # Print new line to make it more pleasant on the eye

# ABC Award Bonus Function - Determines the total award that should be paid
def abcAwardBonus(abc_totalincome):
    if abc_totalincome >= 0 and abc_totalincome <= 500000: # Calculate award bonus for abc_totalincome between 0 - 500000
        awardbonus = abc_totalincome * 0.001
        return awardbonus
    elif abc_totalincome >= 500001 and abc_totalincome <= 1000000: # Calculate award bonus for abc_totalincome between 500001 - 1000000
        awardbonus = (abc_totalincome - 500000) * 0.002 + 500
        return awardbonus
    elif abc_totalincome >= 1000001 and abc_totalincome <= 5000000: # Calculate award bonus for abc_totalincome between 1000001 - 5000000
        awardbonus = (abc_totalincome - 1000000) * 0.003 + 1500
        return awardbonus
    elif abc_totalincome >= 5000001 and abc_totalincome <= 10000000: # Calculate award bonus for abc_totalincome between 5000001 - 10000000
        awardbonus = (abc_totalincome - 5000000) * 0.004 + 13500
        return awardbonus
    elif abc_totalincome > 10000000: # Calculate award bonus for abc_totalincome over 10000000
        awardbonus = (abc_totalincome - 10000000) * 0.005 + 33500
        return awardbonus
    else: # This should not be possible due to dataValidation but if it happens print error and quit
        print("\nError: dataValidation function failed to catch invalid response. \nThis Error should have never occured please contact your System Administrator.")
        raise SystemExit(1) # Exit with code 1 failure

# Calculate Car Contribution Function - Calculates the total award bonus and award bonus contributed by each car
def calculateCarContribution(abc_totalincome,abc_awardbonus):
    car_contribution = [None] * number_of_cars # Create a list the length of the amount of cars
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_contribution[iteration_count] = abc_awardbonus * (abc_totalincome[iteration_count] / abc_totalincome[3]) # Calculate the % the car contributed towards the total award bonus
    
    return car_contribution

# Display Award Bonus - Display the total award bonus and award bonus each car contributed
def displayAwardBonus(abc_awardbonus,abc_contribution):
    # Display the total award bonus
    allcars_awardbonus = 'The total award bonus to be paid is $%s'
    print(allcars_awardbonus % '{:0,.2f}'.format(abc_awardbonus))
    print("\n") # Print new line to make it more pleasant on the eye
    
    # Display the award bonus each car contributed
    # Individual car award bonus is total reward bonus * contribution % (Eg. Total = 1mil, npatrol = 50% then idvidual car contribution is 500k)
    eachcar_awardbonus = 'The %s contributed $%s towards the total award bonus'
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        print(eachcar_awardbonus % (car_name[iteration_count], '{:0,.2f}'.format(abc_contribution[iteration_count])))
    print("\n") # Print new line to make it more pleasant on the eye

# Get Additional Bonus Rate Function - Gets the additional bonus rate
def getAdditionalBonusRate():
    additionalbonusrate = 'Please enter the additional bonus rate of the %s: '
    invalidadditionalbonusrate = '\nInvalid Data, %s\nPlease enter the additional bonus rate of the %s: '
    
    car_additionalbonusrate = [None] * number_of_cars # Create a list the length of the amount of cars
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_additionalbonusrate[iteration_count] = input(additionalbonusrate % car_name[iteration_count])
        while not percentValidation(car_additionalbonusrate[iteration_count]): # Call percentValidation function to check that input is valid
            car_additionalbonusrate[iteration_count] = input(invalidadditionalbonusrate % (invalid_percent, car_name[iteration_count])) # Inform user of invalid data and ask for input again
    
    print("\n") # Print new line to make it more pleasant on the eye
    
    return car_additionalbonusrate

# Calculate Additional Bonus Function - Calculates the additional bonus that should be paid for each car
def calculateAdditionalBonus(abc_contribution,abc_additionalbonusrate):
    car_additionalbonus = [None] * number_of_cars # Create a list the length of the amount of cars
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        car_additionalbonus[iteration_count] = abc_contribution[iteration_count] * (float(abc_additionalbonusrate[iteration_count]) / 100) # Calculate the % the car contributed towards the total award bonus
    
    return car_additionalbonus

# Display Additional Bonus Function - Displays the additional bonus paid of each car
def displayAditionalBonus(abc_additionalbonus):
    additionalbonus = 'The %s will pay an additional bonus of $%s for %s'
    for iteration_count in range(number_of_cars): # Loop through for each car and have variable interation_count as which interation number is currently running starting at 0
        print(additionalbonus % (car_name[iteration_count], '{:0,.2f}'.format(abc_additionalbonus[iteration_count]), yearrun))
    
    print("\n") # Print new line to make it more pleasant on the eye

# Calculate Total Bonus Function - Calculates the grand total bonus (bonus award + additional bonus)
def calculateTotalBonus(abc_awardbonus,abc_additionalbonus):
    totalbonus = abc_awardbonus + (abc_additionalbonus[0] + abc_additionalbonus[1] + abc_additionalbonus[2])
    
    return totalbonus

# Display Total Income Function - Displays the grand total and the total income of each car
def displayTotalBonus(abc_totalbonus):
    grandtotalbonus = 'The grand total bonus to be paid for %s is $%s'
    print(grandtotalbonus % (yearrun, '{:0,.2f}'.format(abc_totalbonus)))
    
    print("\n") # Print new line to make it more pleasant on the eye

#Run Program
while True: # Keep running the program until the user decides to QUIT
    # Display the Main Menu of the program
    print("===========================================")
    print("Welcome to ABC Car Shop:")
    print("Please choose an option from the followings.")
    print("< A>dd sales details in the database.")
    print("< S>earch sales details for a given year in the database.")
    print("< Q>uit.")
    print("===========================================\n")
    
    # Ask the user for input to the menu
    menu_selection = input("Please enter your slection (A/S/Q): ").upper()
    while not menuValidation(menu_selection): # Call menuValidation function to check that input is a valid response if not keep looping asking for valid input response
        print(invalid_menuresponse)
        menu_selection = input("Please enter your slection (A/S/Q): ").upper()

    # Perform the action based on the users input
    if menu_selection in response_add: # Check if response is A
        yearrun = input("What year would you like to calculate the costs for (Eg. 2014): ")
        while not yearValidation(yearrun): # Call yearValidation function to check that input is a valid response if not keep looping asking for valid input response
            print(invalid_yearresponse % (year_earliest_allowed, year_oldest_allowed))
            yearrun = input("What year would you like to calculate the costs for (Eg. 2014): ")
        mainMenu(menu_selection)
    
    elif menu_selection in response_search: # Check if response is S
        yearrun = input("What year would you like to calculate the costs for (Eg. 2014): ")
        while not yearValidation(yearrun): # Call yearValidation function to check that input is a valid response if not keep looping asking for valid input response
            print(invalid_yearresponse % (year_earliest_allowed, year_oldest_allowed))
            yearrun = input("What year would you like to calculate the costs for (Eg. 2014): ")
        mainMenu(menu_selection)
    
    elif menu_selection in response_quit: # Check if response is Q
        print("Thank you for using", welcome_message)
        raise SystemExit(0) # Exit with code 0 successful
    
    else: # This should not be possible due to menuValidation but if it happens print error and quit
        print("\nError: menuValidation function failed to catch invalid response. \nThis Error should have never occured please contact your System Administrator.")
        raise SystemExit(1) # Exit with code 1 failure
    
    print("\n") # Print new line to make it more pleasant on the eye
