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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
