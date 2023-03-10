# Generated by Django 4.1.6 on 2023-02-10 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0002_quote_quote_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='quote_author',
        ),
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='quotes.quote')),
            ],
        ),
    ]
