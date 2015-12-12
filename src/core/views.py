
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

        parsed_content = request.query_params.get("Body").split(' ')
        # garbage = parsed_content[0].lower()
        keyword= parsed_content[1].lower()
        body = (" ".join(parsed_content[2:])).lower()
        print body, keyword
        if keyword=="hello":
            body = utils.get_help()
        if keyword=="wiki":
            body = utils.process_wiki(body)
        elif keyword=="dictionary":
            body = utils.process_dictionary(body)
        elif keyword=="email":
            body = utils.custom_send_email(body)
        elif keyword=="song":
            body = utils.custom_send_email(body)
        return Response(body, status=status.HTTP_200_OK, content_type="text/plain")


