import streamlit as st
import random
from datetime import datetime

# Sample data
challenges = [
    "Learn something new today and share it with someone.",
    "Embrace a mistake and reflect on what you learned from it.",
    "Try a task outside your comfort zone.",
    "Write down three things you're grateful for.",
    "Practice positive self-talk for 5 minutes.",
    "Ask for feedback on a project or task.",
    "Spend 10 minutes visualizing your goals.",
]

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
]

# App title
st.title("🌱 Growth Mindset Challenge")

# Sidebar for user info
st.sidebar.header("About You")
user_name = st.sidebar.text_input("Enter your name:")
if user_name:
    st.sidebar.write(f"Hello, {user_name}! Let's grow together!")

# Daily Challenge Section
st.header("🎯 Your Daily Challenge")
todays_challenge = random.choice(challenges)
st.write(f"**Challenge:** {todays_challenge}")

# Mark as Completed
if st.button("Mark as Completed"):
    st.success("Great job! You're one step closer to growth.")
    st.balloons()

# Motivational Quote Section
st.header("💬 Motivational Quote")
st.write(random.choice(quotes))

# Reflection Journal Section
st.header("📔 Reflection Journal")
reflection = st.text_area("Write a short reflection on today's challenge:")
if st.button("Save Reflection"):
    if reflection:
        st.write("Your reflection has been saved. Keep up the great work!")
    else:
        st.warning("Please write a reflection before saving.")

# Progress Tracker
st.header("📊 Progress Tracker")
progress = st.slider("How would you rate your progress today? (1 = Low, 10 = High)", 1, 10)
st.write(f"You rated your progress as: {progress}/10")

# Footer
st.markdown("---")
st.write("Made with ❤️ by [Syed Hassan Imam]")
