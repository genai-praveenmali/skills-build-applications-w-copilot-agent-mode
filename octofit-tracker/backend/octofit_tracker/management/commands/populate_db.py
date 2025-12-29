from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete individually to avoid ObjectId unhashable error)
        for obj in Leaderboard.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Activity.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Workout.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in User.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()
        for obj in Team.objects.all():
            if getattr(obj, 'id', None):
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        hulk = User.objects.create(name='Hulk', email='hulk@marvel.com', team=marvel)
        thor = User.objects.create(name='Thor', email='thor@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=hulk, type='Swimming', duration=45, date=timezone.now().date())
        Activity.objects.create(user=thor, type='Cycling', duration=60, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Martial Arts', duration=50, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Flying', duration=120, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, type='Lasso Practice', duration=40, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        w2 = Workout.objects.create(name='Situps', description='Do 30 situps')
        w1.suggested_for.set([ironman, batman])
        w2.suggested_for.set([hulk, superman])

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)
        Leaderboard.objects.create(user=superman, score=110)
        Leaderboard.objects.create(user=thor, score=80)
        Leaderboard.objects.create(user=wonderwoman, score=95)
        Leaderboard.objects.create(user=hulk, score=85)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
