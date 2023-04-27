from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    max_salary = 0
    dict = read(path)
    unique_max_salary = set(
        salary["max_salary"]
        for salary in dict
        if salary["max_salary"] and salary["max_salary"].isdigit()
    )
    for x in unique_max_salary:
        if int(x) > int(max_salary):
            max_salary = int(x)
    return max_salary

    raise NotImplementedError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """

    dict = read(path)
    unique_min_salary = set(
        salary["min_salary"]
        for salary in dict
        if salary["min_salary"] and salary["min_salary"].isdigit()
    )
    list_min_salary = list(unique_min_salary)

    min_salary = None

    for x in list_min_salary:
        if x and x.isdigit():
            min_salary = int(x)
            break

    for x in unique_min_salary:
        if int(x) < int(min_salary):
            min_salary = int(x)
    return min_salary

    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = float(job["min_salary"])
        max_salary = float(job["max_salary"])
        salary_in_float = float(salary)
    except (ValueError, TypeError, KeyError):
        raise ValueError("Wrong value of salaries")

    if min_salary > max_salary:
        raise ValueError("Minimum salary bigger than maximum salary")

    if job["min_salary"] <= salary_in_float <= job["max_salary"]:
        return True
    else:
        return False

    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
