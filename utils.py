import json


def load_candidates_from_json():
    """
     Возвращает список всех кандидатов
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """
     Возвращает одного кандидата по его id
    """
    for item in load_candidates_from_json():
        if candidate_id == item['id']:
            return item


def get_candidates_by_name(candidate_name):
    """
     Возвращает кандидатов по имени
    """
    candidates_for_name = []
    for item in load_candidates_from_json():
        if candidate_name.lower() in item['name'].lower():
            candidates_for_name.append(item)
    return candidates_for_name


def get_candidates_by_skill(skill_name):
    """
     Возвращает кандидатов по навыку
    """
    candidates_for_skill = []
    for item in load_candidates_from_json():
        if skill_name.lower() in item['skills'].lower():
            candidates_for_skill.append(item)
    return candidates_for_skill
