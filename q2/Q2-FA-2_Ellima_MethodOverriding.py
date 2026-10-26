class Patient:

    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_bill_amount(self) -> float:
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float) -> None:
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self) -> float:
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        discount = 0.20
        return original_bill * (1 - discount)


class PhilHealthPatient(Patient):
    def calculate_bill(self) -> float:
        original_bill = self.get_bill_amount()
        discount = 0.15
        return original_bill * (1 - discount)

if __name__ == "__main__":
   
    regular_patient = Patient("Juan Dela Cruz", 15000)
    senior_patient = SeniorPatient("Maria Clara", 15000)
    philhealth_patient = PhilHealthPatient("Jose Rizal", 15000)

    patients = [regular_patient, senior_patient, philhealth_patient]

    for patient in patients:
        name = patient.get_name()
        original_bill = patient.get_bill_amount()
        final_bill = patient.calculate_bill()

        print(f"Patient Name  : {name}")
        print(f"Original Bill : PHP {original_bill:,.2f}")
        print(f"Final Bill    : PHP {final_bill:,.2f}")
