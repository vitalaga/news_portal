from django.core.management.base import BaseCommand, CommandError
from news_portal.models import Post, Category


class Command(BaseCommand):
    help = "Удаляет статьи в выбранной категории"

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f"Вы действительно хотите удалить все статьи в категории {options['category']}? yes/no")

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Команда отменена'))
            return
        try:
            category = Category.objects.get(name_category=options['category'])
            Post.objects.filter(categories=category).delete()
            self.stdout.write(self.style.SUCCESS(f"Succesfully deleted all news from {category.name_category}"))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {options["category"]}'))
