# healthBot.py - Complete First-Order Logic Healthcare Chatbot
# CMPG 313 Practical Assignment 4

def main():
    # Knowledge Base (FOL rules implemented as dictionary)
    KNOWLEDGE_BASE = {
        "flu": ["fever", "cough", "sore throat"],
        "common cold": ["sneezing", "runny nose", "mild fever"],
        "malaria": ["fever", "chills", "sweating", "headache"],
        "covid19": ["fever", "cough", "shortness of breath", "loss of taste"],
        "strep throat": ["sore throat", "swollen lymph nodes", "fever"]
    }

    # Advice Base (recommendations for each disease)
    ADVICE_BASE = {
        "flu": [
            "Drink plenty of water",
            "Stay at home and rest (get enough sleep)",
            "Consider pain relievers",
            "Consult a doctor if symptoms worsen"
        ],
        "common cold": [
            "Avoid sharing foods & drinks",
            "Use a humidifier",
            "Get plenty of rest",
            "Consider Over-the-Counter Medications"
        ],
        "malaria": [
            "Seek immediate medical attention",
            "Stay hydrated",
            "Prioritize avoiding mosquito bites",
            "Take prescribed antimalarial medication"
        ],
        "covid19": [
            "Seek medical advice if symptoms get worse",
            "Treat symptoms with over-the-counter medicines (acetaminophen or ibuprofen)",
            "Stay at home",
            "Rest and stay hydrated"
        ],
        "strep throat": [
            "See a doctor for antibiotics",
            "Gargle with warm salt water",
            "Avoid irritants",
            "Get plenty of rest"
        ]
    }

    print("Welcome to the HealthBot!")
    
    # Get and clean user input
    print("\nPlease enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").strip().lower()
    symptoms = [s.strip() for s in user_input.split(',')]
    
    # Diagnose possible diseases
    possible_diseases = []
    for disease, required_symptoms in KNOWLEDGE_BASE.items():
        if all(symptom in symptoms for symptom in required_symptoms):
            possible_diseases.append(disease)
    
    # Display results
    if not possible_diseases:
        print("\nNo specific diagnosis could be made based on your symptoms.")
        print("General advice: Rest and consult a doctor if symptoms persist.")
    else:
        print("\nBased on your symptoms, you might have:")
        for disease in possible_diseases:
            print(f"- {disease.capitalize()}")
            print("  Advice:")
            for advice in ADVICE_BASE.get(disease, []):
                print(f"  • {advice}")
    
    print("\nRemember: This is not a substitute for professional medical advice.")

if __name__ == "__main__":
    main()