# my_app/management/commands/import_data.py
from datetime import datetime

from django.core.management.base import BaseCommand
import os
import json
from quotes.models import Author, Quote, Tag
from django.conf import settings

class Command(BaseCommand):
    help = 'Import authors and quotes from JSON files'

    def handle(self, *args, **kwargs):
        authors_file_path = os.path.join(settings.BASE_DIR, 'import_data', 'authors.json')
        quotes_file_path = os.path.join(settings.BASE_DIR, 'import_data', 'quotes.json')

        self.import_authors(authors_file_path)
        self.import_quotes(quotes_file_path)

    def import_authors(self, authors_file_path):
        with open(authors_file_path, encoding='utf-8') as f:
            authors_data = json.load(f)

        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                fullname=author_data['fullname'],
                born_date=datetime.strptime(author_data['born_date'], '%B %d, %Y').date(),
                born_location=author_data['born_location'],
                description=author_data['description']
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully imported author {author.fullname}'))

    def import_quotes(self, quotes_file_path):
        with open(quotes_file_path, encoding='utf-8') as f:
            quotes_data = json.load(f)

        for quote_data in quotes_data:
            try:
                author = Author.objects.get(fullname=quote_data['author'])
            except Author.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f" Author '{quote_data['author']}' not found. Skipping quote: \"{quote_data['text'][:30]}...\""))
                continue  #


            tags = [Tag.objects.get_or_create(name=tag)[0] for tag in quote_data['tags']]


            quote = Quote.objects.create(
                text=quote_data['text'],
                author=author
            )


            quote.tags.set(tags)

            self.stdout.write(self.style.SUCCESS(
                f'✅ Successfully imported quote: \"{quote.text[:30]}...\"'))

