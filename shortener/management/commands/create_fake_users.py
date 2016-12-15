from django.core.management import BaseCommand

from utils.users import FakeUserGenerator


class Command(BaseCommand):
    """Create a number of random users given by the parameter <users>"""
    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument(
            'users',
            help='Number of users to add',
            type=int,
            nargs=1,
        )

    def handle(self, *args, **options):
        generator = FakeUserGenerator(options['users'][0])
        generator.create_users()
