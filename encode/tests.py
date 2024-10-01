import json
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class Encodetest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.data = {
                "payload": "test encoding payload",
                "salt_key": "secret key",
                "salt_index": 7,
            }

        self.encode_url = "/api/encode/"

    def test_encode_success(self):
        response = self.client.post(self.encode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data['encoded_data'], str)

    def test_encode_wrong_salt_index(self):
        data = self.data
        data['salt_index'] = -7

        response = self.client.post(self.encode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Invalid salt index")

    def test_encode_without_salt_key(self):
        data = self.data
        data.pop('salt_key')

        response = self.client.post(self.encode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data['salt_key'])

    def test_encode_without_salt_index(self):
        data = self.data
        data.pop('salt_index')

        response = self.client.post(self.encode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data['salt_index'])

    def test_encode_without_payload(self):
        data = self.data
        data.pop('payload')

        response = self.client.post(self.encode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data['payload'])


class Decodetest(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.data = {
                "salt_key": "secret key",
                "salt_index": 7,
            }

        self.encode_url = "/api/encode/"
        self.decode_url = "/api/decode/"

    def encode_payload_setup(self):
        data = self.data
        data["payload"] = "test encoding payload"
        response = self.client.post(self.encode_url, json.dumps(data), content_type='application/json')
        encoded_data = response.data['encoded_data']
        return encoded_data

    def test_decode_success(self):
        data = self.data
        encoded_data = self.encode_payload_setup()
        data['encoded_payload'] = encoded_data

        response = self.client.post(self.decode_url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data['decoded_data'], str)

    def test_decode_wrong_salt_index(self):
        data = self.data
        encoded_data = self.encode_payload_setup()
        data['encoded_payload'] = encoded_data

        data['salt_index'] = -7

        response = self.client.post(self.decode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], "Incorrect salt key or salt index")

    def test_decode_without_salt_key(self):
        data = self.data
        encoded_data = self.encode_payload_setup()
        data['encoded_payload'] = encoded_data
        data.pop('salt_key')

        response = self.client.post(self.decode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data['salt_key'])

    def test_decode_without_salt_index(self):
        data = self.data
        encoded_data = self.encode_payload_setup()
        data['encoded_payload'] = encoded_data
        data.pop('salt_index')

        response = self.client.post(self.decode_url, json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This field is required.", response.data['salt_index'])
