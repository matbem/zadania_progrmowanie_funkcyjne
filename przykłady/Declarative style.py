orders = [
    {"id": 1, "total": 100, "status": "completed"},
    {"id": 2, "total": 200, "status": "cancelled"},
    {"id": 3, "total": 150, "status": "completed"}
]

# Oblicz łączną wartość ukończonych zamówień
result = sum(map(lambda order: order["total"],
                 filter(lambda order: order["status"] == "completed", orders)))

print("Suma ukończonych zamówień:", result)  # => 250
