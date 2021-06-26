# Generated by Django 3.1.4 on 2021-06-26 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='view_fee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_image', models.ImageField(upload_to='media/properties')),
                ('back_image', models.ImageField(upload_to='media/properties')),
                ('side_image', models.ImageField(upload_to='media/properties')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
            ],
        ),
    ]
