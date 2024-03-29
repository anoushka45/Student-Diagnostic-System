# Generated by Django 4.1.7 on 2023-03-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_questions_delete_teachdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=100)),
                ("qno", models.IntegerField()),
                ("datee", models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name="questions",
            name="op1",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="questions",
            name="op2",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="questions",
            name="op3",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="questions",
            name="op4",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="questions",
            name="question",
            field=models.CharField(max_length=1000),
        ),
    ]
