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

  # def is_private_number(self):
  #     # Przyjmujemy, że numer prywatny zaczyna się od +48 5 lub +48 6
  #     return self.phone.startswith("+485") or self.phone.startswith("+486")


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

  # def is_private_number(self):
  #     # Przyjmujemy, że numer służbowy zaczyna się od +48 7 lub +48 8
  #     return not super().is_private_number()


def create_contacts(contact_type, quantity):
  contacts = []
  for _ in range(quantity):
    first_name = fake.first_name()
    last_name = fake.last_name()
    # Formatowanie numeru w formacie E.164 z kodem kraju Polski (+48)
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


# Po 3 kontakty
base_contacts = create_contacts(BaseContact, 3)
business_contacts = create_contacts(BusinessContact, 3)

# print("Prywatne kontakty:")
for contact in base_contacts:

  contact.contact()
  print(f"Label length: {contact.label_length}")
  # print(f"Private number: {contact.is_private_number()}")

# print("Biznesowe kontakty:")
for contact in business_contacts:
  contact.contact()
  print(f"Label length: {contact.label_length}")
  # print(f"Private number: {contact.is_private_number()}")

# # Łączenie
# all_contacts = base_contacts + business_contacts

# # Sortowanie
# sorted_contacts = sorted(all_contacts, key=lambda x: x.label_length)

# # Wywołanie
# for contact in sorted_contacts:
#   print(f"Label length: {contact.label_length}")
#   # print(f"Private number: {contact.is_private_number()}")
#   contact.contact()
#   print("------")
