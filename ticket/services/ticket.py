from access.models import User
from access.models import UserTypes
from ticket.models import Ticket
from access.services import profile_service
import base64

def create_ticket(report, location, user: User, user_image) -> Ticket:

    ticket = Ticket.objects.create(report=report, location=location, user=user, user_image=user_image)

    if not ticket:
        Exception("Couldn't create ticket")
    
    return ticket

def update_disptach_center(
            ticket_id: str,
            user: User
        ) -> None:
    
    # Fetch the ticket
    ticket = Ticket.objects.filter(ticket_id=ticket_id).last()

    # Update the dispatch center of the ticket
    ticket.disptach_center = user

    # Save the ticket
    ticket.save()

    return

def get_ticket_history(user: User) -> list:

    user_type = profile_service.get_user_profile(user).get('user_type')

    # If the user is firefighter return all the tickets
    if user_type == UserTypes.FIREFIGHTER:
        ticket = list(Ticket.objects.filter().values(
            'report',
            'location',
            'status',
            'user_image',
            'created_at',
            'modified_at',
            'disptach_center',
            'ticket_id'
        ))
    elif user_type == UserTypes.DISPATCH_CENTER:
        ticket = list(Ticket.objects.filter(disptach_center_id=user).values(
            'report',
            'location',
            'status',
            'user_image',
            'created_at',
            'modified_at',
            'disptach_center',
            'ticket_id'
        ))        
    else:
        ticket = list(Ticket.objects.filter(user=user).values(
            'report',
            'location',
            'status',
            'user_image',
            'created_at',
            'modified_at',
            'disptach_center',
            'ticket_id'
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