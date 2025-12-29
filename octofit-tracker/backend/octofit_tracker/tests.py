from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Iron Man')
        self.assertEqual(self.user.email, 'ironman@marvel.com')
        self.assertEqual(self.user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='DC')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Hulk', email='hulk@marvel.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-12-29')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.user.name, 'Hulk')

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Thor', email='thor@marvel.com', team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)
        self.assertEqual(self.leaderboard.user.name, 'Thor')
