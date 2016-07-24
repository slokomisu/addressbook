class Contact(self):

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def print_information(self):
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Phone Number: " + "(" + self.phone_number[:2] + ")" + "-" + self.phone_number[3:5] + "-" + self.phone_number[6:])
