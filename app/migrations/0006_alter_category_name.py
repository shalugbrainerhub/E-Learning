# Generated by Django 4.2.4 on 2023-09-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('science', 'Science'), ('math', 'Math'), ('langauge', 'Language'), ('computer', 'Computer'), ('electronics', 'Electronics')], default='computer', max_length=100),
        ),
    ]
