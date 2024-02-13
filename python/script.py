    
def hello():
    name = str(input("Enter your name: "))
    if name:
        print('hello ' + str(name))
    else:
        print('hello world')
  
        return 
        
hello()      
 

 
def say():
    say1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num1 = [2, 4, 6, 8, 10]

    print(say1[7])
    print(num1[0])
    
    say()

def user_data():
    
    name =input("Your Name :" +" ")
    age = (input("Your age :"))
    work = input("your work exp : ")
    
    
    print(' nice to meet you : '+ name )

user_data()

def crunt_age():

 brith_year = input( "enter your brith year : " )
 
 age = 2024 - int(brith_year)
 
 print(age)

crunt_age()

# if you commpaer the int to the str it will thro KeyError

   


def allo():
    age = input("Enter Your Age : ")
    not_allowed_age = 18  # Adjust the age threshold as needed
    
    if int(age) >= not_allowed_age:
        print("Adult")
    else:
        print("Minors are not allowed")

allo()
def all(): 
        
 A = 13
 B = 12

 if A == B :
        print(True)
 else:
        print(False)

all()

def start():
        
    Take_Number = int(input('Enter your Number : ')) 
    
    if Take_Number % 2 == 0:
        print("even")
    else:
        print("odd")
        

start()


def My_function ():
        new_patient = input('what is your Nmae :')
        patient_age = int(input('Age:'))
        new_one = True
        
        print(new_patient,patient_age,new_one)

My_function()