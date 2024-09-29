from enum import Enum # Enum for currency
class Currency(Enum):
    USD = "USD"
    AED = "AED"

class Customer:     # A customer in the hotel reservation system.
    def __init__(self, customer_id, name, email, phone_number):
        self.__customer_id = customer_id
        self.__name = name
        self.set_email(email)  # Call the method to set the email, ensuring it's valid
        self.__phone_number = phone_number

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    def get_customer_id(self):
        return self.__customer_id
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_email(self, email):
        while '@' not in email:  # Keep asking until a valid email is provided
            print("Email must contain '@'. Please enter a valid email.")
            email = input("Enter email: ")  # Prompt user for email
        self.__email = email  # Set valid email

    def get_email(self):
        return self.__email
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    def get_phone_number(self):
        return self.__phone_number

# Reservation class
class Reservation:     # Reservation made by a customer.
    def __init__(self, reservation_id, customer_id, room_id, check_in_date, check_out_date, status):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__room_id = room_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id
    def get_reservation_id(self):
        return self.__reservation_id
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    def get_customer_id(self):
        return self.__customer_id
    def set_room_id(self, room_id):
        self.__room_id = room_id
    def get_room_id(self):
        return self.__room_id
    def get_check_in_date(self):
        return self.__check_in_date
    def get_check_out_date(self):
        return self.__check_out_date
    def set_status(self, status):
        self.__status = status
    def get_status(self):
        return self.__status

# Room class
class Room:      # A room in the hotel.
    def __init__(self, room_id, room_type, price_per_night, availability_status):
        self.__room_id = room_id
        self.__room_type = room_type      # Type of the room (Suite, Deluxe, Standard).
        self.__price_per_night = price_per_night  #Price charged per night for the room.
        self.__availability_status = availability_status

    def set_room_id(self, room_id):
        self.__room_id = room_id
    def get_room_id(self):
        return self.__room_id
    def get_room_type(self):
        return self.__room_type
    def get_price_per_night(self):
        return self.__price_per_night
    def set_availability_status(self, status):
        self.__availability_status = status
    def get_availability_status(self):
        return self.__availability_status

# Payment class
class Payment:      # Represents the payment made for a reservation.
    def __init__(self, payment_id, reservation_id, amount, currency, payment_status):
        self.__payment_id = payment_id
        self.__reservation_id = reservation_id
        self.__amount = amount
        self.__currency = currency    # Currency in which the payment is made (USD, AED).
        self.__payment_status = payment_status      # Current status of the payment (Completed, Pending).

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id
    def get_payment_id(self):
        return self.__payment_id
    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id
    def get_reservation_id(self):
        return self.__reservation_id
    def set_amount(self, amount):
        self.__amount = amount
    def get_amount(self):
        return self.__amount
    def set_payment_status(self, status):
        self.__payment_status = status
    def get_payment_status(self):
        return self.__payment_status
    def get_currency(self):
        return self.__currency


class HotelStaff:      # A staff member working at the hotel.
    def __init__(self, staff_id, name, position):
        self.__staff_id = staff_id
        self.__name = name
        self.__position = position     # Job title of the staff member (Receptionist, Manager).

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id
    def get_staff_id(self):
        return self.__staff_id
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_position(self, position):
        self.__position = position
    def get_position(self):
        return self.__position

class System:     # The hotel management system.
    def __init__(self, system_id):
        self.__system_id = system_id
        self.__reservations = []
        self.__rooms = []

    def set_system_id(self, system_id):
        self.__system_id = system_id
    def get_system_id(self):
        return self.__system_id
    def get_reservations(self):
        return self.__reservations
    def get_rooms(self):
        return self.__rooms


#Scenario 1: Customer Reservation and Room Assignment (WITH an invalid email)
# Create a customer
customer1 = Customer(2024001, "Abdulaziz Omar", "Abdulaziz.Omar1gmail.com", "+971501234567")
print("Customer Details:")
print("ID:", customer1.get_customer_id())
print("Name:", customer1.get_name())
print("Email:", customer1.get_email())
print("Phone:", customer1.get_phone_number())

# Create a room
print("Room Details:")
room1 = Room(34, "Deluxe", 500, "Available")
print("Room ID:", room1.get_room_id())
print("Type:", room1.get_room_type())
print("Price per night:", room1.get_price_per_night())
print("Availability:", room1.get_availability_status())

# Create a reservation
print("Reservation Details:")
reservation1 = Reservation(1001, customer1.get_customer_id(), room1.get_room_id(), "2024-10-01", "2024-10-05", "Pending")
print("Reservation ID:", reservation1.get_reservation_id())
print("Customer ID:", reservation1.get_customer_id())
print("Room ID:", reservation1.get_room_id())
print("Check-in:", reservation1.get_check_in_date())
print("Check-out:", reservation1.get_check_out_date())
print("Status:", reservation1.get_status())



# Scenario 2: Payment Processing
# Create a payment
print("Payment Details:")
payment1 = Payment(2001, reservation1.get_reservation_id(), 2500, Currency.AED, "Pending")
print("Payment ID:", payment1.get_payment_id())
print("Reservation ID:", payment1.get_reservation_id())
print("Amount:", payment1.get_amount())
print("Currency:", payment1.get_currency().value)
print("Payment Status:", payment1.get_payment_status())

# Update payment status to "Completed"
payment1.set_payment_status("Completed")
print("Updated Payment Status:", payment1.get_payment_status())



# Scenario 3: Staff Checking Customer In and Out
# Create a hotel staff member
print("Hotel Staff Details:")
staff1 = HotelStaff(221, "Khalid ismael", "Receptionist")
print("Staff ID:", staff1.get_staff_id())
print("Name:", staff1.get_name())
print("Position:", staff1.get_position())

# Update reservation status to "Checked In"
reservation1.set_status("Checked In")
print("Updated Reservation Status (Check-In):", reservation1.get_status())

# Update reservation status to "Checked Out"
reservation1.set_status("Checked Out")
print("Updated Reservation Status (Check-Out):", reservation1.get_status())
