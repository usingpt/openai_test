import streamlit as st
import openai
import json

# Streamlit Community Cloud - get OpenAI API key in the Secrets
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

def get_fine_tune_status():
    # Retrieve the fine-tuning process details using the OpenAI package
    fine_tune = openai.FineTune.retrieve("ft-7R7ZQzwszShH08dXxbbiYldy")

    # Check if the status field exists in the response
    if 'status' not in fine_tune:
        print(f"*************Fine-tune Error: {fine_tune}")
        return None

    # Return the status and the fine-tuned model ID (if available)
    return fine_tune['status'], fine_tune.get('fine_tuned_model', None)

# Call the function to get the fine-tuning status and model ID
status, fine_tuned_model_id = get_fine_tune_status()
print(f"*************Fine-tune status: {status}")
print(f"*************Fine-tuned model ID: {fine_tuned_model_id}")