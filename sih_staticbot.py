import streamlit as st

class AyurvedicChatbot:
    def __init__(self):
        self.prakriti = None

    def classify_prakriti(self, response_dict):
        if response_dict["cold_dry_constipation"]:
            self.prakriti = "Vata"
        elif response_dict["intense_appetite_irritation"]:
            self.prakriti = "Pitta"
        else:
            self.prakriti = "Kapha"

def main():
    st.title("Ayurvedic Prakriti Classification Chatbot")

    st.write("I will ask you a series of questions to determine your Prakriti.")
    st.write("Please answer with 'Yes' or 'No'.")

    chatbot = AyurvedicChatbot()
    responses = {}

    cold_dry_constipation = st.radio("Do you often feel cold, have dry skin, or experience constipation?", ("Yes", "No"))
    responses["cold_dry_constipation"] = (cold_dry_constipation == "Yes")

    if cold_dry_constipation == "No":
        intense_appetite_irritation = st.radio("Do you tend to have an intense appetite and get easily irritated?", ("Yes", "No"))
        responses["intense_appetite_irritation"] = (intense_appetite_irritation == "Yes")

    classify_button = st.button("Classify Prakriti")

    if classify_button:
        chatbot.classify_prakriti(responses)
        st.write(f"Based on your responses, your Prakriti is {chatbot.prakriti}.")

if __name__ == "__main__":
    main()
