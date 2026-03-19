from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("netbox_acls", "0013_acl_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="aclextendedrule",
            name="log_option",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
