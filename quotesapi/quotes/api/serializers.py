from rest_framework import serializers

from quotes.models import Quote, Comment

class CommentSerializer(serializers.ModelSerializer):

    comment_author = serializers.StringRelatedField(read_only=True)

    class Meta: 
        model = Comment
        exclude = ("quote",)

class QuoteSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many=True,
                                read_only=True)
    
    class Meta:
        model = Quote
        fields = '__all__'