# This program is used to allow for entry of apps from the Google store, calculates
# total revenue for the developers and produces a csv file.
# Licensed under the LGPL v2

def message(): #user instructions and keybindings
    welcome = """
    Aaron's App Market Share Estimator Calculator
    Input app details into the app and a formatted .csv file
    will be produced. This program uses VIM type keybindings.
    
    ~ Keybindings ~
    type w to create a new csv file.
    type q to quit.
    """
    print(welcome) 

    
def main(): #main loop for program
    message()
    user = input("Option ~ ") #user input logic- uses VIM style input to match my editor
    if user == "w":
            create_file() #call procedure which creates the csv file
    elif user == "q":
            boolean = False #if user selects 'q', the boolean variable switches state and quits the program


def create_file(): #main procedure for producing the csv file.
    name = input("Type file name ~ ") + ".csv" #user selects file name, file type selection is hard coded as csv
    file = open(name, "w") #take file name and type from 'name' and set permission to write to document
    file.write("App Name, " + "Developer Name, " + "Number of Reviews, " + "App Price, " + "Estimated Revenue (-30%)"+ "\n") #print column names

    #user selects number of lines they would like add, the for loop then runs that many times
    loops = int(input("How many lines would you like to add ~ "))

    for i in range(0, loops):
            i += 1 # 'i' = counter variable, adds 1 with each iteration 

            if i <= loops: 
                    app_name = input("Type app name~ ") #user input types in app_name which then added to dictionary
                    line["app"] = app_name + ", " #assign app name to dictionary position, comma is added for csv formatting
                    
                    developer = input("Type developer name~ ")
                    line["app_developer"] =  developer + ", "
                    
                    reviews = int(input("Input number of reviews~ "))
                    line["reviews"] = reviews
                    
                    app_price = float(input("Input price of app (£ OR $) ~ "))
                    line["price"] = app_price 

                    print(" ") #blank space to break up iteration in terminal

                    line["revenue_est"] = ( app_price * reviews ) - ( 30 * ( app_price * reviews) ) / 100 #calculate revenue and deduct google's cut
                    float("{0:.2f}".format(line["revenue_est"])) #round off the total revenue - 30% to 2 D.P.

                    #index each dictionary position, ints and floats are converted to strings, creates line to be added to csv.
                    output = line["app"]+ line["app_developer"] + str(line["reviews"]) + ", £" + str(line["price"]) + ", £" + str(line["revenue_est"]) + "\n"

                    #writes the above line to csv.
                    file.write(output)

                    #loop repeats and adds as many lines as selected by user in 'loops'
            elif i >= loops: #once loops value is reached, close the csv file and return to program menu
                    file.close()
                    main()
                    
#line dictionary initiall __blank__ until assigned during user input
line = { "app" : " ", "app_developer" : " ", "reviews": 0, "price":0.00, "revenue_est" : 0.00}

#boolean tester
boolean = True

#start the program
main()





     

