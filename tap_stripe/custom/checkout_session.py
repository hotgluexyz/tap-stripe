from stripe.api_resources.abstract import ListableAPIResource


class CheckoutSession(ListableAPIResource):
    OBJECT_NAME = 'checkout_session'

    @classmethod
    def class_url(cls):
        return '/v1/checkout/sessions'
