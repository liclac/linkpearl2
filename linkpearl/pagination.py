from rest_framework import pagination

class UnlimitedPageNumberPagination(pagination.PageNumberPagination):
    page_size = 99999
