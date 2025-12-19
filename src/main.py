import streamlit as st
import time

from puzzle_generator import generate_problem
from tracker import PerformanceTracker
from adaptive_engine import adjust_difficulty

# App Title
st.title("🧠 Math Adventures – Adaptive Learning by Satyam")

# Initialize session state
if "level" not in st.session_state:
    st.session_state.level = "Easy"
    st.session_state.tracker = PerformanceTracker()
    st.session_state.problem = None
    st.session_state.answer = None
    st.session_state.start_time = None
    st.session_state.question_count = 0
    st.session_state.answered = False

# Display current difficulty
st.subheader(f"Current Difficulty: {st.session_state.level}")

# Generate a new problem if none exists
if st.session_state.problem is None:
    problem, answer = generate_problem(st.session_state.level)
    st.session_state.problem = problem
    st.session_state.answer = answer
    st.session_state.start_time = time.time()

# Show problem
st.markdown("### Solve this:")
st.markdown(f"**{st.session_state.problem}**")

# User input
user_answer = st.number_input("Your answer:", step=1)

# Submit Answer button (only if not answered yet)
if not st.session_state.answered:
    if st.button("Submit Answer"):
        response_time = time.time() - st.session_state.start_time
        correct = user_answer == st.session_state.answer

        # Log performance
        st.session_state.tracker.log(
            correct,
            response_time,
            st.session_state.level
        )

        st.session_state.question_count += 1
        st.session_state.answered = True

        # Adaptive logic after minimum questions
        if len(st.session_state.tracker.history) >= 3:
            accuracy, avg_time = st.session_state.tracker.recent_performance()
            st.session_state.level = adjust_difficulty(
                st.session_state.level,
                accuracy,
                avg_time
            )

        # Feedback
        if correct:
            st.success("✅ Correct!")
        else:
            st.error("❌ Incorrect")

# Next Question button (only after answering)
if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.problem = None
        st.session_state.answer = None
        st.session_state.start_time = None
        st.session_state.answered = False
        st.rerun()


# Session summary after 10 questions
if st.session_state.question_count >= 10:
    accuracy, avg_time = st.session_state.tracker.recent_performance(
        len(st.session_state.tracker.history)
    )

    st.markdown("---")
    st.header("📊 Session Summary")
    st.write(f"**Accuracy:** {accuracy * 100:.1f}%")
    st.write(f"**Average Time:** {avg_time:.2f} seconds")
    st.write(f"**Recommended Level:** {st.session_state.level}")
