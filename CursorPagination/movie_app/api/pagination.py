from rest_framework.pagination import CursorPagination

class MovieListPagination(CursorPagination):
    page_size=1
    ordering=['avg_rating','id']
    cursor_query_param='record'

class StreamListPagination(CursorPagination):
    page_size=1
    ordering=['name','id']
    cursor_query_param='record'

class ReviewListPagination(CursorPagination):
    page_size=1
    ordering=['movie','id']
    cursor_query_param='record'