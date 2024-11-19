from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import print_message

class PrintView(APIView):
    def get(self, request):
        printer_name = 'EPSON TM-m30 Receipt5'
        message = "hai\n"
        success, error_message = print_message(printer_name, message)
        if success:
            return Response({"status": "success", "message": "Message sent to printer successfully."})
        else:
            return Response({"status": "error", "message": f"Failed to send message to printer. Error: {error_message}"})
