import base64
import json


class EncoderDecoder:
    def __init__(self, salt_key, salt_index, payload=None, encoded_payload=None) -> None:
        self.payload = payload
        self.salt_key = salt_key
        self.salt_index = salt_index
        self.encoded_payload = encoded_payload

    def encode_with_salt(self):
        payload_str = json.dumps(self.payload)

        if self.salt_index < 0 or self.salt_index > len(payload_str):
            raise ValueError("Invalid salt index")

        salted_payload = payload_str[:self.salt_index] + self.salt_key + payload_str[self.salt_index:]
        encoded_payload = base64.b64encode(salted_payload.encode()).decode()

        return encoded_payload

    def decode_with_salt(self):
        decoded_payload = base64.b64decode(self.encoded_payload).decode()

        if decoded_payload[self.salt_index:self.salt_index+len(self.salt_key)] != self.salt_key:
            raise ValueError("Incorrect salt key or salt index")

        original_payload_str = decoded_payload[:self.salt_index] + decoded_payload[self.salt_index+len(self.salt_key):]
        original_payload = json.loads(original_payload_str)

        return original_payload
