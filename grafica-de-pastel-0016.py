import matplotlib.pyplot as plt
# Johan Paulo Aros Reveles NC 0016
categories = ["ML","Lenguaje N","VA","Matematicas","Lengua"]
sales = [10, 8, 10, 7, 8]

plt.pie(sales, labels=categories, autopct = '%1.1f%%')
plt.title("Grafica circular ejemplo, 0016")
plt.xlabel("nivel X")
plt.ylabel("Nivel Y")
plt.show()

print("Johan Paulo Aros Reveles NC 0016")