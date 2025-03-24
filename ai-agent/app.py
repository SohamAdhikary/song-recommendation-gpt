import streamlit as st
from song_recommender import recommend_song

# Title of the app
st.title("Resonet.AI")

# Information about available moods
st.write("### How are you feeling today?")
st.write("Available moods: **Happy** or **Sad**.")

# Input for user's mood with selectbox
mood = st.selectbox("Select your mood:", ["Happy", "Sad"])

# Input for intensity level
level = st.number_input("Enter intensity level (1, 2, or 3):", min_value=1, max_value=3, value=1)

# Function to generate a YouTube search link
def get_youtube_link(song_title):
    return f"https://www.youtube.com/results?search_query={song_title.replace(' ', '+')}"

# Button to get recommendation
if st.button("Get Recommendation"):
    if mood:
        song = recommend_song(mood, level)
        st.success(f"Recommended song: {song}")

        # Use the YouTube search link
        youtube_link = get_youtube_link(song)
        st.markdown(f"[Listen on YouTube]({youtube_link})")
    else:
        st.error("Please select your mood!")
