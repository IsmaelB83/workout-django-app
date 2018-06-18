# Generated by Django 2.0 on 2018-06-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('instructions', models.TextField(blank=True, max_length=1000)),
                ('tips', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='workout/exercises/')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rest', models.PositiveIntegerField()),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('basics', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='workout/muscles/')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('benefits', models.TextField(blank=True, max_length=1000)),
                ('basics', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to='workout/muscles/')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, max_length=1000)),
                ('recommendations', models.TextField(blank=True, max_length=1000)),
                ('motivation_quotes', models.TextField(blank=True, max_length=1000)),
                ('day_of_week', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='MO', max_length=2)),
                ('exercises', models.ManyToManyField(to='exercise.ExerciseSet')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, max_length=300)),
                ('level', models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced')], default='IN', max_length=2)),
                ('goal', models.CharField(choices=[('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining')], default='MA', max_length=2)),
                ('image', models.ImageField(upload_to='workout/routines/')),
                ('training_days', models.ManyToManyField(to='exercise.TrainingDay')),
            ],
        ),
        migrations.AddField(
            model_name='muscle',
            name='muscle_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exercise.MuscleGroup'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='primary_muscles',
            field=models.ManyToManyField(related_name='primary_muscles', to='exercise.Muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_muscles',
            field=models.ManyToManyField(blank=True, related_name='secondary_muscles', to='exercise.Muscle'),
        ),
    ]
