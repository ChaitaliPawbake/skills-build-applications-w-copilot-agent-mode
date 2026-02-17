
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().exclude(is_superuser=True).delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': 'Marvel'},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(username=u['username'], email=u['email'], password='password')

        # Activities
        Activity.objects.create(user='ironman', activity_type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='batman', activity_type='Cycling', duration=45, team='DC')

        # Leaderboard
        Leaderboard.objects.create(user='ironman', team='Marvel', points=100)
        Leaderboard.objects.create(user='batman', team='DC', points=90)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Stealth Training', description='Stealth and agility', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))

        # Create unique index on email for users collection
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({ "email": 1 }, { unique: true })')
