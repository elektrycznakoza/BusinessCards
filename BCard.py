from faker import Faker

fake = Faker()

class BaseContact:

  def __init__(self, first_name, last_name, phone, email):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email

  def contact(self):
    print(
        f"Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"
    )

  @property
  def label_length(self):
    return len(f"{self.first_name} {self.last_name}")

class BusinessContact(BaseContact):

  def __init__(self, first_name, last_name, phone, email, job_title, company,
               business_phone):
    super().__init__(first_name, last_name, phone, email)
    self.job_title = job_title
    self.company = company
    self.business_phone = business_phone

  def contact(self):
    print(
        f"Wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name} z {self.company}"
    )

def create_contacts(contact_type, quantity):
  contacts = []
  for _ in range(quantity):
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone = "+48" + fake.numerify('#########')
    email = fake.email()

    if contact_type == BaseContact:
      contacts.append(BaseContact(first_name, last_name, phone, email))
    elif contact_type == BusinessContact:
      job_title = fake.job()
      company = fake.company()
      business_phone = "+48" + fake.numerify('#########')
      contacts.append(
          BusinessContact(first_name, last_name, phone, email, job_title,
                          company, business_phone))
  return contacts

base_contacts = create_contacts(BaseContact, 3)
business_contacts = create_contacts(BusinessContact, 3)

for contact in base_contacts:
  contact.contact()
  print(f"Label length: {contact.label_length}")

for contact in business_contacts:
  contact.contact()
  print(f"Label length: {contact.label_length}")
