import streamlit as st
import openai
import json

# Streamlit Community Cloud - get OpenAI API key in the Secrets
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# https://www.ey.com/en_uk/consulting/financial-services-risk-management
file_name = "fine_tune.jsonl"
upload_response = openai.File.create(
	file=open(file_name, "rb"),
		purpose='fine-tune'
)
file_id = upload_response.id

print(file_id)
fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci")

print(fine_tune_response)

fine_tune_id = 'ft-GKqIJtdK16UMNuq555mREmwT'

def get_fine_tune_status():
    # Retrieve the fine-tuning process details using the OpenAI package
    fine_tune = openai.FineTune.retrieve(fine_tune_id)

    # Check if the status field exists in the response
    if 'status' not in fine_tune:
        print(f"Error: {fine_tune}")
        return None

    # Return the status and the fine-tuned model ID (if available)
    return fine_tune['status'], fine_tune.get('fine_tuned_model', None)

# Call the function to get the fine-tuning status and model ID
status, fine_tuned_model_id = get_fine_tune_status()
print(f"Fine-tune status: {status}")
print(f"Fine-tuned model ID: {fine_tuned_model_id}")