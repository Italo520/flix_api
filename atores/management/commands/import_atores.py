import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from atores.models import Atores

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com os dados dos atores'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    nome = row['nome']
                    data_nascimento = datetime.strptime(row['data_nascimento'], '%Y-%m-%d').date() if row['data_nascimento'] else None
                    nascionalidade = row['nascionalidade'] if row['nascionalidade'] else None

                    self.stdout.write(self.style.NOTICE(f'Importando ator: {nome}'))

                    Atores.objects.create(
                        nome=nome,
                        data_nascimento=data_nascimento,
                        nascionalidade=nascionalidade,
                    )
                self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo {file_name} não encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro: {str(e)}'))