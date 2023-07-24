from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from access.services import auth_service
from main.mixins.views import APIResponse
from ticket.services import ticket_service


class CreateTicketView(APIView, APIResponse):
    """Create ticket for user"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        payload: dict = request.data

        user = request.user
        
        report = payload.get('report', None)
        if not report:
            raise BadRequestError(message='invalid report')

        location = payload.get('location', None)
        if not location:
            raise BadRequestError(message='invalid request type')

        ticket_service.create_ticket(
            report=report,
            location=location,
            user=user
        )

        return self.get_success_response(json_response={'ticket_created': True})


class GetTicketHistoryView(APIView, APIResponse):
    """Get history of a ticker"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        payload: dict = request.data

        user = request.user
        
        history = ticket_service.get_ticket_history(
            user=user
        )

        return self.get_success_response(json_response={'ticket_history': history})
