import openai
import random






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
    # Define the system message to guide GPT-4
    system_message = """
    You are a helpful assistant that extracts the mood and intensity level from the user's input.
    The mood can be "Happy", "Sad", or "Frustrated".
    The intensity level is a number between 1 and 3.
    Return the response in the format: "Mood: <mood>, Level: <level>".
    """
    
    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use GPT-4
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ],
        max_tokens=50,
        temperature=0.5
    )
    
    # Extract GPT-4's response
    gpt_response = response.choices[0].message.content.strip()
    return gpt_response

# Main function to handle the conversation
def main():
    print("Welcome to the Mood-Based Song Recommender!")
    chat_history = []  # Initialize chat history
    while True:
        # Get user input
        user_input = input("How are you feeling today? (e.g., 'I'm feeling happy at level 2'): ").strip()
        
        # Ask GPT-4 to extract mood and level
        gpt_response = ask_gpt4(user_input)
        
        # Parse GPT-4's response
        try:
            mood = gpt_response.split("Mood: ")[1].split(",")[0].strip()
            level = int(gpt_response.split("Level: ")[1].strip())
        except:
            print("Sorry, I couldn't understand your mood and level. Please try again!")
            continue
        
        # Recommend a song
        recommendation = recommend_song(mood, level)
        print(f"Here's a song for you: {recommendation}")
        
        # Add the interaction to chat history
        chat_history.append({
            "user_input": user_input,
            "gpt_response": gpt_response,
            "recommendation": recommendation
        })
        
        # Ask if the user wants another recommendation
        again = input("Do you want another recommendation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Mood-Based Song Recommender!")
            break
    
    # Print chat history
    print("\nChat History:")
    for interaction in chat_history:
        print(f"User: {interaction['user_input']}")
        print(f"GPT-4: {interaction['gpt_response']}")
        print(f"Recommendation: {interaction['recommendation']}")
        print("-" * 40)
# Run the program
if __name__ == "__main__":
    main()










chat_history = []



