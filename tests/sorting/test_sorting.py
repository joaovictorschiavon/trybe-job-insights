from src.pre_built.sorting import sort_by

jobs = [
    {"min_salary": 50000, "max_salary": 400000, "date_posted": 2022-11-11},
    {"min_salary": 30000, "max_salary": 300000, "date_posted": 2023-11-11},
    {"min_salary": 40000, "max_salary": 400000, "date_posted": 2024-11-11},
    {"min_salary": 80000, "max_salary": 500000, "date_posted": 2026-11-11}
]


def test_sort_by_criteria():
    # flag_criteria = False
    # criterias = ["min_salary", "max_salary", "date_posted"]
    # for crit in criterias:
    #     if crit == criteria:
    #         flag_criteria = True
    # with pytest.raises(
    #     ValueError, match=f"invalid sorting criteria: {criteria}"
    # ):
    #     sort_by(jobs, criteria)

    criterias = ["min_salary", "max_salary", "date_posted"]
    criterias_desc = ["max_salary", "date_posted"]

    for criteria in criterias:
        sort_by(jobs, criteria)
        if criteria in criterias_desc:
            assert jobs[0][criteria] > jobs[1][criteria]
        else:
            assert jobs[0][criteria] < jobs[1][criteria]
