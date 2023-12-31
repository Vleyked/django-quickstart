# Generated by Django 4.2.5 on 2023-10-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart_first_step', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='anonym@email.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subscription_paid',
            field=models.BooleanField(default=False),
        ),
    ]
