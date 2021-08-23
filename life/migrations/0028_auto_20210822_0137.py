# Generated by Django 3.2.6 on 2021-08-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0027_alter_configure_block_image_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configure',
            name='block_image_3',
            field=models.ImageField(default='pics/calendar.jpg', help_text='Please submit a block image - 500x500px preferably', upload_to='pics/'),
        ),
        migrations.AlterField(
            model_name='configure',
            name='block_title_black_3',
            field=models.CharField(default='Want to talk?', help_text='Enter black block title', max_length=100),
        ),
        migrations.AlterField(
            model_name='configure',
            name='block_title_silver_3',
            field=models.CharField(default='This is how I work.', help_text='Enter silver block title', max_length=100),
        ),
    ]
