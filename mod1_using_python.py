'''
Created on Jul 26, 2016

@author: rafacarv
'''

#This is where you program starts.
if __name__ == '__main__':
    
    #Greet the user by writing something on the console.
    print ("Hello! Welcome!")
    
    #Asks a question to the user using the console
    name = raw_input("What's your name? ")
    
    #Sets up a starting value
    age = 0 
    while (age == 0):
        
        try:
            #Asks a question to the user... Specifically a number
            number = int (raw_input("How old are you? "))
            age = number
        except ValueError:
            #If the user does not provide a valid number, prints an error message.
            print("Invalid entry. Please enter a number")
    
    #Prints the result of the interaction.
    print ("Nice to meet you, {} ({})".format(name, age))