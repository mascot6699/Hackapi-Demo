
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
        # print  request.data["body"]
        # print  request.data[1]

        # keyword =  request.data["body"]
        parsed_content = request.query_params.get("Body").split(' ')
        keyword= parsed_content[0]
        body = " ".join(parsed_content[1:])
        print body, keyword
        if keyword=="wiki":
            body = utils.process_wiki(body)
        elif keyword=="dictionary":
            body = utils.process_dictionary(body)
        return Response(body, status=status.HTTP_200_OK, content_type="text/plain")


