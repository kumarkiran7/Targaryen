# Generated by Django 4.2.1 on 2023-06-07 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Id', models.CharField(max_length=10, unique=True)),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=254, null=True, unique=True)),
                ('First_Name', models.CharField(max_length=100, null=True)),
                ('Last_Name', models.CharField(max_length=100, null=True)),
                ('Father_Name', models.CharField(max_length=100)),
                ('Mother_Name', models.CharField(max_length=100)),
                ('Dob', models.DateField(null=True)),
                ('Blood_Group', models.CharField(max_length=25, null=True)),
                ('Contact_Number', models.CharField(max_length=10, unique=True)),
                ('Emergency_Number', models.CharField(max_length=10)),
                ('Present_Address', models.CharField(max_length=100)),
                ('Permanent_Address', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employment_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_Id', models.CharField(max_length=10, unique=True)),
                ('Previous_CompanyName', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Date_of_Employment', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=100)),
                ('Achievements', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='App.employee_details')),
            ],
        ),
        migrations.CreateModel(
            name='Salary_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.employment_history')),
            ],
        ),
    ]