from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_user_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(email='test@test.com', username='testuser', team=team)
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.team.name, 'TestTeam')

    def test_activity_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(email='test@test.com', username='testuser', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 10)

    def test_workout_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(email='test@test.com', username='testuser', team=team)
        workout = Workout.objects.create(user=user, description='Pushups')
        self.assertEqual(workout.description, 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='TestTeam')
        user = User.objects.create_user(email='test@test.com', username='testuser', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=50)
        self.assertEqual(leaderboard.points, 50)
