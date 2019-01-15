from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Consola'

    def handle(self, *args, **options):
        import pdb;pdb.set_trace()
        print('Arrancando comando')

