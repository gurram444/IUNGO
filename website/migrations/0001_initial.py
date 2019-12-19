# Generated by Django 2.2.7 on 2019-12-18 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, null=True, unique=True, verbose_name='Mobile phone')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('con_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True)),
                ('date_time', models.DateField(auto_now_add=True, verbose_name='Actual BRS Start Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_rating', to='website.Customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.TextField(max_length=200)),
                ('question_description', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicks', models.CharField(max_length=10, verbose_name='clicks')),
                ('date_time', models.DateField(blank=True, null=True, verbose_name='Actual BRS Start Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=250, verbose_name='Feedback')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Actual BRS Start Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_feedback', to='website.Customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_feedback', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('date_time', models.DateField(blank=True, null=True, verbose_name='Actual BRS Start Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_appointment', to='website.Customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_appointment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Customer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Questions')),
            ],
        ),
    ]
