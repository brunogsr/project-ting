import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    try:
        processed_files = {item["nome_do_arquivo"] for item in instance.queue}
        if path_file not in processed_files:
            lines = txt_importer(path_file)
            if lines is not None:
                file_data = {
                    "nome_do_arquivo": path_file,
                    "qtd_linhas": len(lines),
                    "linhas_do_arquivo": lines,
                }
                instance.enqueue(file_data)
                print(file_data)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


def remove(instance):
    if not instance:
        print("Não há elementos")
    else:
        file_data = instance.dequeue()
        path_file = file_data["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position >= len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        file_data = instance.search(position)
        print(file_data)
# push
