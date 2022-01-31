from stripe.api_resources.abstract import ListableAPIResource


class PromotionCode(ListableAPIResource):
    OBJECT_NAME = 'promotion_code'

    @classmethod
    def class_url(cls):
        return '/v1/promotion_codes'


    