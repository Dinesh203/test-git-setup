# Generated by Django 3.2 on 2021-11-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(default='', upload_to='images')),
                ('added_date', models.DateTimeField(default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='cat',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
