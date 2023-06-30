# Import the csv module to read the CSV file containing duck data.
import csv
# Import the pyplot module from the matplotlib library for creating graphs.
import matplotlib.pyplot as plt

# Create a dictionary called ducks to store the data read from the CSV file
ducks = {}

# Read the data from the CSV file into the ducks dictionary using the csv.DictReader class.
with open ('duck_data.csv', newline= '') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader :
        ducks [row ['id']] = {'id' : int(row['id']),'species': row ['species'], 'category': row ['category'], 'length_cm': float(row ['length_cm']), 'wingspan_cm': float(row ['wingspan_cm']), 'body_mass_g': float(row ['body_mass_g'])}
   
# use while loop to iterate through the program
while True:
 # Ask the user to choose one of the options below 
    print('Duck Attribute Analysis')  
    choice = input('   Please choose one of : \n'
                   '      1 - Display a bar chart of a duck\'s measurements \n'
                   '      2 - Display a scatter plot of attribute measurements \n '
                   '      3 - Exit the software \n' 
                   'Your choice? : ' )
# use if statement to allow use to choose between charts 
    if choice == '1':
        # create a bar chart using matplotlib
        duck_id = int(input("Please enter the duck\'s ID number: "))
        duck = ducks.get(str(duck_id))
        if duck is not None:
            attributes = ['length_cm', 'wingspan_cm', 'body_mass_g']
            values = [duck[attr] for attr in attributes]
            plt.bar(attributes, values)
            plt.show()
        else:
            print("Invalid duck id")
    elif choice == '2':
        # create scatter plot using matplotlib
        attribute = input("Enter one of these attribute name (length_cm, wingspan_cm or body_mass_g): ")
        if attribute in ['length_cm', 'wingspan_cm', 'body_mass_g']:
            x_values = [d[attribute] for d in ducks.values()]
            y_values = [(d['length_cm'] + d['wingspan_cm'] + d['body_mass_g']) / 3 for d in ducks.values()]
            plt.scatter(x_values, y_values)
            plt.xlabel(attribute)
            plt.ylabel("Average length, wingspan, and mass")
            plt.show()
        else:
            print("Invalid attribute name")
    elif choice == '3':
        # Exit program
        break
    else:
        print("Invalid choice")