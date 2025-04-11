users = [
    {"name": "Ala", "age": 30},
    {"name": "Zosia", "age": 22},
    {"name": "Bartek", "age": 25}
]

# Sortujemy według wieku, odwrotnie
sorted_users = sorted(users, key=lambda user: user["age"], reverse=True)

for user in sorted_users:
    print(f'{user["name"]} ({user["age"]} lat)')
