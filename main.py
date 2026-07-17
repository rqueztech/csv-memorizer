from collections import defaultdict
from pathlib import Path

file_path = Path.home() / "Documents" / "restaurant-menu" / "resources.csv"

def read_in_restaurant_menu() -> list[str]:
    restaurant_full_menu = []
    with open(file_path, "r", encoding = "utf-8") as file:
        results = file.read().splitlines()
        restaurant_full_menu = [current.split(",") for current in results]
        
    return restaurant_full_menu

def create_index_map(restaurant_full_menu_headers: list[str]) -> dict[int]:
    index_menu = {item: index for index, item in enumerate(restaurant_full_menu_headers)}
    return index_menu

def sort_by_field(restaurant_full_menu: list[list[str]], index_map: int, key_field: dict[str], restaurant_blacklist: set) -> dict[list[str]]:
    sorted_custom_map = defaultdict(list)
    for index, value in enumerate(restaurant_full_menu):
        if index == 0:
            continue
        raw_index: int = index_map[key_field]
        key_payload: str = value[raw_index]
        
        if key_payload in restaurant_blacklist:
            continue

        new_value = []
        for current in index_map:
            current_index = index_map[current]
            if current in restaurant_blacklist:
                continue

            if raw_index == index_map[current]:
                continue
            new_value.append(value[current_index])
            
        sorted_custom_map[key_payload].append(new_value)
    return sorted_custom_map

def print_sorted_custom_map(sorted_custom_map):
    for key, value in sorted_custom_map.items():
        print(key, " :: ", value)

def main():
    if not file_path.exists():
        print("DEBUG! The file does not exist")
        return -1
    restaurant_full_menu = read_in_restaurant_menu()
    restaurant_headers = restaurant_full_menu[0]
    index_map = create_index_map(restaurant_headers)

    restaurant_whitelist = set(restaurant_full_menu[0])
    restaurant_blacklist = set()
    
    while True:
        print(f"Current blacklist {restaurant_blacklist}")
        menu_option = input(f"Enter your desired sorting: {restaurant_whitelist}")
        if menu_option in index_map and menu_option not in restaurant_blacklist:
            sorted_custom_map = sort_by_field(restaurant_full_menu, index_map, menu_option, restaurant_blacklist)
            print_sorted_custom_map(sorted_custom_map)
        elif menu_option == "blacklist":
            while True:
                print(restaurant_whitelist)
                print(restaurant_blacklist)
                blacklist_option  = input("Which one do you want to blacklist?")

                print(index_map)

                if blacklist_option == "exit":
                    break
                
                if blacklist_option in restaurant_blacklist or blacklist_option not in index_map:
                    print("Either blacklisted or nonexistent")
                    continue

                restaurant_whitelist.remove(blacklist_option)
                restaurant_blacklist.add(blacklist_option)
                
        else:
            print("Enter Correct Value")
    
    return 0

if __name__ == "__main__":
    main()
