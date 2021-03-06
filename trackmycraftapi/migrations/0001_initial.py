# Generated by Django 3.1.3 on 2021-03-13 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=80)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CraftUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_image_url', models.CharField(max_length=250)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='craftusers', related_query_name='craftuser', to='trackmycraftapi.craftuser')),
                ('beer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers', related_query_name='beer', to='trackmycraftapi.beer')),
            ],
        ),
        migrations.AddField(
            model_name='beer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beers', related_query_name='beer', to='trackmycraftapi.category'),
        ),
        migrations.AddField(
            model_name='beer',
            name='craftuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beers', related_query_name='beer', to='trackmycraftapi.craftuser'),
        ),
        migrations.AddField(
            model_name='beer',
            name='location',
            field=models.ManyToManyField(related_name='beer_locations', related_query_name='beer_location', to='trackmycraftapi.Location'),
        ),
        migrations.AddField(
            model_name='beer',
            name='rating',
            field=models.ManyToManyField(related_name='beer_ratings', related_query_name='beer_rating', to='trackmycraftapi.Rating'),
        ),
        migrations.AddField(
            model_name='beer',
            name='tags',
            field=models.ManyToManyField(related_name='tag_beers', related_query_name='tag_beer', to='trackmycraftapi.Tag'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ended_on', models.DateTimeField(null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_subscriptions', related_query_name='author_subscription', to='trackmycraftapi.craftuser')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_subscriptions', related_query_name='follower_subscription', to='trackmycraftapi.craftuser')),
            ],
            options={
                'unique_together': {('follower_id', 'author_id')},
            },
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackmycraftapi.reaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'reaction')},
            },
        ),
    ]
