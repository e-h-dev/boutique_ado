from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Wehooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self,event):
        """
        Handle all unexpected webhook events
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved: {event['type']}',
            status=200)

    def handle_payment_intent_succeeded(self,event):
        """
        Handle payment_intent_success
        """
        return HttpResponse(
            content=f'Webhook recieved: {event['type']}',
            status=200)

    def handle_payment_intent_payment_failed(self,event):
        """
        Handle payment_intent_failed
        """
        return HttpResponse(
            content=f'Webhook recieved: {event['type']}',
            status=200)



