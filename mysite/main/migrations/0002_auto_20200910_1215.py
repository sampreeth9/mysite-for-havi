# Generated by Django 3.1 on 2020-09-10 06:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(default='NEW COUNTRY', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(default='NEW DISTRICT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(default='NEW LOCATION', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mandal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandal_name', models.CharField(default='NEW MANDAL', max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.district')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(default='NEW STATE', max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.country')),
            ],
        ),
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='temporary', max_length=100)),
                ('last_name', models.CharField(default='temporary', max_length=100)),
                ('user_name', models.CharField(default='temporary', max_length=100)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('date_of_birth', models.DateField(null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
                ('date_of_account_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('bio', models.TextField(null=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
        migrations.AddField(
            model_name='location',
            name='mandal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.mandal'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.state'),
        ),
    ]
