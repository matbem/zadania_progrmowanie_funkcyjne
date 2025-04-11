def update_user_info(user, field, value):
    return {**user, field: value}  # zwraca nowy słownik

original_user = {"name": "Ania", "role": "user"}
updated_user = update_user_info(original_user, "role", "admin")

print("Original:", original_user)
print("Updated:", updated_user)
