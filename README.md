📄 Requirements Description — Movie Recommendation Web App
1. Purpose
The goal of this project is to develop a web-based movie recommendation system where a user can enter a movie name, and the system suggests similar movies along with their ratings (vote_average).
The app will be accessible online for free via a hosting platform such as Render or PythonAnywhere.

2. Functional Requirements:

   1. User Input

      A form for the user to enter a movie title.
   
      A submit button to trigger recommendations.

   2. Recommendation Engine
     
      Load movie dataset from a CSV file (e.g., movies.csv).
     
      Use TF-IDF vectorization + cosine similarity to compute similarity between movies.
     
      Display vote_average as ratings alongside each recommendation.

    3. Result Display

       Show a list of recommended movies in a table or card layout (Bootstrap styling).
     
       Include movie title and rating.
    
    4. Error Handling

       If the entered movie does not exist, show a “Movie not found” message.
     
       Handle empty input by prompting the user to enter a title.

3. Non-Functional Requirements:

   1. Performance
        Should return recommendations within 2 seconds for datasets up to ~10,000 movies.

   2. Usability
        Mobile-friendly design using Bootstrap.

   3. Availability
        Hosted online on a free platform, accessible via a public URL.

5. Technology Stack:

      **Backend** : Python (Flask)
   
      **Frontend** : HTML, CSS, Bootstrap
   
      **Data Handling** : Pandas
   
      **Machine Learning** : Scikit-learn (TF-IDF, cosine similarity)
   

7. Folder Structure

    movie_recommender
   
   - app.py
   
   - requirements.txt
   
   - movies.csv
   
   - templates/
   
     -- index.html
   
   - static/
   
     -- style.css
   
9. Installation Requirements:

   1. Install Python 3.x

   2. Install dependencies

     - pip install flask pandas scikit-learn gunicorn
   
   3. Have a CSV dataset (movies.csv) with columns like:
    
     - title, overview, vote_average
  
11. Usage

    - python app.py



<img width="1920" height="972" alt="Screenshot (137)" src="https://github.com/user-attachments/assets/277294db-a94b-44ec-a911-42390efcba2b" />

