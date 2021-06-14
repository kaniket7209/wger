# Generated by Django 3.2.3 on 2021-06-13 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0014_historicalexercise_historicalexercisebase_historicalexercisecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisecomment',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='exercises.exercise',
                                    verbose_name='Exercise'),
        ),
        migrations.AlterField(
            model_name='historicalexercise',
            name='license_author',
            field=models.CharField(blank=True,
                                   help_text='If you are not the author, enter the name or source '
                                             'here. This is needed for some licenses e.g. the '
                                             'CC-BY-SA.',
                                   max_length=50, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='historicalexercisecomment',
            name='exercise',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='+', to='exercises.exercise',
                                    verbose_name='Exercise'),
        ),
        migrations.CreateModel(
            name='HistoricalExerciseAlias',
            fields=[
                ('id', models.IntegerField(auto_created=True,
                                           blank=True,
                                           db_index=True,
                                           verbose_name='ID')),
                ('alias', models.CharField(max_length=200,
                                           verbose_name='Alias for an exercise')),
                ('history_id', models.AutoField(primary_key=True,
                                                serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type',
                 models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')],
                                  max_length=1)),
                ('exercise', models.ForeignKey(blank=True, db_constraint=False, null=True,
                                               on_delete=django.db.models.deletion.DO_NOTHING,
                                               related_name='+', to='exercises.exercise',
                                               verbose_name='Exercise')),
                ('history_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                   related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical exercise alias',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ExerciseAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('alias', models.CharField(max_length=200, verbose_name='Alias for an exercise')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               to='exercises.exercise', verbose_name='Exercise')),
            ],
        ),
    ]