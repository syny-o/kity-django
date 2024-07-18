# Generated by Django 5.0.6 on 2024-07-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('P', 'Portrait'), ('L', 'Landscape')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='wedding_photos/')),
            ],
            options={
                'ordering': ['-type', 'order'],
                'abstract': False,
            },
        ),
    ]
