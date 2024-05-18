Here is a step-by-step guide to setting up the project, integrating the Gemini API, and connecting it to Dialogflow CX using Ngrok:

1. **Fork and Clone the Project:**
   - Fork the project repository on GitHub.
   - Clone the repository to your local machine using Visual Studio Code (VSCode) or IntelliJ IDEA.
     ```bash
     git clone <your-forked-repo-url>
     ```
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```

2. **Add Your API Key:**
   - In the project directory, locate the `helper/gemini_api.py` file.
   - Generate an API key for your Google Cloud Platform (GCP) project at [Google API Key](https://aistudio.google.com/app/apikey).
   - Add the generated API key to `helper/gemini_api.py`.

3. **Set Up a Virtual Environment:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```

4. **Install Required Packages:**
   - Install Flask and OpenAI:
     ```bash
     pip install Flask openai
     ```

5. **Set Up Ngrok:**
   - Download Ngrok from [Ngrok Setup](https://dashboard.ngrok.com/get-started/setup) and unzip it.
   - In a separate terminal, run Ngrok on port 5000:
     ```bash
     ngrok http 5000
     ```
   - Copy the generated Ngrok URL (e.g., `http://abcd1234.ngrok.io`).

6. **Configure Dialogflow CX:**
   - In Dialogflow CX, add the Ngrok URL with the path `/dialogflow/cx/receiveMessage` to your webhooks.
     - Example: `http://abcd1234.ngrok.io/dialogflow/cx/receiveMessage`
   - Enable the webhook in the Default Fallback or Welcome Intent and specify the webhook name created above.

7. **Run the Flask Application:**
   - Run the following command to start the Flask server:
     ```bash
     python run.py
     ```

8. **Test the Integration:**
   - Make a request to your Dialogflow CX agent.
   - The request will be forwarded to your local server through the Ngrok URL, and the Gemini API will respond back to Dialogflow CX.

These steps ensure that your local server can handle requests from Dialogflow CX through Ngrok, enabling seamless integration and response handling.
