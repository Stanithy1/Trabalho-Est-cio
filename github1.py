import os
import sqlite3
from datetime import datetime

# Conexão com o banco de dados SQLite (cria o arquivo caso não exista)
conn = sqlite3.connect('unimed_files.db')
cursor = conn.cursor()

# Criação da tabela para armazenar os arquivos
cursor.execute('''
CREATE TABLE IF NOT EXISTS documentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    data_upload TEXT NOT NULL,
    caminho TEXT NOT NULL
)
''')
conn.commit()

# Função para fazer upload de um arquivo
def upload_arquivo(nome_arquivo, tipo, caminho):
    data_upload = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO documentos (nome, tipo, data_upload, caminho) 
        VALUES (?, ?, ?, ?)
    ''', (nome_arquivo, tipo, data_upload, caminho))
    conn.commit()
    print(f"Arquivo {nome_arquivo} adicionado com sucesso!")

# Função para listar os arquivos
def listar_arquivos():
    cursor.execute("SELECT * FROM documentos")
    arquivos = cursor.fetchall()
    for arquivo in arquivos:
        print(arquivo)

# Função para buscar um arquivo pelo nome
def buscar_arquivo(nome):
    cursor.execute("SELECT * FROM documentos WHERE nome LIKE ?", ('%' + nome + '%',))
    arquivos = cursor.fetchall()
    return arquivos

# Função para excluir um arquivo
def excluir_arquivo(id_arquivo):
    cursor.execute("DELETE FROM documentos WHERE id = ?", (id_arquivo,))
    conn.commit()
    print(f"Arquivo {id_arquivo} excluído com sucesso!")

# Exemplo de uso
upload_arquivo("Acordo_Cooperado_123.pdf", "acordo", "Z:/arquivos/acordos/Acordo_Cooperado_123.pdf")
listar_arquivos()

# Fechar a conexão com o banco de dados
conn.close()
