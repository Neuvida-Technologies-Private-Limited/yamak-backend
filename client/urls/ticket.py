from django.urls import path

from client.views import ticket

API_MODULE = 'ticket'

urlpatterns = [
    # Access views
    path(f'{API_MODULE}/create_ticket', ticket.CreateTicketView.as_view(), name='create_ticket'),
    path(f'{API_MODULE}/get_ticket_history', ticket.GetTicketHistoryView.as_view(), name='get_ticket_history'),
    path(f'{API_MODULE}/assign-dispatch-center', ticket.AssignDispatchCenterView.as_view(), name='assign-dispatch-center'),
    path(f'{API_MODULE}/update-ticket-status', ticket.UpdateStatusView.as_view(), name='update-ticket-status')
]
