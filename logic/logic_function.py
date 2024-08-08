from logic.search_1c import find_display_names


def find_full_1c():
    find_1c = find_display_names(r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall")
    find_1c_2 = find_display_names(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    found_all_One_C = find_1c.copy()
    found_all_One_C.update(find_1c_2)
    return found_all_One_C
