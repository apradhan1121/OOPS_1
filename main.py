from Car import CarRental, Customer
import random

def main():
    shop = CarRental(100)
    l=[]
    i=0  #No customers are present


    while True:



        print(""" 


        ====== Car Rental Shop =======
        1. Owner
        2. User


        """)
        Login = input("Enter choice: ")   #Login Is Whether (Owner/User)

        try:
            Login = int(Login)
        except ValueError:
            print("That's not an int!")
            continue



        if (Login == 1):
            print("""

                  1.Display no. of Cars which currently at rent
                  2.Total Number of Customers visited
                  3.Total Rent Amount Generated

                  """)
            Owner = input("Enter choice: ")

            try:
                Owner = int(Owner)
            except ValueError:
                print("That's not an int!")
                continue

            if (Owner == 1):
                shop.Rentedstock()
            elif (Owner == 2):
                print("""

                      Total number of customers visited are :{} """.format(CarRental.get_subscribers()))
            elif (Owner == 3):
                print("Total Rent generated is equal to ${}".format(CarRental.get_totalbill()))
            else:
                print("Invalid input. Please enter number between 1-3 ")






        elif (Login == 2):

            print("""
                        1. Are you a New User
                        2. Are you a Existing User""")
            User = (input())
            try:
                User = int(User)
            except ValueError:
                print("That's not an int!")
                continue

            if (User == 1):
                customer = Customer()
                l.append(customer)
                print("Your customer id is:{} ".format(len(l)-1))




                print("""
                ====== Car Rental Shop =======
                1. Display available Cars
                2. Request a Car on hourly basis $25
                3. Request a Car on daily basis $50
                4. Request a Car on weekly basis $100
                5. Return a Car
                6. Exit
                """)

                choice = input("Enter choice: ")

                try:
                    choice = int(choice)
                except ValueError:
                    print("That's not an int!")
                    continue



                if choice == 1:
                    shop.displaystock()

                elif choice == 2:
                    customer.rentalTime = shop.rentCarOnHourlyBasis(customer.requestCar())
                    customer.rentalBasis = 1

                elif choice == 3:
                    customer.rentalTime = shop.rentCarOnDailyBasis(customer.requestCar())
                    customer.rentalBasis = 2

                elif choice == 4:
                    customer.rentalTime = shop.rentCarOnWeeklyBasis(customer.requestCar())
                    customer.rentalBasis = 3

                elif choice == 5:
                    customer.bill = shop.returnCar(customer.returnCar())
                    customer.rentalBasis, customer.rentalTime, customer.Cars = 0, 0, 0
                elif choice == 6:
                    break
                else:
                    print("Invalid input. Please enter number between 1-6 ")



            elif(User==2):  ##Existing Customer
                print("""
                Provide Your Customer id:""")

                b=(input())
                try:
                    b = int(b)
                except ValueError:
                    print("That's not an int!")
                    continue

                if(len(l)==0):
                    print("No customer Subscribed Yet.. ")
                elif(0<=b<=len(l)):
                    customer=l[b]

                    print("""
                                        ====== Car Rental Shop =======
                                        1. Balance History
                                        2. Return a Car
                                        3. Exit
                                        """)

                    choice = input("Enter choice: ")

                    try:
                        choice = int(choice)
                    except ValueError:
                        print("That's not an int!")
                        continue


                    if choice ==1:
                        customer.rentalTime, customer.rentalBasis, customer.Cars=(customer.returnCar())
                        print(""" 
                        -->RentalBasis: {}
                        -->RentalTime: {}
                        -->No. of Cars taken on Rent: {}""".format(customer.rentalBasis,customer.rentalTime,customer.Cars))

                    elif choice == 2:
                        customer.bill = shop.returnCar(customer.returnCar())
                        customer.rentalBasis, customer.rentalTime, customer.Cars = 0, 0, 0
                    elif choice == 3:
                        break
                    else:
                        print("Invalid input. Please enter number between 1-6 ")
                else:
                    print("Invalid Customer id.")

            else:
                print("Invalid input. Please enter number between 1-2 ")




        else:
            print("Invalid input. Please enter number between 1-2 ")
        print("Thank you for using the Car rental system.")


if __name__ == "__main__":
    main()