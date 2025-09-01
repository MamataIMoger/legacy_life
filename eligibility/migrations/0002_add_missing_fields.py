from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('eligibility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eligibilitycheck',
            name='selected_hospital',
            field=models.ForeignKey(
                to='eligibility.Hospital',
                on_delete=django.db.models.deletion.SET_NULL,
                null=True,
                blank=True
            ),
        ),
        migrations.AddField(
            model_name='eligibilitycheck',
            name='transplant_type',
            field=models.CharField(
                max_length=100,
                null=True,
                blank=True
            ),
        ),
    ]
