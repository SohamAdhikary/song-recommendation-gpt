import streamlit as st
from song_recommender import recommend_song

# Title of the app
st.title("Resonet.AI")

# Information about available moods
st.write("### How are you feeling today?")
st.write("Available moods: *Happy* or *Sad*.")

# Input for user's mood with selectbox
mood = st.selectbox("Select your mood:", ["Happy", "Sad"])

# Input for intensity level
level = st.number_input("Enter intensity level (1, 2, or 3):", min_value=1, max_value=3, value=1)

# Button to get recommendation
if st.button("Get Recommendation"):
    if mood:
        song = recommend_song(mood, level)
        st.success(f"Recommended song: {song}")
        # Add a YouTube link (replace YOUR_VIDEO_ID with an actual ID)
        youtube_link = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" 
        st.markdown(f"[Listen on YouTube]({youtube_link})")
    else:
        st.error("Please select your mood!")