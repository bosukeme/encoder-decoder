from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import EncodeSerializer, DecodeSerializer, EncodedResponseSerializer, DecodedResponseSerializer
from .services import EncoderDecoder


@extend_schema(
    tags=["Encode"],
    responses={status.HTTP_201_CREATED: EncodedResponseSerializer},
)
class EncodeView(generics.CreateAPIView):
    serializer_class = EncodeSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        values = serializer.save()
        try:
            encoded_data = EncoderDecoder(**values).encode_with_salt()
            response_data = {'encoded_data': encoded_data}

            response_serializer = EncodedResponseSerializer(data=response_data)
            response_serializer.is_valid(raise_exception=True)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=["Decode"],
    responses={status.HTTP_201_CREATED: DecodedResponseSerializer},
)
class DecodeView(generics.CreateAPIView):
    serializer_class = DecodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        values = serializer.save()

        try:
            decoded_data = EncoderDecoder(**values).decode_with_salt()
            response_data = {'decoded_data': decoded_data}

            response_serializer = DecodedResponseSerializer(data=response_data)
            response_serializer.is_valid(raise_exception=True)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
