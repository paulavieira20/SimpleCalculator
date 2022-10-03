#import classes
import main
import functionsCalculator

#class to chose the operation or continue
class OperationsToRun:
    
    #ask the user to chose if he wants to continue or not
    def continue_operation():
        continue_operation = input("Do you want to continue? (y/n): ")
        if continue_operation == "y":
            OperationsToRun.chose_operation()
            
        else:
            print("Exit! Thank you for using the calculator!")
            exit()
        
    #ask the user to chose the operation
    def chose_operation():
        
        print("Select operation. \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Power \n 6.Exit")  
        chosed_operation = input("Choose the operation:\n") 
        
        validInput = {"1", "2", "3", "4", "5"}	#set of valid inputs
        
        if chosed_operation in validInput:

            value_A = int(input("Enter the first value: "))
            value_B = int(input("Enter the second value: ")) 
            
            #sum operation
            if chosed_operation == "1":
                ValueCalculated = functionsCalculator.Calculator.sum(value_A, value_B)
                print('{} + {} = '.format(value_A, value_B)) #print the equation
                
            #subtract operation
            elif chosed_operation == "2":
                ValueCalculated = functionsCalculator.Calculator.subtract(value_A, value_B)
                print('{} - {} = '.format(value_A, value_B)) #print the equation
            
            elif chosed_operation == "3":
                ValueCalculated = functionsCalculator.Calculator.multiply(value_A, value_B)
                print('{} * {} = '.format(value_A, value_B)) #print the equation
            
            #divide operation
            elif chosed_operation == "4":
                ValueCalculated = functionsCalculator.Calculator.divide(value_A, value_B)
                print('{} / {} = '.format(value_A, value_B)) #print the equation
            
            #power operation
            elif chosed_operation == "5":
                ValueCalculated = functionsCalculator.Calculator.power(value_A, value_B)
                print('{} ^ {} = '.format(value_A, value_B)) #print the equation
                
            else:
                exit()
               
            #print the result and ask if the user wants to continue 
            print("The result is: ",ValueCalculated)
            OperationsToRun.continue_operation() #run the function to chose the operation 
        
        #exit the program if the user chose 6
        elif chosed_operation == "6":
                    print("\n----------------------------------------------------")
                    print("\n Exit! Thank you for using the calculator!\n")
                    exit()

        #if the user chose a invalid option, ask again
        else:    
            print("\n----------------------------------------------------")
            print("\n Invalid operation! Please try again.\n")
            print("\n----------------------------------------------------")
            OperationsToRun.chose_operation() #run the function to chose the operation
        
           
   
