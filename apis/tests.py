from django.test import TestCase


class HomePageTests(TestCase):

    def test_status_code_correct(self):
        response = self.client.get('/weather?current_location=-33.927407,18.415747&booking_location=-32.927407,19.415747')
        self.assertEquals(response.status_code, 200)

    def test_status_code_error(self):
        response = self.client.get('/weather?current_location=-sdfsdfsdf&booking_location=-32.927407,19.415747')
        self.assertEquals(response.status_code, 400)

    def test_data_format(self):
        response = self.client.get('/weather?current_location=-33.927407,18.415747&booking_location=-32.927407,19.415747')
        self.assertEquals(type(response.json()['current_location']['temperature']), float)
