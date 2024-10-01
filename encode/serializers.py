from rest_framework import serializers


class EncodeSerializer(serializers.Serializer):
    payload = serializers.CharField()
    salt_key = serializers.CharField()
    salt_index = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class EncodedResponseSerializer(serializers.Serializer):
    encoded_data = serializers.CharField()


class DecodeSerializer(serializers.Serializer):
    encoded_payload = serializers.CharField()
    salt_key = serializers.CharField()
    salt_index = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class DecodedResponseSerializer(serializers.Serializer):
    decoded_data = serializers.CharField()
