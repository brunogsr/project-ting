def exists_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        filename = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]

        occurrences = [
            {"linha": line_num + 1}
            for line_num, line in enumerate(lines)
            if word.lower() in line.lower()
        ]

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": filename,
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        filename = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]

        occurrences = [
            {"linha": line_num + 1, "conteudo": line}
            for line_num, line in enumerate(lines)
            if word.lower() in line.lower()]

        if occurrences:
            result = {"arquivo": filename, "ocorrencias": occurrences}
            if word.lower() in result["ocorrencias"][0]["conteudo"].lower():
                result["palavra"] = word
            results.append(result)

    return results
