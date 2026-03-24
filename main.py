from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Carrega o dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Divide os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Cria e treina o modelo
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Faz previsões
predictions = model.predict(X_test)

# Avalia o modelo
accuracy = accuracy_score(y_test, predictions)

print("Projeto de Machine Learning executado com sucesso no Docker.")
print(f"Acurácia do modelo: {accuracy:.2f}")
print(f"Primeiras previsões: {predictions[:5]}")