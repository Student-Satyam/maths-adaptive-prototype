# This class keeps track of user performance
class PerformanceTracker:

    # Initialize empty list to store question history
    def __init__(self):
        self.history = []

    # Save result of each question
    def log(self, correct, response_time, difficulty):
        self.history.append({
            "correct": correct,           # True or False
            "time": response_time,        # Time taken to answer
            "difficulty": difficulty      # Easy / Medium / Hard
        })

    # Calculate accuracy and average time for recent questions
    def recent_performance(self, window=3):

        # Take last 'window' number of records
        recent = self.history[-window:]

        # Accuracy = correct answers / total answers
        accuracy = sum(r["correct"] for r in recent) / len(recent)

        # Average time taken
        avg_time = sum(r["time"] for r in recent) / len(recent)

        return accuracy, avg_time
