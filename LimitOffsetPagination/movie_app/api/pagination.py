from rest_framework.pagination import LimitOffsetPagination

class MovieListPagination(LimitOffsetPagination):
    default_limit=1
    max_limit=5
    limit_query_param='limit'
    offset_query_param='start'

class StreamListPagination(LimitOffsetPagination):
    default_limit=1
    max_limit=5
    limit_query_param='limit'
    offset_query_param='start'

class ReviewListPagination(LimitOffsetPagination):
    default_limit=1
    max_limit=5
    limit_query_param='limit'
    offset_query_param='start'