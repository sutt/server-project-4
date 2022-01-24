# Generated by Django 4.0.1 on 2022-01-24 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chatter.chatroom'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='user_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_one_chat_rooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='user_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_two_chat_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
