from faker import Faker

class BaseContact:
    def __init__(self, first_name=None, last_name=None, phone=None, email=None, faker_instance=None):
        self._faker = faker_instance or Faker()
        self._first_name = first_name or self._faker.first_name()
        self._last_name = last_name or self._faker.last_name()
        self._phone = phone or "+48" + self._faker.numerify('#########')
        self._email = email or self._faker.email()

    def contact(self):
        return f"Wybieram numer {self._phone} i dzwonię do {self._first_name} {self._last_name}"

    @property
    def label_length(self):
        return len(f"{self._first_name} {self._last_name}")

class BusinessContact(BaseContact):
    def __init__(self, first_name=None, last_name=None, job_title=None, company=None, business_phone=None, faker_instance=None, **kwargs):
        super().__init__(first_name, last_name, faker_instance=faker_instance, **kwargs)
        self._job_title = job_title or self._faker.job()
        self._company = company or self._faker.company()
        self._business_phone = business_phone or "+48" + self._faker.numerify('#########')

    def contact(self):
        return f"Wybieram numer {self._business_phone} i dzwonię do {self._first_name} {self._last_name} z {self._company}"

    @property
    def label_length(self):
        return len(f"{self._first_name} {self._last_name}")

def create_contacts(contact_type, quantity, faker_instance=None):
    fake = faker_instance or Faker()
    contacts = []
    for _ in range(quantity):
        contacts.append(contact_type(faker_instance=fake))

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