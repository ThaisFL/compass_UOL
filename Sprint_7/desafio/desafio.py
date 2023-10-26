import boto3
import os

# Substitua 'SEU_ACCESS_KEY' e 'SUA_SECRET_KEY' pelas credenciais da sua função IAM
access_key = 'AWSGlueServiceRole-Lab4'
secret_key = 'AWSGlueServiceRole-Lab4'

# Configuração do cliente S3 com as credenciais
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Nome do seu bucket no S3
bucket_name = 'laboratorio-etl.com'

# Especificação dos dados
data_specification = 'Local/CSV'

# Data de processamento
processing_date = '2023/10/25'

# Lista de arquivos CSV a serem carregados
csv_files = ['movies.csv', 'series.csv']

for file in csv_files:
    # Caminho completo no S3
    s3_path = f'{bucket_name}/{data_specification}/{file}/{processing_date}/{file}'
    
    # Realize a carga do arquivo CSV no S3
    s3.upload_file(f'/app/desafio/{file}', bucket_name, s3_path)

print("Arquivos CSV carregados com sucesso no Amazon S3 usando credenciais IAM.")
