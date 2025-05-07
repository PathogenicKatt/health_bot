from knowledge_base import knowledge_base
from advice_base import advice_base

def main():
    print("Welcome to the HealthBot!")
    symptoms = get_user_symptoms()
    possible_diseases = diagnose(symptoms)
    display_results(possible_diseases)

def get_user_symptoms():
    print("Please enter your symptoms (comma-separated):")
    user_input = input("Symptoms: ").strip().lower()
    return [s.strip() for s in user_input.split(',')]

def diagnose(symptoms):
    possible_diseases = []
    
    for disease, conditions in knowledge_base.items():
        if all(symptom in symptoms for symptom in conditions):
            possible_diseases.append(disease)
    
    return possible_diseases

def display_results(diseases):
    if not diseases:
        print("\nNo specific diagnosis could be made based on your symptoms.")
        print("General advice: Rest and consult a doctor if symptoms persist.")
        return
    
    print("\nBased on your symptoms, you might have:")
    for disease in diseases:
        print(f"- {disease.capitalize()}")
        print("  Advice:")
        for advice in advice_base.get(disease, []):
            print(f"  • {advice}")

if __name__ == "__main__":
    main()