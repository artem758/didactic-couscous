import yaml

def load_groups():
    try:
        with open("group_list.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data.get("groups", [])
    except Exception as e:
        print(f"Ошибка загрузки group_list.yaml: {e}")
        return []

def check_group_transition(current_group, group_list):
    try:
        next_index = group_list.index(current_group) + 1
        return group_list[next_index]
    except (ValueError, IndexError):
        return group_list[0]

def run():
    group_list = load_groups()
    current_group = group_list[0]
    next_group = check_group_transition(current_group, group_list)
    print(f"🛰 Переход от {current_group} к {next_group}")