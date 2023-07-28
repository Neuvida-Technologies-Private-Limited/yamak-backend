from access.models import User
from ticket.models import Ticket
from access.services import profile_service
import base64

def create_ticket(report, location, user: User, user_image) -> Ticket:

    ticket = Ticket.objects.create(report=report, location=location, user=user, user_image=user_image)

    if not ticket:
        Exception("Couldn't create ticket")
    
    return ticket

    
def get_ticket_history(user: User) -> list:

    user_type = profile_service.check_user_type(UserTypes.)
    ticket = list(Ticket.objects.filter(user=user).values(
        'report',
        'location',
        'status',
        'user_image',
        'created_at',
        'modified_at'
    ))

    ticket_copy = ticket

    for index, value in enumerate(ticket_copy):
        image_path = value.get('user_image', None)
        if len(image_path):
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            ticket[index]["user_image"] = image_data
            # Todo: Add exception handling here
    if not ticket:
        Exception("Couldn't create ticket")
    
    return ticket