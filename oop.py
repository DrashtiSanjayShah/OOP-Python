class Atm:
    counter = 1
   
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.sno = Atm.counter
        Atm.counter = Atm.counter + 1
        #self.menu()

    def menu(self):
        user_input = input('''
                           Hello how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to check balance
                           3. Enter 3 to withdraw money
                           4. Enter 4 to deposit money 
                           5. Enter 5 to exit 
                            ''')
        if user_input == '1':
            print('You have chosen to create pin')
            self.create_pin()
        elif user_input =='2':
            print('You have chosen to check balance')
            self.check_balance()
        elif user_input =='3':
            print("You have chosen to withdraw money")
            self.withdraw_money()
        elif user_input =='4':
            print("You have chosen to deposit money")
            self.deposit()
        elif user_input =='5':
            print("You have chosen to exit")
        else:
            print("Exit")
    
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Your pin is: ", self.__pin)

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            temp1 = int(input("Enter the amount you want to deposit: "))
            print("You have deposited ", temp1)
            self.balance += temp1
            print("Your balance is: ", self.__balance)
        
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print("Your balance is: ", self.__balance)
        else:
            print("Incorrect pin")
    def withdraw_money(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            temp2 = int(input("Enter the amount you want to withdraw: "))
            if temp2 <= self.__balance:
                print("You have withdrawn ", temp2)
                self.balance -= temp2
                print("Your balance is: ", self.__balance)
            else:
                print("Insufficient balance")


                
 #functions inside class are called methods.

#init is a constructor. Counstructor is a special method inside which the code gets executed automatically.
        #__somename__ becomes a dunder method or magic method. They are not called by object, it is triggered automatically.
        #the code that is written there runs without the user knowing.
        #self is the object with which you are currently working.
        #two methods in the same class cannot access/call each other. This is possible only using 'self'.
        #INSTANCE VARIABLE IS A VARIABLE FOR WHIVH THE VALUE IS DIFFERENT.
        
#we have used '__' before pin and balance in order to hide it from the other methods. This is because we dont want users to access it.
        #BUT, NOTHING IN PYTHON IS TRULY PRIVATE.
                
#REFERENCE VARIABLE
    #when we do
                #sbi = Atm()
                #sbi is not the object, it is the REFERENCE VARIABLE. if we do not do the 'sbi = Atm()' then, Atm() will be lost as it is
                #not stored in any variable.
#OBJECTS OF A CLASS IN PYTHON ARE MUTABLE.

#there are two types of variables - instance variable:- changes(pin,balance), is always outside the method.
#                                   static variable:- remains same

#The child class also inherits the constructor of the parent.

#METHOD OVERRIDING:- If the parent and the child class have a method with the same name, the child method will be executed.

#IF THE CHILD CLASS HAS A CONSTRUCTOR, THEN THE PARENT CLASS CONSTRUCTOR WILL NOT BE INVOKED.SO, IF THERE WAS ANY ATTRIBUTE DEFINED IN THE PARENT CLASS THAT
#IS NEEDED BY THE CHILD, THE CHILD CLASS WILL NOT BE ABLE TO EXECUTE IT.

#IF WE HAVE A CONSTRUCTOR IN RHE CHILD CLASS AND ALSO WANT TO USE THE CONSTRUCTOR OF THE PARENT CLASS, WE CAN USE THE super() KEYWORD

#METHOD OVERLOADING: ONE METHOD IS IMPLEMENTED IN DIFFERENT WAYS.eg: area of all the shapes
