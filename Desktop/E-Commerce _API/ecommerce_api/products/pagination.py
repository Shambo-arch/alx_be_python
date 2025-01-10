from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 2 # Number of products per page
    page_size_query_param = 'page_size'  # Allow clients to specify the page size via a query parameter
    max_page_size = 100  # Maximum number of products per page
