#M24W0633
#Kanakarathne Kasun Madhawa

# Import modules for datetime operations, random number generation, and string manipulation
import datetime
import random
import string

# Define Customer class
class Customer:
    def __init__(self, name, address, phone, vehicle_number, make, model, year):
        # Initialize instance variables with customer and vehicle attributes
        self.name = name
        self.address = address
        self.phone = phone
        self.vehicle_number = vehicle_number
        self.make = make
        self.model = model
        self.year = year

# Define Booking class
class Booking:
    def __init__(self, customer, date, time, branch, booking_type, reference):
        # Initialize instance variables with booking attributes
        self.customer = customer
        self.date = date
        self.time = time
        self.branch = branch
        self.booking_type = booking_type
        self.reference = reference

# Define BookingSystem class
class BookingSystem:
    def __init__(self):
        # Initialize data structures for storing customers and bookings
        self.customers = [] # List to store Customer objects
        self.bookings = [] # List to store Booking objects
        # Define staff user credentials in a list of dictionaries
        self.staff_users = [
            {"username": "staff1", "password": "pass1"},
            {"username": "staff2", "password": "pass2"},
            {"username": "staff3", "password": "pass3"},
            {"username": "staff4", "password": "pass4"},
            {"username": "staff5", "password": "pass5"}
        ]
        # Define available branches and time slots in a list
        self.branches = ["Tokyo", "Osaka", "Kyoto", "Nara", "Chiba"]
        self.time_slots = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]

    # Generate a unique alphanumeric reference number
    def generate_reference(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Validate date string against YYYY-MM-DD format
    def validate_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # Create a new customer profile and add it to the customers list
    def create_customer_profile(self):
        name = input("Enter customer name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        vehicle_number = input("Enter vehicle number: ")
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        year = input("Enter vehicle manufacturing year: ")

        # Create a new Customer object with the input details and add it to the customers list
        customer = Customer(name, address, phone, vehicle_number, make, model, year)
        self.customers.append(customer) # Add a customer to the list
        print("Customer profile created successfully.")

    # Method for Search a customer in the customers list by their vehicle number.
    def find_customer(self, vehicle_number):
        for customer in self.customers:
            if customer.vehicle_number == vehicle_number:
                return customer
        return None # Return the Customer object if found; otherwise, return None.

    # Update an existing customer profile
    def edit_customer_profile(self):
        vehicle_number = input("Enter vehicle number: ")
        customer = self.find_customer(vehicle_number)
        if customer:
            customer.name = input("Enter new name: ")
            customer.address = input("Enter new address: ")
            customer.phone = input("Enter new phone number: ")
            customer.make = input("Enter new vehicle make: ")
            customer.model = input("Enter new vehicle model: ")
            customer.year = input("Enter new vehicle manufacturing year: ")
            print("Profile updated successfully.")
        else:
            print("Customer not found.")

    # Create a new service booking
    def book_service(self):
        vehicle_number = input("Enter vehicle number: ")
        customer = self.find_customer(vehicle_number)
        if not customer:
            print("Customer not found. Please create a profile first.")
            return

        date = input("Enter date (YYYY-MM-DD): ")
        if not self.validate_date(date):
            print("Invalid date format. Please try again.")
            return

        branch = input(f"Enter branch ({', '.join(self.branches)}): ")
        booking_type = input("Enter booking type (service/repair): ")

        if booking_type.lower() == 'service':
            available_slots = self.get_available_slots(date, branch)
            if not available_slots:
                print("No available slots for the selected date and branch.")
                return
            print("Available slots:", available_slots)
            time = input("Select a time slot: ")
            if time not in available_slots:
                print("Invalid time slot selected.")
                return
        else:
            time = "N/A"


        reference = self.generate_reference()
        # Create a new Booking object with the input details and add it to the booking list
        booking = Booking(customer, date, time, branch, booking_type, reference)
        self.bookings.append(booking)

        print("\nBooking Confirmation:")
        print(f"Reference Number: {reference}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"Branch: {branch}")
        print(f"Customer: {customer.name}")
        print(f"Vehicle: {customer.make} {customer.model} ({customer.vehicle_number})")

    # Get available time slots for a given date and branch
    def get_available_slots(self, date, branch):
        booked_slots = [booking.time for booking in self.bookings if booking.date == date and booking.branch == branch]
        return [slot for slot in self.time_slots if booked_slots.count(slot) < 2]

    # Display bookings for a specific vehicle(customer function)
    def view_booking(self):
        vehicle_number = input("Enter vehicle number: ")
        customer_bookings = [booking for booking in self.bookings if booking.customer.vehicle_number == vehicle_number]
        if customer_bookings:
            for booking in customer_bookings:
                print(f"\nReference: {booking.reference}")
                print(f"Date: {booking.date}")
                print(f"Time: {booking.time}")
                print(f"Branch: {booking.branch}")
                print(f"Type: {booking.booking_type}")
        else:
            print("No bookings found for this vehicle number.")

    # cancel a booking from the bookings list
    def cancel_booking(self):
        reference = input("Enter booking reference number: ")
        for booking in self.bookings:
            if booking.reference == reference:
                self.bookings.remove(booking) # Remove the specified booking from the bookings list
                print("Booking cancelled successfully.")
                return
        print("Booking not found.")

    # Display all bookings for a specific date and branch (staff function)
    def staff_view_bookings(self):
        date = input("Enter date (YYYY-MM-DD): ")
        branch = input(f"Enter branch ({', '.join(self.branches)}): ")
        day_bookings = [b for b in self.bookings if b.date == date and b.branch == branch]
        if day_bookings:
            for booking in day_bookings:
                print(f"\nReference: {booking.reference}")
                print(f"Time: {booking.time}")
                print(f"Type: {booking.booking_type}")
                print(f"Customer: {booking.customer.name}")
                print(f"Vehicle: {booking.customer.make} {booking.customer.model} ({booking.customer.vehicle_number})")
        else:
            print("No bookings found for the selected date and branch.")

    # Modify available time slots for a specific date and branch (staff function)
    def adjust_time_slots(self):
        date = input("Enter date (YYYY-MM-DD): ")
        branch = input(f"Enter branch ({', '.join(self.branches)}): ")
        print("Current time slots:", self.time_slots)
        new_slots = input("Enter new time slots (comma-separated, e.g., 09:00,10:00,11:00): ").split(',')
        self.time_slots = new_slots
        print("Time slots updated successfully.")

    #Define a method to export all bookings to a text file
    def export_bookings(self):
        try:
            with open("bookings.txt", "w") as file:  # Open a file named "bookings.txt" in write mode ("w")
                for booking in self.bookings:
                    # Write the booking details to the file
                    file.write(f"Reference: {booking.reference}\n")
                    file.write(f"Date: {booking.date}\n")
                    file.write(f"Time: {booking.time}\n")
                    file.write(f"Branch: {booking.branch}\n")
                    file.write(f"Type: {booking.booking_type}\n")
                    file.write(f"Customer: {booking.customer.name}\n")
                    file.write(f"Vehicle: {booking.customer.make} {booking.customer.model} ({booking.customer.vehicle_number})\n\n")
            print("Bookings exported to bookings.txt")
        # Handle any I/O errors that occur during file operations
        except IOError as e:
            print(f"Error exporting bookings: {e}")

    # Method to display and handle staff menu options
    def staff_menu(self):
        while True:
            print("\nStaff Menu:")
            print("1. Create customer profile")
            print("2. Create booking")
            print("3. Cancel booking")
            print("4. View all bookings of a location")
            print("5. Adjust service time slots")
            print("6. Export bookings")
            print("7. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_customer_profile()
            elif choice == '2':
                self.book_service()
            elif choice == '3':
                self.cancel_booking()
            elif choice == '4':
                self.staff_view_bookings()
            elif choice == '5':
                self.adjust_time_slots()
            elif choice == '6':
                self.export_bookings()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    # Method to display and handle customer menu options
    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. Create profile")
            print("2. Book a service")
            print("3. Edit profile")
            print("4. View booking")
            print("5. Cancel booking")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_customer_profile()
            elif choice == '2':
                self.book_service()
            elif choice == '3':
                self.edit_customer_profile()
            elif choice == '4':
                self.view_booking()
            elif choice == '5':
                self.cancel_booking()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    # Main program loop for the booking system
    def main(self):
        while True:
            print("\nWelcome to Car Service Booking System")
            print("1. Staff Login")
            print("2. Customer Menu")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if not any(user['username'] == username and user['password'] == password for user in self.staff_users):
                    # Raise an error if the credentials are invalid
                    try:
                        raise ValueError("Invalid credentials.")
                    except ValueError as e:
                        print(e) # Print the error message
                        continue # Restart the loop to allow for another login attempt
                self.staff_menu()
            elif choice == '2':
                self.customer_menu()
            elif choice == '3':
                print("Thank you for using the Car Service Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    booking_system = BookingSystem()# Create an instance of the BookingSystem class
    booking_system.main()  # Call the main method to start the program