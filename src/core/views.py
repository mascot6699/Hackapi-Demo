
from . import models, serializers, utils

from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions



class Process(APIView):
    """
    These apis are for general purpose
    """

    def get(self, request, format=None):
        """
        GET api for getting particular template from id

        SmsSid	string, unique identifier of that SMS
        From	string, the number of the sender
        To	string, your Exotel Company number where the SMS was received
        Date	string, Time when the SMS reached Exotel's servers
        Body	string, the contents of the SMS
        """
        print  request.data["body"]
        # print  request.data[1]

        keyword =  request.data["body"]
        # if keyword=="wiki":
        body = utils.process_wiki(keyword)
        # elif keyword=="dictionary":
        #     body = utils.process_dictionary(request.data[1])
        return Response({"body":body}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Creates a template
        """
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        """
        To change name of the template and its type
        """
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
