from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from access.services import auth_service
from main.mixins.views import APIResponse
from ticket.services import ticket_service
from access.services import profile_service
from main.mixins.exceptions import BadRequestError

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

        user_image = payload.get('image', None)

        """ 
        Todo: The create ticket should only work for USER911, 
        if any other usertype tries to hit the API, there should be error
        """
        ticket_service.create_ticket(
            report=report,
            location=location,
            user=user,
            user_image=user_image
        )

        return self.get_success_response(json_response={'ticket_created': True})


class GetTicketHistoryView(APIView, APIResponse):
    """Get history of a ticker"""

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = request.user
        
        history = ticket_service.get_ticket_history(
            user=user
        )

        return self.get_success_response(json_response={'ticket_history': history})


class AssignDispatchCenterView(APIView, APIResponse):
    """Assign Disptach center to a ticket"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        # user = request.user

        payload: dict = request.data

        # Extract email of dispatch center
        # Todo: Add the validation that the email should belong to a disptach center only.
        email = payload.get('email', None)

        if not email:
            raise BadRequestError('invalid params')
        
        ticket_id = payload.get('ticket_id', None)
        if not ticket_id:
            raise BadRequestError('invalid params')

        dispatch_center_user = profile_service.get_user(email=email)
        # Todo: Add the validation later that only a firefighter
        # can assign a disptach center to a ticket
        ticket_service.update_disptach_center(
            ticket_id=ticket_id,
            user=dispatch_center_user
        )

        return self.get_success_response(json_response={'disptach_center_assigned': True})


class UpdateStatusView(APIView, APIResponse):
    """Assign Disptach center to a ticket"""

    permission_classes = (IsAuthenticated,)

    def post(self, request):

        # user = request.user

        payload: dict = request.data

        # Extract email of dispatch center
        # Todo: Certain status should be changed by certain type of users only.
        status = payload.get('status', None)
        if not status:
            raise BadRequestError('invalid params')

        ticket_id = payload.get('ticket_id', None)
        if not ticket_id:
            raise BadRequestError('invalid params')

        # dispatch_center_user = profile_service.get_user(email=email)
        # Todo: Add the validation later that only a firefighter
        # can assign a disptach center to a ticket
        ticket_service.update_status(
            ticket_id=ticket_id,
            status=status
        )

        return self.get_success_response(json_response={'status_changed': True})
