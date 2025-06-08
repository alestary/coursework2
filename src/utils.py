def filter_top_vacancies(vacancies: list, top_n: int) -> list:
    """Сортирует вакансии"""
    return sorted(vacancies, reverse=True)[:top_n]