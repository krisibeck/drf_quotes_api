from django.shortcuts import render

from rest_framework import generics

from quotes.models import Quote, Comment
from quotes.api.serializers import QuoteSerializer, CommentSerializer
from quotes.api.pagination import SmallSetPagination
from quotes.api.persmissions import IsAdminOrReadOnly, IsCommentAuthorOrReadOnly

class QuotesCreateAPIView(generics.ListCreateAPIView):

    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
    pagination_class = SmallSetPagination
    permission_classes = [IsAdminOrReadOnly]

class QuotesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminOrReadOnly]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrReadOnly]

    def perform_create(self, serializer):
        quote_pk = self.kwargs.get('quote_pk')
        quote = generics.get_object_or_404(Quote, pk=quote_pk)

        comment_author = self.request.user

        serializer.save(quote=quote, comment_author=comment_author)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = QuoteSerializer