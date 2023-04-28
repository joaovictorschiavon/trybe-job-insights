from src.pre_built.counter import count_ocurrences


def test_counter():
    "Para os parâmetros de path e word a função deve retornar a quantidade"
    "correta de vezes que a palavra ocorre"
    assert count_ocurrences("data/jobs.csv", "python") == 1639
