from faker import Faker

fake = Faker()

class BaseContact:

    def __init__(self, first_name, last_name, phone=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone or "+48" + fake.numerify('#########')
        self.email = email or fake.email()

    @property
    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

class BusinessContact(BaseContact):

    def __init__(self, first_name, last_name, job_title=None, company=None, business_phone=None, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.job_title = job_title or fake.job()
        self.company = company or fake.company()
        self.business_phone = business_phone or "+48" + fake.numerify('#########')

    @property
    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name} z {self.company}"

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()

        if contact_type == BaseContact:
            contacts.append(BaseContact(first_name, last_name))
        elif contact_type == BusinessContact:
            contacts.append(BusinessContact(first_name, last_name))

    return contacts

if __name__ == "__main__":
    base_contacts = create_contacts(BaseContact, 3)
    business_contacts = create_contacts(BusinessContact, 3)

    for contact in base_contacts:
        print(contact.contact)
        print(f"Label length: {contact.label_length}")

    for contact in business_contacts:
        print(contact.contact)
        print(f"Label length: {contact.label_length}")
