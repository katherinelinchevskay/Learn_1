friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for i in friends:
        if i == "James":
            continue
        elif i in enemies:
            print(f'{i} we are not friends anymore')
        elif i not in enemies:
            print(f'{i} we are the best friends')