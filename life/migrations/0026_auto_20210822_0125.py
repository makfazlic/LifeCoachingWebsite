# Generated by Django 3.2.6 on 2021-08-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0025_auto_20210822_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configure',
            name='slideshow_subtitle_1',
            field=models.CharField(default='Demand more from yourself than anyone else could ever expect.', help_text='Slideshow Subheading description', max_length=100),
        ),
        migrations.AlterField(
            model_name='configure',
            name='slideshow_title_1',
            field=models.CharField(default='- Tony Robbins', help_text='Slideshow Heading description', max_length=50),
        ),
    ]
