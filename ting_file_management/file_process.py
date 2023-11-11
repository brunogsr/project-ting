import sys
import os
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        file = instance.search(index)
        if file["nome_do_arquivo"] == path_file:
            print("Arquivo já processado", file=sys.stderr)
            return

    if not os.path.exists(path_file):
        print("Arquivo não encontrado", file=sys.stderr)
        return

    file_lines = txt_importer(path_file)
    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }
    instance.enqueue(file)
    print(file, file=sys.stdout)


def remove(instance):
    if not instance.queue:
        print("Não há elementos")
    else:
        file_data = instance.dequeue()
        path_file = file_data["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance.queue):
        print("Posição inválida", file=sys.stderr)
    else:
        file_data = instance.search(position)
        print(file_data)
