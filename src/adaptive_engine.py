# List of difficulty levels in order
LEVELS = ["Easy", "Medium", "Hard"]

# This function decides the next difficulty level
def adjust_difficulty(current_level, accuracy, avg_time):

    # Get current level index (Easy=0, Medium=1, Hard=2)
    index = LEVELS.index(current_level)

    # If user is doing very well → increase difficulty
    if accuracy >= 0.8 and avg_time <= 5:
        return LEVELS[min(index + 1, len(LEVELS) - 1)]

    # If user is struggling → decrease difficulty
    if accuracy <= 0.5 or avg_time >= 10:
        return LEVELS[max(index - 1, 0)]

    # Otherwise keep same difficulty
    return current_level
