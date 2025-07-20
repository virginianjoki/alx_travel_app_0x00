from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with listings data'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()

        locations = ["Nairobi", "Mombasa", "Diani", "Naivasha"]
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i+1}",
                description="A lovely place to stay.",
                location=random.choice(locations),
                price_per_night=random.uniform(50, 200),
                available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
