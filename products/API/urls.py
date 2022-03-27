from django.urls import path
from .views import *

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='category'),

    path('books', ListBooks.as_view(), name='books'),
    path('books/<int:pk>/', DetailBooks.as_view(), name='book'),

    path('headphones', ListHeadphones.as_view(), name='headphones'),
    path('headphones/<int:pk>/', DetailHeadphones.as_view(), name='headphone'),
]
