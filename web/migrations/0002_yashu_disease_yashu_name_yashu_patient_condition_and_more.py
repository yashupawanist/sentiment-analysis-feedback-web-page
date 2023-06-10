from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yashu',
            name='disease_effect',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AddField(
            model_name='yashu',
            name='name',
            field=models.CharField(default='NEW DEFAULT VALUE', max_length=200),  # Changed default value and max length
        ),
        migrations.AddField(
            model_name='yashu',
            name='Symptoms',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
        migrations.AddField(
            model_name='yashu',
            name='precaution/medicine',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
    ]
