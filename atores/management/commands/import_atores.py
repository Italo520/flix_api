import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from atores.models import Atores, CONST_NACIONALIDADE


class Command(BaseCommand):
    help = 'Importa dados de atores de um arquivo CSV.'

    NACIONALIDADE_MAP = {value: key for key, value in CONST_NACIONALIDADE}

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

                    # Converte a data de nascimento, se existir
                    data_nascimento = None
                    if row['data_nascimento']:
                        try:
                            data_nascimento = datetime.strptime(row['data_nascimento'], '%Y-%m-%d').date()
                        except ValueError:
                            self.stdout.write(self.style.WARNING(f'AVISO: Data de nascimento inválida para {nome}: "{row["data_nascimento"]}". Ignorando data.'))

                    # Obtém a nacionalidade do CSV e a mapeia para o código de duas letras
                    nacionalidade_do_csv = row.get('nacionalidade', '').strip()

                    # Usa o mapeamento para obter o código da nacionalidade
                    # Se não encontrar no mapeamento, salva como None (ou uma string vazia, dependendo da necessidade)
                    nacionalidade_para_salvar = self.NACIONALIDADE_MAP.get(nacionalidade_do_csv, None)

                    if not nacionalidade_para_salvar and nacionalidade_do_csv:
                        self.stdout.write(self.style.WARNING(f'AVISO: Nacionalidade "{nacionalidade_do_csv}" para o ator {nome} não encontrada no mapeamento. Salvando como vazio.'))

                    self.stdout.write(self.style.NOTICE(f'Importando ator: {nome} (Nacionalidade CSV: "{nacionalidade_do_csv}", Salvando como: "{nacionalidade_para_salvar}")'))

                    Atores.objects.create(
                        nome=nome,
                        data_nascimento=data_nascimento,
                        nacionalidade=nacionalidade_para_salvar,
                    )
                self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo {file_name} não encontrado.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro: {str(e)}'))
