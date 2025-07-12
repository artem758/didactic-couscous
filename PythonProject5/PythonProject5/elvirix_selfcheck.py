import yaml

def load_groups():
    try:
        with open("group_list.yaml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, dict) and "groups" in data:
                return data["groups"]
            else:
                print("⚠️ group_list.yaml не содержит ключ 'groups'")
                return []
    except Exception as e:
        print(f"Ошибка загрузки group_list.yaml: {e}")
        return []

def check_group_transition(current_group, group_list):
    try:
        next_index = group_list.index(current_group) + 1
        return group_list[next_index]
    except (ValueError, IndexError):
        return group_list[0] if group_list else None

def run():
    groups = load_groups()
    print(f"✅ Загружено {len(groups)} групп")