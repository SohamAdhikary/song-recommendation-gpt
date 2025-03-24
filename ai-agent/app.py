import streamlit as st
from song_recommender import recommend_song

# Title of the app
st.title("Song Recommendation GPT")

# Input for user's mood
mood = st.text_input("How are you feeling today?")

# Input for intensity level
level = st.number_input("Enter intensity level (1, 2, or 3):", min_value=1, max_value=3, value=1)

# Button to get recommendation
if st.button("Get Recommendation"):
    if mood:
        song = recommend_song(mood, level)
        st.success(f"Recommended song: {song}")
    else:
        st.error("Please enter your mood!")