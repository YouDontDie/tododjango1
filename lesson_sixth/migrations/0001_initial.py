# Generated by Django 2.2.2 on 2019-06-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth', models.DateField()),
                ('company', models.CharField(choices=[('google', 'Google'), ('yandex', 'Yandex'), ('itvdn', 'Itvdn'), ('epam', 'Epam')], max_length=150)),
                ('position', models.CharField(choices=[('senior', 'Senior'), ('middle', 'Middle'), ('junior', 'Junior')], max_length=15)),
                ('language', models.CharField(choices=[('python', 'Python'), ('javascript', 'Javascript'), ('c#', 'C#'), ('cpp', 'C++')], default='python', max_length=10)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
