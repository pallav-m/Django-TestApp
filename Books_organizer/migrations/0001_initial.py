# Generated by Django 5.0.3 on 2024-04-09 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default='example@example.com', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('telephone', models.CharField(max_length=100, null=True)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
                ('recommendedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', to='Books_organizer.author')),
                ('followers', models.ManyToManyField(related_name='followed_authors', related_query_name='followed_authors', to='Books_organizer.user')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('joindate', models.DateField()),
                ('popularity_score', models.IntegerField()),
                ('recommendedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Books_organizer.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='Books_organizer.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to='Books_organizer.publisher')),
            ],
        ),
    ]
