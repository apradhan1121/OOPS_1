import datetime


class CarRental:
    __Subscribers = 0  # STATIC VARIABLE
    __TotalBill = 0

    def __init__(self, stock=0):
        """
        Our constructor class that instantiates Car rental shop.
        """

        self.stock = stock


    def get_subscribers():  # @STATIC METHODS #Encapsulation
        return CarRental.__Subscribers

    def get_totalbill():
        return CarRental.__TotalBill

    def Rentedstock(self):
        """
        Displays the Cars currently available for rent in the shop.
        """
        c = 100 - self.stock
        print("There are total {} Cars on rent.".format(c))
        return c

    def displaystock(self):
        """
        Displays the Cars currently available for rent in the shop.
        """

        print("We have currently {} Cars available to rent.".format(self.stock))
        return self.stock

    def rentCarOnHourlyBasis(self, n):
        """
        Rents a Car on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of Cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} Cars available to rent.".format(self.stock))
            return None

        else:
            CarRental.__Subscribers = CarRental.__Subscribers + 1
            now = datetime.datetime.now()
            print("--> You have rented {} Car(s) on hourly basis on {}".format(n, now.strftime("%c")))
            print("--> You will be charged $25 for each hour per Car.")
            print("We hope that you enjoy our service.")

            self.stock -= n

            return now

    def rentCarOnDailyBasis(self, n):
        """
        Rents a Car on daily basis to a customer.
        """
        if n <= 0:
            print("Number of Cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} Cars available to rent.".format(self.stock))
            return None

        else:
            CarRental.__Subscribers = CarRental.__Subscribers + 1
            now = datetime.datetime.now()
            print("--> You have rented {} Car(s) on daily basis on {}".format(n, now.strftime("%c")))
            print("--> You will be charged $50 for each day per Car.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rentCarOnWeeklyBasis(self, n):
        """
        Rents a Car on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of Cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} Cars available to rent.".format(self.stock))
            return None

        else:
            CarRental.__Subscribers = CarRental.__Subscribers + 1
            now = datetime.datetime.now()
            print("--> You have rented {} Car(s) on weekly basis on {}".format(n, now.strftime("%c")))
            print("--> You will be charged $100 for each week per Car.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now


    def returnCar(self, request):
        """
        1. Accept a rented Car from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            print("RentalTime is:",rentalTime)
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfCars

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfCars

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfCars

            if (3 <= numOfCars <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            CarRental.__TotalBill = CarRental.__TotalBill + bill

            print("Thanks for returning your Car. Hope you enjoyed our service!")
            print("""

                Your Bill Receipt is:
                  "1.Selected RentalBasis:{}
                  "2.Booking Time:{}
                  "3.Returning Time:{}
                  "4.No Of Cars:{}
                  "5.Rental Period:{}""".format(rentalBasis, rentalTime, now, numOfCars, rentalPeriod)
                  )
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a Car with us?")
            return None


class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.Cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestCar(self):
        """
        Takes a request from the customer for the number of Cars.
        """

        Cars = input("How many Cars would you like to rent?")
        try:
            Cars = int(Cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if Cars < 1:
            print("Invalid input. Number of Cars should be greater than zero!")
            return -1
        else:
            self.Cars = Cars
        return self.Cars

    def returnCar(self):
        """
        Allows customers to return their Cars to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.Cars:
            return self.rentalTime, self.rentalBasis, self.Cars
        else:
            return 0, 0, 0
