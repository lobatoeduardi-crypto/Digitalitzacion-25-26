# Ordenación con Selection Sort

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

# Selection Sort: buscamos el mínimo en cada iteración
for i in range(len(list_num)):
    min_idx = i
    for j in range(i+1, len(list_num)):
        if list_num[j] < list_num[min_idx]:
            min_idx = j
    # Intercambiamos el mínimo con la posición actual
    list_num[i], list_num[min_idx] = list_num[min_idx], list_num[i]

print("Lista ordenada con Selection Sort:", list_num)

# Ordenación con Insertion Sort

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

# Insertion Sort: insertamos cada elemento en la posición correcta
for i in range(1, len(list_num)):
    key = list_num[i]
    j = i - 1
    while j >= 0 and list_num[j] > key:
        list_num[j + 1] = list_num[j]
        j -= 1
    list_num[j + 1] = key

print("Lista ordenada con Insertion Sort:", list_num)