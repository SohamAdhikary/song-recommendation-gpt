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
def recommend_song(mood, level=1):
    """
    Recommends a song based on the user's mood and intensity level.
    
    Args:
        mood (str): The user's mood (e.g., "Happy", "Sad").
        level (int): The intensity level (1, 2, or 3).
    
    Returns:
        str: A recommended song or an error message.
    """
    mood = mood.capitalize()  # Ensure mood is capitalized
    if mood in song_recommendations:
        if level in song_recommendations[mood]:
            return random.choice(song_recommendations[mood][level])
        else:
            return "Invalid level. Please choose a level between 1 and 3."
    else:
        return "Invalid mood. Please choose a valid mood."