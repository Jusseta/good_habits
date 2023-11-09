from rest_framework.pagination import PageNumberPagination


class HabitsPaginator(PageNumberPagination):
    """Пагинатор для привычек"""
    page_size = 5
