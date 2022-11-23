def comparison(array1,array2):
    return print(all([array1[i]==array2[i] for i in range(len(array1))]))

#Функция all() возвращает значение True , если все элементы в итерируемом объекте - истинны, в противном случае она возвращает значение False.
comparison([1,2,3],[3,4,5])