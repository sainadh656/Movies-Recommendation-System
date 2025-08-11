from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import os

app = Flask(__name__)

# ---------- Load dataset (once on startup) ----------
DATA_PATH = os.path.join("data", "tmdb_5000_movies.csv")  # update if needed
movies = pd.read_csv(DATA_PATH)
# Ensure required cols exist
for col in ["title", "overview"]:
    if col not in movies.columns:
        raise SystemExit(f"CSV must contain a '{col}' column.")
movies['overview'] = movies['overview'].fillna('')
# Optional rating column:
if 'vote_average' not in movies.columns:
    movies['vote_average'] = None

# Prepare TF-IDF matrix and cosine similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Helper: get list of titles
all_titles = movies['title'].tolist()

def recommend_movies(title, num_recommendations=5):
    # find close match (handles typos / partial)
    matches = difflib.get_close_matches(title, all_titles, n=1, cutoff=0.3)
    if not matches:
        return None, []
    best_match = matches[0]

    # get the first index for that title (handles duplicates)
    idx_list = movies[movies['title'] == best_match].index.tolist()
    if not idx_list:
        return None, []
    idx = idx_list[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # skip itself

    recs = []
    for i, score in sim_scores:
        title_rec = movies.at[i, "title"]
        rating = movies.at[i, "vote_average"] if 'vote_average' in movies.columns else None
        recs.append({"title": title_rec, "rating": rating, "score": float(score)})
    return best_match, recs

# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def home():
    best_match = None
    recommendations = []
    query = ""
    if request.method == "POST":
        query = request.form.get("movie", "").strip()
        if query:
            best_match, recommendations = recommend_movies(query, num_recommendations=5)
    return render_template("index.html", best_match=best_match,
                           recommendations=recommendations, query=query)

if __name__ == "__main__":
    app.run(debug=True)
