from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='test', activity_type='run', duration=10, team='Test Team')
        self.assertEqual(activity.user, 'test')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='test', team='Test Team', points=5)
        self.assertEqual(lb.points, 5)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test', description='desc', suggested_for='Test Team')
        self.assertEqual(workout.name, 'Test')
