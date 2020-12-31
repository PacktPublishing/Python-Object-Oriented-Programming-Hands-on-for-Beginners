# Project Solution


class Patient:
    __government_discount = 0.5
    __doctor_discount = 0
    __hospital_discount = 0
    __single_payment_discount = 0

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, first_name, last_name, address, phone_number, total_charges):
        # Object Attributes/Variables
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.total_charges = total_charges

    # Properties
    @property
    def doctor_discount(self):
        return self.__doctor_discount

    @doctor_discount.setter
    def doctor_discount(self, doctor_discount):
        if 0.00 <= doctor_discount <= 5.00:
            self.__doctor_discount = doctor_discount / 100
        else:
            error_msg = "Doctor discount must be between 0% and 5%. Discount not applied."
            print("{} {} : {}".format(self.first_name, self.last_name, error_msg))


    @property
    def hospital_discount(self):
        return self.__hospital_discount

    @hospital_discount.setter
    def hospital_discount(self, hospital_discount):
        if 0.00 <= hospital_discount <= 5.00:
            self.__hospital_discount = hospital_discount / 100
        else:
            error_msg = "Hospital discount must be between 0% and 5%. Discount not applied."
            print("{} {} : {}".format(self.first_name, self.last_name, error_msg))


    @property
    def single_payment_discount(self):
        return self.__single_payment_discount

    @single_payment_discount.setter
    def single_payment_discount(self, single_payment_discount):
        if 0.00 <= single_payment_discount <= 5.00:
            self.__single_payment_discount = single_payment_discount / 100
        else:
            error_msg = "Single Payment discount must be between 0% and 5%. Discount not applied."
            print("{} {} : {}".format(self.first_name, self.last_name, error_msg))

    #  Methods
    def calculate_payment(self):
        amount_due = self.total_charges
        doctor_discount_amount = amount_due * self.__doctor_discount
        hospital_discount_amount = amount_due * self.__hospital_discount
        single_payment_discount_amount = amount_due * self.__single_payment_discount
        government_discount_amount = amount_due * self.__single_payment_discount
        return amount_due - doctor_discount_amount - hospital_discount_amount\
               - single_payment_discount_amount - government_discount_amount


class PaymentProcessor:
    def __init__(self, list_of_patients):
        self.list_of_patients = list_of_patients

    def print_patient_dues(self):
        print()
        print("-" * 75)
        print("{:15} {:21} {:15} {:10}".format("First", "Last", "Tot. Amt.", "After Discount"))
        print("-" * 75)
        for patient in self.list_of_patients:
            print("{:15} {:15} {:15} {:20}".format(patient.last_name, patient.first_name, patient.total_charges, patient.calculate_payment()))


def main():
    '''
    first_name = str(input("Enter the patient's first name : "))
    last_name = str(input("Enter the patient's last name : "))
    address = str(input("Enter the patient's address : "))
    phone_number = str(input("Enter the patient's phone number : "))
    total_charges = str(input("Enter the patient's total charges : "))
    '''
    patient1 = Patient("John", "Key", "1505 Main St, Main, CA", "111-222-3333", 10000.00)
    patient1.doctor_discount = 0
    patient1.hospital_discount = 0
    patient1.single_payment_discount = 5

    patient2 = Patient("Matt", "Simon", "1022 Main St, Main, CA", "111-222-3333", 50000.00)
    patient2.doctor_discount = 5
    patient2.hospital_discount = 5
    patient2.single_payment_discount = 5

    patient3 = Patient("Bob", "Tori", "1022 Main St, Main, CA", "111-222-3333", 50000.00)
    patient3.doctor_discount = 10
    patient3.hospital_discount = 5
    patient3.single_payment_discount = 5

    patient3 = Patient("Peter", "Thompson", "1022 Main St, Main, CA", "111-222-3333", 50000.00)
    patient3.doctor_discount = 10
    patient3.hospital_discount = 5
    patient3.single_payment_discount = 10

    list1 = [patient1, patient2, patient3]
    payment_processor = PaymentProcessor(list1)
    payment_processor.print_patient_dues()


if __name__ == '__main__':
    main()
