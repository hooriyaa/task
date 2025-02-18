import streamlit as st
import random
import time
from datetime import datetime

# Custom Styling
st.markdown(
    """
    <style>
        /* Main Background Gradient */
        body {
            background: linear-gradient(135deg, #1a1a2e, #16213e);
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }

        /* Progress Bar Styling */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #ff6f61, #ffcc00);
            border-radius: 12px;
        }

        /* Button Styling */
        .stButton > button {
            border-radius: 12px;
            padding: 12px 24px;
            width: 100%;
            background: linear-gradient(90deg, #ff6f61, #ffcc00);
            color: white;
            font-weight: bold;
            border: none;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Text Area Styling */
        .stTextArea > div > div > textarea {
            background-color: #2e2e3e;
            color: #ffffff;
            border-radius: 12px;
            border: 2px solid #ff6f61;
            padding: 10px;
            transition: border-color 0.3s ease;
        }
        .stTextArea > div > div > textarea:focus {
            border-color: #ffcc00;
        }

        /* Radio Button Styling */
        .stRadio > div {
            background-color: #2e2e3e;
            padding: 15px;
            border-radius: 12px;
            border: 2px solid #ff6f61;
        }

        /* Header Styling */
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #ff6f61;
            margin-bottom: 10px;
        }

        /* Success Message Styling */
        .stSuccess {
            background: linear-gradient(90deg, #00cc66, #00b359);
            color: white;
            padding: 15px;
            border-radius: 12px;
            border: 2px solid #00cc66;
        }

        /* Warning Message Styling */
        .stWarning {
            background: linear-gradient(90deg, #ffcc00, #ffbb00);
            color: black;
            padding: 15px;
            border-radius: 12px;
            border: 2px solid #ffcc00;
        }

        /* Info Message Styling */
        .stInfo {
            background-color: #2e2e3e;
            color: white;
            padding: 15px;
            border-radius: 12px;
            border: 2px solid #ff6f61;
        }

        /* Card-like Styling for Sections */
        .stCard {
            background-color: #2e2e3e;
            padding: 20px;
            border-radius: 12px;
            border: 2px solid #ff6f61;
            margin-bottom: 20px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .stCard:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        /* Badge Styling */
        .badge {
            display: inline-block;
            background: linear-gradient(90deg, #ff6f61, #ffcc00);
            color: white;
            padding: 8px 16px;
            border-radius: 12px;
            margin: 5px;
            font-size: 14px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for user data
if "progress" not in st.session_state:
    st.session_state.progress = random.randint(30, 90)  # Simulated progress percentage
if "badges" not in st.session_state:
    st.session_state.badges = []
if "last_challenge_date" not in st.session_state:
    st.session_state.last_challenge_date = None
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "username" not in st.session_state:
    st.session_state.username = "User"
if "profile_pic" not in st.session_state:
    st.session_state.profile_pic = None
if "feedback" not in st.session_state:
    st.session_state.feedback = []

# Growth Mindset Content
tips = [
    "✨ Skills improve with effort and persistence!",
    "🚀 Mistakes are opportunities to learn.",
    "💡 Your brain grows stronger when you challenge yourself.",
    "🎯 Success comes from learning, not just talent.",
    "🔥 Effort and resilience lead to mastery."
]

challenges = [
    "✍️ Write down one new thing you learned today.",
    "🧩 Solve a problem using a different approach than usual.",
    "🤝 Encourage someone today and uplift their spirit.",
    "🔄 Reflect on a past failure and list three things you learned.",
    "🚀 Step out of your comfort zone and try something new!"
]

quiz_options = [
    "💪 I will try and learn!",
    "🤔 I will observe how others solve it.",
    "😞 I will give up; this isn’t for me."
]

motivational_quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt"
]

# UI Design
st.title("🌱 Growth Mindset Challenge")

# User Authentication
st.sidebar.header("User Profile")
st.session_state.username = st.sidebar.text_input("Enter your username:", st.session_state.username)
st.session_state.profile_pic = st.sidebar.file_uploader("Upload a profile picture:", type=["jpg", "png", "jpeg"])
if st.session_state.profile_pic:
    st.sidebar.image(st.session_state.profile_pic, width=100)

# Display Streak
st.sidebar.markdown(f"🔥 **Current Streak:** {st.session_state.streak} days")

# Leaderboard
st.sidebar.header("🏆 Leaderboard")
leaderboard = {"User1": 95, "User2": 80, "User3": 70}
for user, score in leaderboard.items():
    st.sidebar.write(f"{user}: {score}%")

# Growth Mindset Introduction
st.markdown(
    """
    <div class="stCard">
        <h2>🚀 What is Growth Mindset?</h2>
        <p>A growth mindset means that you believe your skills and abilities can improve through hard work, dedication, and learning.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Motivational Quote of the Day
st.markdown(
    """
    <div class="stCard">
        <h3>💬 Motivational Quote of the Day</h3>
        <p>{}</p>
    </div>
    """.format(random.choice(motivational_quotes)),
    unsafe_allow_html=True
)

# Growth Mindset Tips
if st.button("🌟 Get Growth Mindset Tips"):
    st.info(random.choice(tips))

# Thought Sharing
st.markdown(
    """
    <div class="stCard">
        <h3>📝 Share Your Thoughts</h3>
    </div>
    """,
    unsafe_allow_html=True
)
user_thought = st.text_area("How does a growth mindset help you?", height=100)
if user_thought:
    st.success("Thank you! Your thoughts have been shared.")

# Quiz Section
st.markdown(
    """
    <div class="stCard">
        <h2>🧠 Growth Mindset Quiz</h2>
        <p>If you face a difficult problem, what will you do?</p>
    </div>
    """,
    unsafe_allow_html=True
)
quiz_response = st.radio("Select an option:", quiz_options)

if quiz_response:
    if quiz_response == quiz_options[0]:
        st.success("✅ Absolutely correct! This is the essence of a growth mindset.")
    else:
        st.warning("🔄 Change your thinking! Every problem is an opportunity to learn.")

# Progress Bar
st.markdown(
    """
    <div class="stCard">
        <h2>📊 Your Growth Mindset Progress:</h2>
    </div>
    """,
    unsafe_allow_html=True
)
st.progress(st.session_state.progress / 100)

# Random Challenge Generator
st.markdown(
    """
    <div class="stCard">
        <h2>🎯 Daily Challenge</h2>
    </div>
    """,
    unsafe_allow_html=True
)
if st.button("Give me a challenge!"):
    today = datetime.today().date()
    if st.session_state.last_challenge_date != today:
        challenge = random.choice(challenges)
        st.session_state.last_challenge_date = today
        st.warning(challenge)
        st.session_state.progress = min(100, st.session_state.progress + 10)  # Increase progress
        st.session_state.streak += 1  # Increase streak
        if st.session_state.progress % 20 == 0:  # Award badges for every 20% progress
            badge = f"🏆 {st.session_state.progress}% Progress Badge"
            st.session_state.badges.append(badge)
            st.balloons()
            st.success(f"Badge Earned: {badge}")
    else:
        st.info("You've already completed today's challenge. Try again tomorrow!")

# Display Badges
if st.session_state.badges:
    st.markdown(
        """
        <div class="stCard">
            <h2>🏅 Your Badges</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    for badge in st.session_state.badges:
        st.markdown(f'<div class="badge">{badge}</div>', unsafe_allow_html=True)

# Feedback Section
st.markdown(
    """
    <div class="stCard">
        <h2>📝 Feedback</h2>
    </div>
    """,
    unsafe_allow_html=True
)
feedback = st.text_area("How can we improve this app?")
if st.button("Submit Feedback"):
    if feedback:
        st.session_state.feedback.append(feedback)
        st.success("Thank you! Your feedback is very valuable to us.")

# Motivation Section
if st.button("🔥 Need Motivation?"):
    with st.spinner("Processing..."):
        time.sleep(1.5)
    st.balloons()
    st.success("🚀 Keep Going! Adopt a growth mindset and always strive to learn. 💡")