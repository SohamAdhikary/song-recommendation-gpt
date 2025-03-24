from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import random

app = FastAPI()

# Set your OpenAI API key
openai.api_key = "your-api-key-here"  # Replace with your actual API key

# Dictionary of songs mapped to moods and levels
song_recommendations = {
    "Happy": {
        1: [
            "Brazil - Declan McKenna",
            "BIRDS OF A FEATHER - Billie Eilish",
            "See You Again - Tyler, The Creator, Kali Uchis",
            "Go Steady - Tender",
            "End of Beginning - Djo",
            "Sex, Drugs, Etc. - Beach Weather",
            "Borderline - Tame Impala",
            "Sailor Song - Gigi Perez",
            "Aashiyan - gini"
        ],
        2: [
            "Ocean Eyes - Billie Eilish",
            "Heather - Conan Gray",
            "Electric Love - BØRNS",
            "Like Real People Do - Hozier",
            "Falling - Harry Styles",
            "Youth - Daughter",
            "Talk Me Down - Troye Sivan",
            "Ribs - Lorde",
            "Stargazing - The Neighbourhood",
            "Line Without a Hook - Ricky Montgomery",
            "Espresso - Sabrina Carpenter",
            "That's So True - Gracie Adams",
            "WILDFLOWER - Billie Eilish",
            "Sweater Weather - The Neighbourhood"
        ],
        3: [
            "Khudi - The Local Train",
            "Savera - Aashir Wajahat, NAYEL",
            "Aadhey Aadhore - Aashir Wajahat",
            "Chor - Justh",
            "Kabhi Mein Kabhi Tum - AUR",
            "Mera Safar - Iqliqse Nova",
            "Lamhey - Anubha Bajaj",
            "Beqadra - Hasan Raheem",
            "Jhoom - Ali Zafar",
            "Pyaar Bhi Doongi - Abdul Hannan, Rovalio",
            "Tera Hua - Arijit Singh",
            "Dil Fareb - Shae Gill, Hassan and Roshaan",
            "Mitti - Taha G",
            "Ik Lamha - Soch The Band",
            "Sahil - Hasan Raheem",
            "Raatein - Aish",
            "Tu - Righteous Rep"
        ]
    },
    "Sad": {
        1: [
            "Noor - Tanmaya Bhatnagar",
            "Haaraay - Abdul Hannan",
            "Rihaee - Suzonn",
            "Shayaad - Taba Chake",
            "Dhalti Rahe - Twin Strings",
            "Jeene Mein Aye Maza - Ankur Tewari, Mikey McCleary",
            "Aankhon Ke Darmiyan - Osho Jain",
            "Udne Do - Anuv Jain",
            "Na Tum Rahe Tum - Razdeep"
        ],
        2: [
            "Lae Dooba - Sunidhi Chauhan",
            "Hale Dil - Harshit Saxena",
            "Kasoor - Prateek Kuhad",
            "Aziyat - PratOfficial",
            "Sun Lo Na - Suzonn",
            "Tere Jaane Se - Anurag Vashisht",
            "Tu Aisa Kaisa Hai - Osho Jain",
            "Phir Le Aya Dil (Reprise) - Rekha Bhardwaj",
            "Baarishein - Anuv Jain",
            "Ajab Si - KK"
        ],
        3: [
            "Tuta Pull Wahan - Deepak Rathore Project",
            "Choo Lo - The Local Train",
            "Aaoge Tum Kabhi - The Local Train",
            "Let Her Go - Passenger",
            "Apologize - OneRepublic",
            "Stay - Rihanna, Mikky Ekko",
            "Manzil - The Local Train",
            "Zaroori Tha - Rahat Fateh Ali Khan",
            "Bekhayali - Sachet Tandon",
            "It's Too Late - Carole King",
            "Bleeding Love - Leona Lewis",
            "Someone You Loved - Lewis Capaldi",
            "All of Me - John Legend",
            "Khulne Do - Prateek Kuhad",
            "Shaamein - Prateek Kuhad, Lisa Mishra",
            "Mann Mera - Gajendra Verma",
            "Dil Mere - The Local Train",
            "Iktara - Kavita Seth, Amitabh Bhattacharya",
            "Nahi Jaana - Jasleen Royal",
            "Tum Jab Paas - Prateek Kuhad",
            "Yahin Hoon Main - Ayushmann Khurrana",
            "Moh Moh Ke Dhaage - Monali Thakur, Papon",
            "Tum Mile (Reprise) - Javed Ali"
        ]
    }
}


# Function to recommend a song
def recommend_song(mood, level):
    if mood in song_recommendations:
        if level in song_recommendations[mood]:
            return random.choice(song_recommendations[mood][level])
        else:
            return "Invalid level. Please choose a level between 1 and 3."
    else:
        return "Invalid mood. Please choose a valid mood."

# Function to interact with GPT-4
def ask_gpt4(user_input):
    system_message = """
    You are a helpful assistant that extracts the mood and intensity level from the user's input.
    The mood can be "Happy", "Sad", or "Frustrated".
    The intensity level is a number between 1 and 3.
    Return the response in the format: "Mood: <mood>, Level: <level>".
    """
    
    messages = [{"role": "system", "content": system_message}]
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=50,
        temperature=0.5
    )
    
    gpt_response = response.choices[0].message.content.strip()
    return gpt_response

# Define a request model for the API
class UserInput(BaseModel):
    user_input: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Mood-Based Song Recommender!"}


# Create an API endpoint
@app.post("/recommend")
async def recommend_song_endpoint(user_input: UserInput):
    try:
        # Ask GPT-4 to extract mood and level
        gpt_response = ask_gpt4(user_input.user_input)
        
        # Parse GPT-4's response
        mood = gpt_response.split("Mood: ")[1].split(",")[0].strip()
        level = int(gpt_response.split("Level: ")[1].strip())
        
        # Recommend a song
        recommendation = recommend_song(mood, level)
        return {"recommendation": recommendation}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



