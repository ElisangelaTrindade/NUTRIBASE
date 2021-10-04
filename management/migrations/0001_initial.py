# Generated by Django 3.2.7 on 2021-10-04 14:38

import cpffield.cpffield
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField(blank=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(db_column='name_city', max_length=50)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=255)),
                ('date_of_creation', models.DateField()),
                ('amount_of_calories', models.DecimalField(decimal_places=1, help_text='gram_weight', max_digits=8)),
                ('gram_weigh', models.DecimalField(decimal_places=1, help_text='gram_weight', max_digits=8)),
            ],
            options={
                'db_table': 'diet_plan',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='type', max_length=255)),
                ('frequency', models.CharField(help_text='frequency', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obesity', models.CharField(db_column='obesity ', max_length=100)),
                ('cardiovascular_disease', models.CharField(db_column='cardiovascular_disease', max_length=100)),
                ('hypertension', models.CharField(db_column='hypertension', max_length=100)),
                ('cancer', models.CharField(db_column='cancer', max_length=100)),
                ('diabetes', models.CharField(db_column='diabetes', max_length=100)),
                ('dyslipidemia', models.CharField(db_column='dyslipidemia', max_length=100)),
            ],
            options={
                'db_table': 'family_health_history',
            },
        ),
        migrations.CreateModel(
            name='FoodConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_drink', models.CharField(db_column='soft_drink', max_length=100)),
                ('candy', models.CharField(db_column='candy', max_length=100)),
                ('deep_fried', models.CharField(db_column='deep_fried', max_length=100)),
                ('fast_food', models.CharField(db_column='fast_food', max_length=100)),
                ('processed_food', models.CharField(db_column='processed_food', max_length=100)),
                ('canned_food', models.CharField(db_column='canned', max_length=100)),
                ('fruits', models.CharField(db_column='fruits', max_length=100)),
                ('vegetables', models.CharField(db_column='vegetables', max_length=100)),
                ('others', models.CharField(db_column='others', max_length=100)),
            ],
            options={
                'db_table': 'food_consumption',
            },
        ),
        migrations.CreateModel(
            name='FoodDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(db_column='description', max_length=255)),
                ('date_of_consultation', models.DateField()),
                ('gram_weigh', models.DecimalField(decimal_places=1, help_text='gram_weight', max_digits=8)),
            ],
            options={
                'db_table': 'food_diary',
            },
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(db_column='name_group', max_length=150)),
                ('gram_weight', models.DecimalField(decimal_places=1, help_text='gram_weight', max_digits=8)),
                ('calorie', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'food_group',
            },
        ),
        migrations.CreateModel(
            name='FoodIntolerance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intolerance_description', models.CharField(db_column='description', max_length=255)),
            ],
            options={
                'db_table': 'food_intolerance',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', cpffield.cpffield.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('birthday', models.DateField()),
                ('email', models.CharField(db_column='email_patient', max_length=150)),
                ('street', models.CharField(max_length=50)),
                ('zip_code', models.CharField(default='', max_length=9)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.city')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.exercise')),
                ('family_health_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.familyhealthhistory')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='PatientHealthHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obesity', models.CharField(db_column='obesity', max_length=100)),
                ('cardiovascular_disease', models.CharField(db_column='cardiovascular_disease', max_length=100)),
                ('hypertension', models.CharField(db_column='hypertension', max_length=100)),
                ('cancer', models.CharField(db_column='cancer', max_length=100)),
                ('diabetes', models.CharField(db_column='diabetes', max_length=100)),
                ('dyslipidemia', models.CharField(db_column='dyslipidemia', max_length=100)),
                ('others', models.CharField(db_column='others', max_length=100)),
            ],
            options={
                'db_table': 'patient_health_history',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_state', models.CharField(db_column='name_state', max_length=50)),
                ('acrm_state', models.CharField(db_column='acrm_state', max_length=3)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=25)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_health_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patienthealthhistory'),
        ),
        migrations.AddField(
            model_name='patient',
            name='register_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='NutritionalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_information', models.CharField(db_column='description', max_length=255)),
                ('diet_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.dietplan')),
                ('food_consumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.foodconsumption')),
                ('food_intolerance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.foodintolerance')),
                ('food_preferences', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
            options={
                'db_table': 'nutricional_information',
            },
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_meal', models.CharField(db_column='type_meal', max_length=50)),
                ('time_meal', models.DateTimeField(auto_now_add=True, db_column='time_meal')),
                ('diet_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.dietplan')),
                ('food_diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.fooddiary')),
                ('register_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'meal',
            },
        ),
        migrations.CreateModel(
            name='FoodPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_description', models.CharField(db_column='description', max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
            options={
                'db_table': 'food_preferences',
            },
        ),
        migrations.AddField(
            model_name='foodintolerance',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient'),
        ),
        migrations.AddField(
            model_name='fooddiary',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient'),
        ),
        migrations.AddField(
            model_name='fooddiary',
            name='register_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='foodconsumption',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient'),
        ),
        migrations.AddField(
            model_name='foodconsumption',
            name='register_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(db_column='food_name', max_length=50)),
                ('gram_weigh', models.DecimalField(decimal_places=1, help_text='gram_weight', max_digits=8)),
                ('diet_plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.dietplan')),
                ('food_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.foodgroup')),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_exam', models.CharField(db_column='description', max_length=100)),
                ('lab_reference_values', models.DecimalField(decimal_places=2, help_text='lab_reference_value', max_digits=6)),
                ('lab_value_found', models.DecimalField(decimal_places=2, help_text='ab_value_found', max_digits=6)),
                ('additional_information', models.CharField(db_column='dditional_information', max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
                ('register_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField(db_column='hire_date')),
                ('type', models.CharField(db_column='type', max_length=50)),
                ('cpf', cpffield.cpffield.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('birthday', models.DateField()),
                ('email', models.CharField(db_column='email_patient', max_length=150)),
                ('street', models.CharField(db_column='street', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=9)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.city')),
                ('register_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AddField(
            model_name='dietplan',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient'),
        ),
        migrations.AddField(
            model_name='dietplan',
            name='register_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.state'),
        ),
        migrations.CreateModel(
            name='AntopometricEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, help_text='weight', max_digits=6)),
                ('height', models.CharField(max_length=4)),
                ('BMI', models.DecimalField(decimal_places=2, help_text='bmi', max_digits=4)),
                ('arm_circumference', models.DecimalField(decimal_places=2, help_text='arm_circumference', max_digits=4)),
                ('abdomen_circumference', models.DecimalField(decimal_places=2, help_text='abdomen_circumference', max_digits=4)),
                ('wrist_circumference', models.DecimalField(decimal_places=2, help_text='wrist_circumference', max_digits=4)),
                ('others', models.CharField(db_column='description', max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
                ('register_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'antopometric_evaluation',
            },
        ),
    ]
