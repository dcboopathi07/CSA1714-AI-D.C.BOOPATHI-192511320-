
from sklearn.tree import DecisionTreeClassifier

# Input: [Age, Salary]
X = [[22, 20000], [25, 30000], [30, 50000],
     [35, 60000], [40, 80000]]

# Output: 0 = No, 1 = Yes
y = [0, 0, 1, 1, 1]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

age = 32
salary = 55000

result = model.predict([[age, salary]])

if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
