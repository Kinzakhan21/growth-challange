import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="★", layout="wide")

# Initialize session state for user inputs
if 'challenges' not in st.session_state:
    st.session_state['challenges'] = []
if 'reflections' not in st.session_state:
    st.session_state['reflections'] = []
if 'achievements' not in st.session_state:
    st.session_state['achievements'] = []

# Title and introduction
st.title("Growth Mindset Challenge: Web App With Streamlit")
st.subheader("🚀 Welcome to Your Growth Journey!")
st.write("This is a growth mindset project")

# Quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

# Challenge section
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if st.button("Add Challenge"):
    if user_input:
        st.session_state['challenges'].append(user_input)
        st.success(f"You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
    else:
        st.warning("Remember, every challenge is an opportunity for growth. 🌱")

# Display all challenges
if st.session_state['challenges']:
    st.write("### Your Challenges:")
    for challenge in st.session_state['challenges']:
        st.write(f"- {challenge}")

# Reflection section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write about what you learned today:")

if st.button("Add Reflection"):
    if reflection:
        st.session_state['reflections'].append(reflection)
        st.success(f"✨ Great Insight! Your reflection: {reflection}")
    else:
        st.warning("Take a moment to reflect on your learning. 🌱")

# Display all reflections
if st.session_state['reflections']:
    st.write("### Your Reflections:")
    for ref in st.session_state['reflections']:
        st.write(f"- {ref}")

# Motivational quote section
st.header("💪 Motivational Quote of the Day")
st.write("\"Believe you can and you're halfway there.\" - Theodore Roosevelt")

# Achievements section
st.header("🏆 Your Achievements")
achievement = st.text_input("Add a new achievement:")

if st.button("Add Achievement"):
    if achievement:
        st.session_state['achievements'].append(achievement)
        st.success(f"🎉 Congratulations! You've achieved: {achievement}")
    else:
        st.warning("Remember, every achievement is a step towards your goals. 🌱")

# Display all achievements
if st.session_state['achievements']:
    st.write("### Your Achievements:")
    for ach in st.session_state['achievements']:
        st.write(f"- {ach}")

# Progress tracker
st.header("🌟 Your Progress")

# Footer
st.write("---")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ⭐")
st.write("🌱 Thank you for using the Growth Mindset App! ❤️")
st.write("**📝 Created by Kinza Khan**")




      
