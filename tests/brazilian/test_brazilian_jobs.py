from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    flag = True
    dict = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in dict:
        if any(key in job for key in ["titulo", "salario", "tipo"]):
            flag = False
    assert flag
