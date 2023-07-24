from access.models import User
from ticket.models import Ticket

def create_ticket(report, location, user: User) -> Ticket:

    ticket = Ticket.objects.create(report=report, location=location, user=user)

    if not ticket:
        Exception("Couldn't create ticket")
    
    return ticket

    
def get_ticket_history(user: User) -> list:

    ticket = list(Ticket.objects.filter(user=user).values(
        'report',
        'location',
        'status',
        'created_at',
        'modified_at'
    ))

    if not ticket:
        Exception("Couldn't create ticket")
    
    return ticket