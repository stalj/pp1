import matplotlib.pyplot as plt
commutes_by = ['car', 'public transport', 'bike', 'on foot']
number_of_people = [25, 19, 32, 7]
plt.bar(commutes_by,number_of_people)
plt.show()