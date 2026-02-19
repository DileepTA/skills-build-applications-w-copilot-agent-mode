from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', username='testuser', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2024-01-01')
        self.assertIn('run', str(activity))

    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushups')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertIn('Test Team', str(leaderboard))
