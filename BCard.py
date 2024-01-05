from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self._label_length = len(f"{self.first_name} {self.last_name}")

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return self._label_length

class BusinessContact(BaseContact):
    def __init__(self, job_title, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name} z {self.company}"

    @property
    def label_length(self):
        return self._label_length

def create_contacts(contact_type, quantity):
    contacts = []
    fake = Faker('pl_PL')
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()

        if contact_type == BaseContact:
            contacts.append(contact_type(first_name, last_name, phone_number, email))

        elif contact_type == BusinessContact:
            company = fake.company()
            business_phone = "+48" + fake.numerify('#########')
            job_title = fake.job()
            contacts.append(contact_type(job_title, company, business_phone, first_name, last_name, phone_number, email))
    return contacts

if __name__ == "__main__":
    base_contacts = create_contacts(BaseContact, 3)
    business_contacts = create_contacts(BusinessContact, 3)

    for contact in base_contacts:
        print(contact.contact())
        print(f"Label length: {contact.label_length}")

    for contact in business_contacts:
        print(contact.contact())
        print(f"Label length: {contact.label_length}")
