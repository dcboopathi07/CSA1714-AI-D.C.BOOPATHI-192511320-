from sklearn.linear_model import LinearRegression

n = int(input("Enter number of data points: "))

X = []
y = []

for i in range(n):
    x = float(input("Enter X value: "))
    target = float(input("Enter Y value: "))
    X.append([x])
    y.append(target)

model = LinearRegression()
model.fit(X, y)

value = float(input("Enter value to predict: "))
print("Predicted Value:", model.predict([[value]])[0])
