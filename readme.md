This is the ultimate super chatbot for Prisma AIRS demo purposes.

1. Download Root CA certificate which you are using with decryption from Strata Cloud Manager.
  
2. Copy single signed Root CA certificate to your Ubuntu box and set it as trusted. Copy pem file to /usr/local/share/ca-certificates/ folder with name decrypt.pem

3. Run following commands
   
    dccrt=/usr/local/share/ca-certificates/decrypt.pem
    export SSL_CERT_FILE=$dccrt
    export REQUESTS_CA_BUNDLE=$dccrt
    export GRPC_DEFAULT_SSL_ROOTS_FILE_PATH=$dccrt

4. Clone this repo to user Ubuntu box

5. Install dotenv and openai python libraries with pip
    pip install dotenv
    pip install openai

6. Deploy your LLM with Azure AI Foundry

7. Get API key, endpoint, api version information from the Azure AI Foundry

8. Set API key and API endpoint with commands:
    export AZURE_OPENAI_API_KEY="XXXXXXXX"
    export AZURE_OPENAI_ENDPOINT="https://endpointname_openai.openai.azure.com/"

9. Modify app.py with your api version information.

10. Fire up the app with "flask run -p 8080 --host=0.0.0.0"

11. Now the Super Chatbot should be accessible via TCP port 8080  
