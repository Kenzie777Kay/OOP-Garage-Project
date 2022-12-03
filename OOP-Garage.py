class ParkingGarage():

    takenSpaces = []

    takenTickets = []

    currentTickets = {}

    def __init__(self, tickets, parkingSpaces):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces


    def takeTicket(self):
        self.takenTickets.append(self.tickets.pop())
        self.takenSpaces.append(self.parkingSpaces.pop())
        self.currentTickets["paid"] = False
        print(self.takenTickets)
        print(self.tickets)

    def payParking(self):
        payment = input("Please enter amount(8): ")
        if payment == "8":
            print("Ticket has been paid, you have 15 minutes to leave the lot.")
            self.currentTickets.update({"paid": True})
            print(self.currentTickets)
        else:
            print("Tickets are 8 dollars, please pay correct amount. No Change.")

    def leaveLot(self):
        if self.currentTickets["paid"]:
            print("Thank you, have a nice day!")
            self.tickets.append(self.takenTickets.pop())
            self.parkingSpaces.append(self.takenSpaces.pop())
        else:
            self.payForParking()
        


tickets = [1, 2, 3, 4, 5]
parking_spots = [1, 2, 3, 4, 5]


garage = ParkingGarage(tickets, parking_spots)

while True:
    user_input = input("What would you like to do? take/pay/leave/quit: ").lower()

    if user_input == "quit":
        break
    elif user_input == 'take':
        garage.takeTicket()
    elif user_input == 'pay':
        garage.payParking()
    elif user_input == 'leave':
        garage.leaveLot()






