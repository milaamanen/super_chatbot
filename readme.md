This is the ultimate super chatbot for Prisma AIRS demo purposes.

1. Copy single signed Root CA certificate to your Ubuntu box and set it as trusted.
2. Clone this repo to user Ubuntu box
3. Install dotenv and openai python libraries with pip
    pip install dotenv
    pip install openai 
4. Deploy your LLM with Azure AI Foundry
5. Get API key, endpoint, api version information from Azure AI Foundry
6. Set API key and API endpoint with commands:
    export AZURE_OPENAI_API_KEY="XXXXXXXX"
    export AZURE_OPENAI_ENDPOINT="https://endpointname_openai.openai.azure.com/"
7. Fire up the app with "flask run -p 8080 --host=0.0.0.0"
