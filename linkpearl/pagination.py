from rest_framework import pagination

class PageNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'per_page'

class UnlimitedPageNumberPagination(pagination.PageNumberPagination):
    page_size = 99999
