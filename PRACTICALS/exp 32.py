from sklearn.neighbors import KNeighborsClassifier

X = [[1, 2], [2, 3], [3, 3], [6, 7], [7, 8]]
y = [0, 0, 0, 1, 1]

k = int(input("Enter K value: "))
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

print("Predicted Class:", model.predict([[a, b]])[0])
