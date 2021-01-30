# Generated by Django 3.0.3 on 2020-02-20 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0003_auto_20200110_0200'),
        ('files', '0003_auto_20200122_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='letter',
            field=models.ForeignKey(help_text='Related letter.', on_delete=django.db.models.deletion.CASCADE, related_name='attachment', to='letters.Letter', verbose_name='Letter'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(help_text='Name of file.', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(help_text='Path to file.', max_length=200, verbose_name='Path'),
        ),
    ]