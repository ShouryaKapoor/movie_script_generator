def generate_movie_script(prompt):
    import requests

    # Define the endpoint for Google Generative AI
    endpoint = "https://api.google.com/generative-ai/v1/generate"

    # Set up the headers with your API key
    headers = {
        "Authorization": "AIzaSyBtYB7Da8VNN8paGnsA2fSNx69UqYfTXao",
        "Content-Type": "application/json"
    }

    # Create the payload with the prompt
    payload = {
        "prompt": prompt,
        "max_tokens": 500,  # Adjust the token limit as needed
        "temperature": 0.7   # Adjust the creativity level
    }

    # Send the request to the Google Generative AI API
    response = requests.post(endpoint, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        script = response.json().get("generated_text", "")
        return script
    else:
        # Handle errors
        return f"Error: {response.status_code} - {response.text}"