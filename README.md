# Socratic_agent
Socratic Chatbot for Data Structures and Algorithms

Overview

This project is a Socratic method-based chatbot designed to help students learn Data Structures and Algorithms (DSA) concepts by guiding them through step-by-step questions. The chatbot focuses on teaching problem-solving techniques in a way that leads the user toward discovering the answer on their own, rather than giving the solution directly.

Features

Socratic Method: The chatbot asks probing questions to guide students to the correct solution instead of providing direct answers.
Interactive Learning: Focuses on understanding performance issues, code optimization, and various DSA concepts.
Personalized Learning Path: Adaptively helps students tackle problem-solving based on their responses.
Real-Time Feedback: Provides instant feedback on code performance, specifically around timeouts and optimizations.
Dataset with Clue-based Learning: The dataset includes clues that lead to answers, designed to engage users and help them learn the concepts deeply.

Tech Stack

Frontend: HTML, React, Tailwind CSS
Backend: Python, Flask
Database: MongoDB
AI Integration: Google Generative AI (Gemini API)
Hosting/Deployment: Vercel or Netlify
Getting Started

Prerequisites

Python: Make sure Python 3.x is installed on your local machine.
MongoDB: A MongoDB database for storing user interactions and learning sessions.
Google Generative AI API (Gemini): Integrated for the AI-driven Socratic method.
Installation
Clone the repository:
Copy code
git clone https://github.com/yourusername/socratic-chatbot-dsa.git
cd socratic-chatbot-dsa
Install the required Python dependencies:
Copy code
pip install -r requirements.txt
Set up MongoDB for storing conversation history and user interactions.
Refer to MongoDB documentation for setting up a local database or use a cloud solution.

Create an .env file in the root directory and add your API keys and MongoDB connection string:

makefile
Copy code
GOOGLE_API_KEY=<your-google-api-key>
MONGO_URI=<your-mongodb-uri>
Running the Application
Start the Flask backend server:

bash
Copy code
python app.py
Navigate to the frontend directory and install React dependencies:

bash
Copy code
cd frontend
npm install
Start the React development server:

bash
Copy code
npm start


Using the Socratic Chatbot

Once the server is running, open your browser and navigate to http://localhost:3000/.
Start interacting with the chatbot by asking questions related to DSA topics.
The chatbot will engage you in a Socratic method of learning, asking relevant questions based on your input and guiding you toward understanding.
Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

Google Generative AI (Gemini API) for providing advanced language understanding and generation capabilities.
MongoDB for offering a robust and scalable database solution.
React and Tailwind for building a responsive and modern frontend interface.
