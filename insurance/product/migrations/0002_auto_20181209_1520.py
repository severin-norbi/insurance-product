# Generated by Django 2.1.4 on 2018-12-09 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnumOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='risktypefield',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_fields', to='product.RiskType'),
        ),
        migrations.AddField(
            model_name='enumoption',
            name='enum_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='product.RiskTypeField'),
        ),
    ]
