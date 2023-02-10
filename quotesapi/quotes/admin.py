from django.contrib import admin

from quotes.models import Quote, Comment

admin.site.register(Quote)
admin.site.register(Comment)