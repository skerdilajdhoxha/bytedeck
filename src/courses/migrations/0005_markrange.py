# Generated by Django 2.0.13 on 2019-08-15 20:25

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_coursestudent_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('minimum_mark', models.IntegerField(default=0, help_text='Minimum mark as a percentage from 0 to 100 (or higher)')),
                ('active', models.BooleanField(default=True)),
                ('color', models.CharField(default='blue', help_text='An HTML color name or hax color value to represent this range', max_length=20)),
                ('days', models.CharField(default='1,2,3,4,5,6,7', help_text='Comma seperated list of weekdays that this range is active, with Sun=1 eg: "2,4,6" for M, W, F.', max_length=13, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('courses', models.ManyToManyField(blank=True, help_text='Which courses this field is relevant to; blank means all courses.', to='courses.Course')),
            ],
        ),
    ]
