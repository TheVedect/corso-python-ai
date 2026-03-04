import pandas as pd
import numpy as np
from pyexpat import features

from numpy.ma.extras import hstack
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

pd.options.display.max_columns = 20

df = pd.read_csv("NetFlix.csv")
print(df["show_id"].nunique())
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Varies")
df["country"] = df["country"].fillna("Not Listed")
df["date_added"] = df["date_added"].fillna("9999")
df["rating"] = df["rating"].fillna("N/A")
missing_values = df.isna().sum().sort_values(ascending=False)
print(missing_values)

df["soup"] = f"{df['type']}{df['title']}{df['director']}{df['cast']}{df['country']}{df['genres']}{df['description']}"
#print(df["soup"])

tfdif = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfdif.fit_transform(df["soup"])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(),index=df.index)
#print(tfidf_matrix)

scaler = StandardScaler()
#df["year_normalized"] = scaler.fit_transform(df[["release_year"]])
#X = pd.concat([tfidf_df, df["year_normalized"]], axis=1)
X = pd.DataFrame(tfidf_df)
#print(X)

model = NearestNeighbors(metric="cosine" ,n_neighbors=10)
model.fit(X)

def reccomend_by_show_id(
        show_id: str,
        k: int = 10,
) -> pd.DataFrame:
    seed = df[df["show_id"] == show_id]
    if seed.empty:
        raise ValueError("Show ID does not exist!")

    seed_row = seed.iloc[0]
    seed_soup = seed_row["soup"]
    seed_tfidf = tfdif.fit_transform(seed_row[["soup"]])
    seed_tfidf_df = pd.DataFrame(seed_tfidf.toarray())
    #seed_year_normalized = pd.DataFrame(scaler.fit_transform(df[["year_normalized"]]))
    #seed_vec = pd.concat([seed_tfidf_df,seed_year_normalized], axis=1)
    seed_tfidf_df.columns = seed_tfidf_df.columns.astype(str)

    distances, indices = model.kneighbors(seed_tfidf_df)
    recs = df.iloc[indices[0]].copy()
    recs = recs[recs["show_id"] != show_id]

    recs = recs.head(k)
    cols = [
        "show_id",
        "type",
        "title",
        "director",
        "cast",
        "genres",
    ]
    return recs[cols]


test_id = "s5837"
print("Show seed: \n")
print(df[df["show_id"] == test_id][["title", "director"]])

print("Show consigliate:\n")
print(reccomend_by_show_id(test_id, k=10))

