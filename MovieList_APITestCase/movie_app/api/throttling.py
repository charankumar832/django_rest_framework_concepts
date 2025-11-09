from rest_framework.throttling import UserRateThrottle

class StreamDetailThrottle(UserRateThrottle):
    scope='stream-detail'

class ReviewDetailThrottle(UserRateThrottle):
    scope='review-detail'
