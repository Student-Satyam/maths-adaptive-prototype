Math Adventures — AI-Powered Adaptive Learning Prototype
Math Adventures is a minimal adaptive learning system designed to help children (ages 5–10) practice basic math concepts. The prototype demonstrates how AI-driven logic can dynamically personalize learning difficulty based on learner performance.

The primary focus of this project is the adaptive engine, not UI complexity.

Features
Dynamic math puzzle generation
Three difficulty levels: Easy, Medium, Hard
Performance tracking using accuracy and response time
Rule-based adaptive difficulty adjustment
End-of-session performance summary
Simple Streamlit-based interface
Adaptive Learning Logic
The system continuously evaluates recent learner performance and adjusts difficulty to keep the learner in an optimal challenge zone:

Difficulty increases when accuracy ≥ 80% and average response time ≤ 5 seconds
Difficulty decreases when accuracy ≤ 50% or average response time ≥ 10 seconds
Difficulty remains unchanged otherwise
A sliding window of recent responses is used to ensure stability and reduce noise.

Project Structure
math-adaptive-prototype/ ├── src/ │ ├── main.py # Streamlit application │ ├── puzzle_generator.py # Math problem generator │ ├── tracker.py # Performance tracking │ └── adaptive_engine.py # Adaptive difficulty logic ├── README.md └── requirements.txt

How to Run
Install dependencies:
pip install -r requirements.txt


Run the application:

streamlit run src/main.py


The app will open automatically in your web browser.

Performance Metrics Tracked

Correct and incorrect responses

Response time per question

Accuracy trends over recent questions

Difficulty transitions

Design Decisions

Rule-based adaptation was chosen for simplicity, explainability, and effectiveness with limited data.

Streamlit enables rapid prototyping while keeping the focus on learning logic.

Minimal dependencies ensure easy setup and reproducibility.

Future Enhancements

Machine learning-based difficulty prediction

Expansion to other learning domains beyond math

Persistent learner profiles and progress tracking

Enhanced analytics and visualizations

Author

Satyam Singh

License

This project is intended for educational and evaluation purposes only.