import sys
import os
import difflib
import streamlit as st
import pickle
import requests
from recommender import get_recommendations
from frontend import render_ui

# 1. Path for Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.insert(0, parent_dir)
sys.path.insert(0, current_dir)

# Set page configuration for a wider layout
st.set_page_config(page_title="The Movie Matrix", layout="wide")

# Inject Custom CSS for styling the web app
render_ui()

# Function to fetch movie poster from OMDb API
@st.cache_data
def fetch_poster(movie_title):
    url = f"https://www.omdbapi.com/?t={movie_title}&apikey=c5bf42ab"
    response = requests.get(url)
    data = response.json()
    
    if 'Poster' in data and data['Poster'] != 'N/A':
        return data['Poster']
    else:
        return "https://dummyimage.com/300x450/cccccc/000000.png&text=No+Poster"
    

# Load the saved pickle data files
movies_file_path = os.path.join(current_dir, 'movies.pkl')
matrix_file_path = os.path.join(current_dir, 'matrix.pkl')

movies = pickle.load(open(movies_file_path, 'rb'))
matrix = pickle.load(open(matrix_file_path, 'rb'))

movie_names = movies['title'].values

# Create special options for the dropdown
default_option = "🎬 Choose a movie from the dropdown..."
custom_option = "🔍 Cannot find it? Type your own spelling here..."

# Add both special options to the top of the list
options_list = [default_option, custom_option] + list(movie_names)

# 1. Primary Dropdown Menu (Defaults to index 0: 'Choose a movie...')
selected_option = st.selectbox(
    "Select a movie from the list or type your own:",
    options_list,
    index=0
)

# 2. Conditional Text Box
if selected_option == custom_option:
    final_movie = st.text_input(
        "Type the movie name (Don't worry about spelling!):",
        placeholder="e.g. Avatabne, Titanc..."
    )
elif selected_option == default_option:
    final_movie = ""  # Keep it empty so the landing page triggers
else:
    final_movie = selected_option


# 3. Auto-Trigger Logic (Runs when a movie is selected/searched)
if final_movie:
    
    # --- AI CORRECTION LOGIC ---
    # Find the closest matching movie in our database
    close_matches = difflib.get_close_matches(final_movie, movie_names, n=1)
    
    if close_matches:
        corrected_movie = close_matches[0]
        
        # Check if the spelling was exact or if the AI corrected it
        if final_movie.lower() == corrected_movie.lower():
            # Perfect spelling
            display_message = f"Because you liked '{corrected_movie}', we recommend:"
            bg_color = "#d4edda" # Light Green background
            text_color = "#155724" # Dark Green text
        else:
            # Spelling was wrong, AI corrected it
            display_message = f"💡 Did you mean '{corrected_movie}'? Here are similar movies:"
            bg_color = "#fff3cd" # Light Yellow background
            text_color = "#856404" # Dark Yellow/Brown text
            
        # Display the dynamic message box
        st.markdown(
            f"<div style='text-align: center; color: {text_color}; font-weight: 600; padding: 12px; background-color: {bg_color}; border-radius: 8px; margin-bottom: 25px; font-size: clamp(0.9rem, 2.5vw, 1.1rem);'>{display_message}</div>", 
            unsafe_allow_html=True
        )
        
        # Fetch recommendations using the CORRECTED movie name
        recs = get_recommendations(corrected_movie, cleaned_df=movies, vector_matrix=matrix)
        
        if recs:
            cards_html = "<div class='poster-container'>"
            
            # Loop through the recommendations
            for i in range(10):
                poster_url = fetch_poster(recs[i])
                movie_name = recs[i]
                
                # Append each card to the container
                cards_html += f"""
<div class="movie-card">
<img src="{poster_url}" class="movie-poster" alt="{movie_name}">
<div class="movie-title-card">{movie_name}</div>
</div>
                """
            
            cards_html += "</div>" # Close the grid container
            st.markdown(cards_html, unsafe_allow_html=True)
                    
    else:
        # If the spelling is completely unrecognizable
        st.error(f"Sorry, we couldn't find any match for '{final_movie}'. Please try another spelling!")

# 4. DEFAULT LANDING PAGE (Runs when no movie is searched yet)
else:
    # Welcome message
    st.markdown(
        "<div style='text-align: center; color: #0c5460; font-weight: 600; padding: 12px; background-color: #d1ecf1; border-radius: 8px; margin-bottom: 25px; font-size: clamp(0.9rem, 2.5vw, 1.1rem);'>🔥 Popular Picks to Get You Started:</div>", 
        unsafe_allow_html=True
    )
    
    # Top 10 default movies to display
    default_movies = [
        "Inception", "The Dark Knight", "Interstellar", "The Matrix", "The Avengers",
        "Titanic", "Avatar", "The Shawshank Redemption", "Jurassic Park", "Spider-Man"
    ]
    
    cards_html = "<div class='poster-container'>"
    
    for i in range(10):
        poster_url = fetch_poster(default_movies[i])
        movie_name = default_movies[i]
        
        # Append each card to the container
        cards_html += f"""
<div class="movie-card">
<img src="{poster_url}" class="movie-poster" alt="{movie_name}">
<div class="movie-title-card">{movie_name}</div>
</div>
        """
        
    cards_html += "</div>" # Close the grid container
    st.markdown(cards_html, unsafe_allow_html=True)

# 5. FIXED GENRE ROWS
def display_movie_row(section_title, movies_list):
    st.markdown(f'<div class="section-title">{section_title}</div>', unsafe_allow_html=True)
    
    row_html = "<div class='poster-container'>"
    for movie in movies_list:
        poster_url = fetch_poster(movie)
        row_html += f"""<div class="movie-card">
<img src="{poster_url}" class="movie-poster" alt="{movie}">
<div class="movie-title-card">{movie}</div>
</div>"""
    row_html += "</div>"
    
    st.markdown(row_html, unsafe_allow_html=True)

scifi_movies = ["Interstellar", "Inception", "The Matrix", "Gravity", "The Martian"]
romance_movies = ["The Notebook", "Titanic", "A Walk to Remember", "La La Land", "Pride & Prejudice"]
thriller_movies = ["Shutter Island", "Memento", "The Prestige", "Gone Girl", "Prisoners"]

display_movie_row("🚀 Sci-Fi & Space Adventures", scifi_movies)
display_movie_row("💖 Epic Romance", romance_movies)
display_movie_row("🤯 Mind-Bending Thrillers", thriller_movies)