from django.urls import path
from quotes.views import QuotesCreateAPIView, QuotesDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path('quotes/', QuotesCreateAPIView.as_view(), name='quotes-list'),
    path('quotes/<int:pk>/', QuotesDetailAPIView.as_view(), name='quote-detail'),
    path('quotes/<int:quote_pk>/comment', CommentListCreateAPIView.as_view(), name='quote-comment'), 
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-details')

]