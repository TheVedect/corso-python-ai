import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt

pd.options.display.max_columns = 12 #Mi permette di vedere più colonne.
df = pd.read_csv("Titanic-Dataset.csv")
print(df.info())
#Ci sono 177 su 891 Age null: ci posso mettere la media.
#Ci sono solo 204 dati per Cabin, però non mi serve la colonna, poiché la cabina poco centra.
#Le stringhe non ci servono, tranne il Sex, poiché non ci interessano nomi, cose così.

#EDA: Explorative Data Analysis.
#survived = df["Survived"].value_counts() #Anche perché valgono o 0 o 1.
#survived_by_sex = df.groupby("Sex")["Survived"].mean()
#survived_by_age = df.groupby("Age")["Survived"].mean()
#survived_by_pclass = df.groupby("Pclass")["Survived"].mean()
#avg_age_survived = df[df["Survived"] == 1]["Age"].mean()
#print(survived_by_sex)
#print(survived_by_age)
#print(survived_by_pclass)
#print(avg_age_survived)

#Inizio pulizia del dato.
df["IsMaleChild"] = 0
df.loc[df["Name"].str.contains("Master"), "IsMaleChild"] = 1
df = df.drop(["PassengerId","Name", "Cabin", "Ticket", "Fare"], axis=1) #Tolgo le colonne inutili.
df["Age"] = df["Age"].fillna(df["Age"].median()) #Posso usare anche la mediana, volendo.
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0]) #Usare la moda per fare fill con l'elemento  più probabile
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = 0
df["Age0015"] = 0
df["Age1540"] = 0
df["Age4080"] = 0
df.loc[df["FamilySize"] == 1, "IsAlone"] = 1 #Permette di assegnare valori condizionali.

df.loc[(df["Age"] > 0) & (df["Age"] <= 15), "Age0015"] = 1
df.loc[(df["Age"] > 15) & (df["Age"] <= 40), "Age1540"] = 1
df.loc[df["Age"] > 40, "Age4080"] = 1
df = df.drop(["SibSp", "Parch"], axis=1)
df = df.drop(["Age"], axis=1)

#Ora tocca fare il One Hot Encoding, che mi permette di separare una colonna con valori non numerici in più colonne,
#Una per ciascun valore di tale colonna, che vale 1 se è quello e 0 se non vale quello.
df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True) #drop_first elimina la prima colonna creata, per spazio

#Il target è se è sopravvissuto o meno, le features sono il resto.
X = df.drop(["Survived"], axis=1) #Non serve fare le copie: non sto modificando i dati.
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split( #Il modello non vede quelli di train, poiché poi ci deve testare sopra.
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

#print(X_train)

#Verrà utilizzato il falsificatore Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy ========> ", accuracy)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix ========>\n",cm)

cr = classification_report(y_test, y_pred)
print("Classification Report ========>\n",cr)

y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_pred)
print("Train Accuracy ========> ", train_accuracy)
print("Test Accuracy ========> ", test_accuracy)

for feature, coef in zip(X.columns, model.coef_[0]): #Sono i pesi con cui dà la correlazione di non sopravvivenza,
    print(feature, coef)                             #Faranno attivare o meno la sigmoide.

#Provando a predire il finale di Titanic.
jack = {
    "Pclass": 3,
    "IsMaleChild": 0,
    "FamilySize": 1,
    "IsAlone": 1,
    "Sex_male": 1,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q" : 0,
    "Embarked_S" : 1
}

rose = {
    "Pclass": 1,
    "IsMaleChild": 0,
    "FamilySize": 2,
    "IsAlone": 0,
    "Sex_male": 0,
    "Age0015": 0,
    "Age1540": 1,
    "Age4080": 0,
    "Embarked_Q" : 0,
    "Embarked_S" : 1
}

char_titanic_movie = pd.DataFrame([jack, rose], index=["Jack", "Rose"])
char_titanic_movie = char_titanic_movie.reindex(columns=X.columns, fill_value=0)

pred_class = model.predict(char_titanic_movie)
pred_proba = model.predict_proba(char_titanic_movie)[:,1]
results = pd.DataFrame(
    {
        "Predicted Survived": pred_class,
        "Predicted Probability": pred_proba
    }, index=char_titanic_movie.index
)

print(results)
survived_by_sex = df.groupby("Sex_male")["Survived"].mean()
plt.figure()
plt.bar(["Femminucce", "Maschietti"], survived_by_sex)
plt.title("Sopravvivenza per Sesso")
plt.ylabel("Probabilità di sopravvivenza")
plt.show()