import streamlit as st
import random
import string
import math

# Function to evaluate password strength and provide feedback
def evaluate_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    feedback = []
    if length < 8:
        feedback.append("Password is too short.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_digit:
        feedback.append("Add numbers.")
    if not has_special:
        feedback.append("Add special characters.")

    # Determine strength
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Function to calculate password entropy
def calculate_entropy(password):
    pool_size = 0
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

# Function to generate a random password
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        return ''

    return ''.join(random.choice(char_pool) for _ in range(length))

# Streamlit app
st.set_page_config(page_title="Advanced Password Power Meter", layout="centered", initial_sidebar_state="expanded")

st.title("🔒 Advanced Password Power Meter")
st.markdown("Check the strength of your password and generate strong passwords with detailed feedback.")

# Password strength checker
st.subheader("Check Password Strength")
password = st.text_input("Enter your password", type="password")
if password:
    strength, feedback = evaluate_password_strength(password)
    entropy = calculate_entropy(password)
    st.write(f"Password Strength: **{strength}**")
    st.write(f"Password Entropy: **{entropy:.2f} bits**")
    if feedback:
        st.write("Feedback:")
        for item in feedback:
            st.write(f"- {item}")

# Password generator
st.subheader("Generate a Strong Password")
length = st.slider("Password Length", min_value=8, max_value=32, value=12)
use_upper = st.checkbox("Include Uppercase Letters", value=True)
use_lower = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_special = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Password"):
    new_password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    st.write(f"Generated Password: `{new_password}`")

# Dark theme styling
st.markdown(
    """
    <style>
    body {
        background-color: #2E2E2E;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)





      
