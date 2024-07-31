import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from app import create_app

class TestCustomer(unittest.TestCase):

    #stubbing do not want to do this in production.
    # def test_create_customer_stub(self):
    #     fake = Faker()
    #     name = fake.name() #Generating random data for our user's info
    #     phone = fake.phone_number()
    #     username = fake.user_name()
    #     email = fake.email()
    #     role_id = 1

    #     payload = {
    #         "name": name,
    #         "phone": phone,
    #         "email": email,
    #         "username": username,
    #         "password": fake.password(),
    #         "role_id": role_id
    #     }

    #     response = self.app.post('/customers/', json=payload)
    #     print('RESPONSE:',response)
    #     print('RESPONSE MESSAGE', response.json)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.json['name'], name)

    #setting up our test client with a mock app 'build'
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('services.customerService.save')
    def test_create_customer(self, mock_save):
        fake = Faker()
        name = fake.name() #Generating random data for our user's info
        phone = fake.phone_number()
        username = fake.user_name()
        email = fake.email()
        role_id = 1

        mock_customer = MagicMock() #Using this data to create a Mock Customer object
        mock_customer.id = 1
        mock_customer.name = name
        mock_customer.phone = phone
        mock_customer.username = username
        mock_customer.email = email
        mock_customer.role_id = 1
        mock_save.return_value = mock_customer

        payload = {
            "name": name,
            "phone": phone,
            "email": email,
            "username": username,
            "password": fake.password(),
            "role_id": role_id
        }

        response = self.app.post('/customers/', json=payload)
        print('RESPONSE:',response)
        print('RESPONSE MESSAGE', response.json)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], name)

    @patch('services.customerService.login')
    def test_login_customer(self, mock_token):
        mock_token.return_value = '1234'
        fake = Faker()

        payload = {
            'username': fake.user_name(),
            'password': fake.password()
        }

        response = self.app.post('/customers/login', json=payload)

        self.assertEqual(response.status_code, 200)

    # 


if __name__ == '__main__':
    unittest.main()