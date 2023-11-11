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
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
        return
    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
