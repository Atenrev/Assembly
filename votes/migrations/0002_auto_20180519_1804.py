# Generated by Django 2.0.5 on 2018-05-19 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0001_initial'),
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommentVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserProposalPhaseVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.BooleanField(default=True)),
                ('unique_id', models.CharField(max_length=200)),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Phase')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='citizens.Profile'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='citizens.Profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AddField(
            model_name='userproposalphasevote',
            name='proposal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Proposal'),
        ),
        migrations.AddField(
            model_name='userproposalphasevote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizens.Profile'),
        ),
        migrations.AddField(
            model_name='usercommentvote',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Comment'),
        ),
        migrations.AddField(
            model_name='usercommentvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citizens.Profile'),
        ),
    ]
