import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyAzcoFa8C1kmiITDbdQLCMcaKBMV02dSJ0")


# Function to generate travel itinerary using chat session
def generate_itinerary(destination, days, nights):

    generation_config = {
        "temperature": 0.4,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }

    # Initialize Gemini model
    model = genai.GenerativeModel(
        model_name="models/gemini-2.5-flash",
        generation_config=generation_config
    )

    # Start chat session
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Write a travel itinerary to {destination} for {days} days and {nights} nights."
                ],
            }
        ]
    )

    # Send message to generate itinerary
    response = chat_session.send_message(
        f"""
        Create a detailed travel itinerary for {destination}.

        Trip Duration:
        - Days: {days}
        - Nights: {nights}

        Include:
        - Day-wise activities
        - Tourist attractions
        - Food recommendations
        - Travel tips
        """
    )

    return response.text


# Main function to run Streamlit app
def main():

    # Activity 1: Project Title
    st.title("Travel Itinerary Generator")

    # Activity 2: User Input Fields
    destination = st.text_input("Enter your desired destination:")
    days = st.number_input("Enter the number of days:", min_value=1)
    nights = st.number_input("Enter the number of nights:", min_value=0)

    # Generate button
    if st.button("Generate Itinerary"):

        # Validate input
        if destination.strip() and days > 0 and nights >= 0:
            try:
                itinerary = generate_itinerary(destination, days, nights)

                # Display output
                st.text_area("Generated Itinerary:", value=itinerary, height=300)

            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:
            st.error("Please make sure all inputs are provided and valid.")


# Run the application
if __name__ == "__main__":
    main()
