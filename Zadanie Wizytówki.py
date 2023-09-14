import random
from faker import Faker


class BaseContact:
    def __init__(self, imię, nazwisko, p_n_privat, adres_e_mail):
        self.imię = imię
        self.nazwisko = nazwisko
        self.p_n_privat = p_n_privat
        self.adres_e_mail = adres_e_mail

    def contact(self):
        print(
            f"Wybieram numer {self.p_n_privat} i dzwonię do {self.imię} {self.nazwisko}")

    @property
    def label_length(self):
        return len(self.imię) + len(self.nazwisko)


class BusinessContact(BaseContact):
    def __init__(self, imię, nazwisko, p_n_privat, adres_e_mail, nazwa_firmy, stanowisko, p_n_work):
        super().__init__(imię, nazwisko, p_n_privat, adres_e_mail)
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.p_n_work = p_n_work

    def contact(self):
        print(
            f"Wybieram numer {self.p_n_work} i dzwonię do {self.imię} {self.nazwisko}")


def create_contacts(contact_type, quantity):
    fake = Faker()
    contacts = []

    for _ in range(quantity):
        if contact_type == BaseContact:
            contact = BaseContact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email(),
            )
        elif contact_type == BusinessContact:
            contact = BusinessContact(
                fake.first_name(),
                fake.last_name(),
                fake.phone_number(),
                fake.email(),
                fake.company(),
                fake.job(),
                fake.phone_number(),
            )
        contacts.append(contact)

    return contacts


contacts = create_contacts(BaseContact, 3)
for contact in contacts:
    contact.contact()
    print(f"Label length: {contact.label_length}")

business_contacts = create_contacts(BusinessContact, 3)
for contact in business_contacts:
    contact.contact()
    print(f"Label length: {contact.label_length}")
