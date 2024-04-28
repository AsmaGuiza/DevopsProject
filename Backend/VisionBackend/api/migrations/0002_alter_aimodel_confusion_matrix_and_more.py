# Generated by Django 4.2 on 2024-04-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='confusion_matrix',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='train_validation_acc',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='train_validation_loss',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
