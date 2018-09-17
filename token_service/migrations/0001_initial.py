# Generated by Django 2.1.1 on 2018-09-14 01:55

from django.db import migrations, models
import django.db.models.deletion
import token_service.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API_key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_hash', models.CharField(max_length=256)),
                ('owner', token_service.models.EncryptedTextField()),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OIDCMetadataCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('retrieval_time', models.DateTimeField(auto_now_add=True)),
                ('provider', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='PendingCallback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=256)),
                ('state', token_service.models.EncryptedTextField()),
                ('nonce', token_service.models.EncryptedTextField()),
                ('provider', models.CharField(max_length=256)),
                ('url', token_service.models.EncryptedTextField()),
                ('return_to', token_service.models.EncryptedTextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', token_service.models.EncryptedTextField()),
                ('refresh_token', token_service.models.EncryptedTextField()),
                ('expires', models.DateTimeField()),
                ('provider', models.CharField(max_length=256)),
                ('issuer', models.CharField(max_length=256)),
                ('enabled', models.BooleanField(default=True)),
                ('access_token_hash', models.TextField()),
                ('nonce', models.ManyToManyField(to='token_service.Nonce')),
                ('scopes', models.ManyToManyField(to='token_service.Scope')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=256, unique=True)),
                ('name', token_service.models.EncryptedTextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_key',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('key_hash', models.CharField(max_length=256)),
                ('label', models.CharField(blank=True, max_length=256, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='token_service.User')),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='token_service.User'),
        ),
        migrations.AddField(
            model_name='pendingcallback',
            name='scopes',
            field=models.ManyToManyField(to='token_service.Scope'),
        ),
    ]
