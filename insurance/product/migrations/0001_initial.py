# Generated by Django 2.1.4 on 2018-12-08 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskTypeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('field_type', models.CharField(choices=[('text', 'A short text string'), ('number', 'A number'), ('date', 'A date'), ('enum', 'A choice in a list')], max_length=10)),
                ('required', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='risktypefield',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.RiskType'),
        ),
    ]
