# Generated by Django 3.2.6 on 2021-08-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0011_alter_configure_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='configure',
            name='slideshow_background_1',
            field=models.ImageField(default='road.jpg', help_text='Please submit a darkened slideshow background - 1920x1080 minimum', upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_background_3',
            field=models.ImageField(default='road.jpg', help_text='Please submit a darkened slideshow background - 1920x1080 minimum', upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_subtitle_1',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor', help_text='Slideshow Subheading description', max_length=100),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_subtitle_2',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor', help_text='Slideshow Subheading description', max_length=100),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_subtitle_3',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor', help_text='Slideshow Subheading description', max_length=100),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_title_1',
            field=models.CharField(default='SS1', help_text='Slideshow Heading description', max_length=50),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_title_2',
            field=models.CharField(default='SS1', help_text='Slideshow Heading description', max_length=50),
        ),
        migrations.AddField(
            model_name='configure',
            name='slideshow_title_3',
            field=models.CharField(default='SS1', help_text='Slideshow Heading description', max_length=50),
        ),
    ]
