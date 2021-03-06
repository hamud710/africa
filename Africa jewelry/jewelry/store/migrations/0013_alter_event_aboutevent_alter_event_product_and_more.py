# Generated by Django 4.0.2 on 2022-02-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_event_user_event_aboutevent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='aboutEvent',
            field=models.CharField(choices=[('discount', 'discount'), ('announcement', 'announcement'), ('aboutUS', 'aboutUS')], default='discount', max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='product',
            field=models.ForeignKey(blank=True, help_text='If you choose discount on Event', null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for Shipping', 'Out for Shipping'), ('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
    ]
