import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample rating data
data = {
    "Movie": ["Inception", "Avatar", "Titanic", "Avengers", "Interstellar"],
    "User1": [5, 4, 5, 4, 5],
    "User2": [4, 5, 4, 5, 4],
    "User3": [5, 5, 3, 4, 5],
    "User4": [3, 4, 5, 4, 3]
}

df = pd.DataFrame(data)
df.set_index("Movie", inplace=True)

# Compute similarity between movies
similarity = cosine_similarity(df)
sim_df = pd.DataFrame(similarity, index=df.index, columns=df.index)

print("📊 Smart Recommendation System \n")
movie = input("Enter a movie you like: ")

if movie not in sim_df:
    print("Movie not found.")
else:
    scores = sim_df[movie].sort_values(ascending=False)
    print("\n🎯 Recommended movies:")
    for m in scores.index[1:4]:
        print("•", m)
