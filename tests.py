# Tests for the program
# by Mark Edmunds
#
#
#
from faker import Faker
import input_vailidator as check
# initialize faker
fake = Faker()
# test data
emails = []
phone_numbers = []
names = []
# data generation
for i in range(10):
    names.append(fake.first_name())
    emails.append(fake.email())
    phone_numbers.append(fake.phone_number())

# tests


def test_validate_name_input ():
    for name in names:
        assert check.validate_name_input(name) is not None


def test_validate_email_input ():
    for email in emails:
        assert check.validate_email_input(email) is not None


def test_validate_phone_input ():
    for phone_number in phone_numbers:
        assert check.validate_phone_input(phone_number) is not None
