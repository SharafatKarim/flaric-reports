# Flaric Reports 📊

Welcome to the **Flaric Reports** repository! This project is built with Streamlit, leveraging Google Sheets to collect and manage complaints and suggestions for **Rising Flare**. This simple, privacy-focused platform allows users to submit feedback confidentially, which is then logged in a secure Google Sheet.

## About the Project

**Flaric Reports** is designed as a complaint and suggestion portal for **Rising Flare**. The platform respects user privacy: no personal information is stored, and all feedback is handled confidentially. Users can submit feedback using a simple form, and the information is updated in real time to a Google Sheet for easy tracking and review.

## Key Features

- 📄 **Privacy-Centered Design**: No name, ID, or any other personal data is stored.
- 🌐 **Multilingual Interface**: Interface is available in both Bengali and English.
- 📊 **Real-Time Data Management**: New feedback entries are instantly updated in Google Sheets.
- 🔐 **Confidentiality**: All feedback is securely stored and accessible only to authorized personnel.

## Tech Stack

- **Python**
- **Streamlit** for the frontend
- **Google Sheets API** (via `streamlit_gsheets`) for data storage
- **Pandas** for data handling

## Setup Instructions

To run the application locally, follow these steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/SharafatKarim/flaric-reports.git
cd flaric-reports
```

2. Install Dependencies: Make sure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt
```

3. Set Up Google Sheets Connection:

- Set up a Google Cloud project and enable the Google Sheets API.
- Generate credentials for API access and save the credentials JSON in the project folder.
- Update streamlit_app.py to point to your Google Sheets connection.

4. Run the Application:

```bash
streamlit run streamlit_app.py
```

5. Usage

Open the Streamlit app in your browser (default: <http://localhost:8501>).
Fill in the required fields:

- Title (e.g., Cannot find resources)
- Description (Provide a detailed description of the issue)
- Submit your feedback.

> The information will be instantly updated in the connected Google Sheet.

## Contributing

We welcome contributions! To contribute:

- Fork this repository.
- Create a new branch (feature/YourFeature).
- Commit your changes.
- Open a pull request.

For major changes, please open an issue first to discuss the proposed modifications.
License

> This project is licensed under the MIT License.
