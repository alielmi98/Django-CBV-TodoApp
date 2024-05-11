from django.core.management.base import BaseCommand

from faker import Faker
import random
from datetime import datetime

from accounts.models import User, Profile
from todo.models import Task


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username=self.fake.user_name(),
            password="Test@123456",
            email=self.fake.email(),
        )
        profile = Profile.objects.get(user=user)
        profile.country = self.fake.country()
        profile.city = self.fake.city()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for _ in range(10):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                complete=random.choice([True, False]),
            )
