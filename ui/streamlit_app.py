import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Piano Coach", page_icon="🎹")

st.title("🎹 AI Piano Coach")
st.write("A small agent-based piano learning assistant.")

st.sidebar.header("Learning Profile")

level = st.sidebar.selectbox("Level", ["beginner"])
goal = st.sidebar.text_input("Goal", "play Happy Birthday")
weeks = st.sidebar.slider("Weeks", 1, 4, 4)
daily_minutes = st.sidebar.slider("Minutes per day", 5, 60, 20)
current_week = st.sidebar.slider("Current week", 1, weeks, 1)

st.header("1. Create Learning Plan")

if st.button("Create Plan"):
    response = requests.post(
        f"{API_URL}/plan",
        json={
            "level": level,
            "goal": goal,
            "weeks": weeks,
            "daily_minutes": daily_minutes,
        },
    )

    data = response.json()

    st.subheader("Learning Plan")
    for week in data["curriculum_plan"]["weeks"]:
        st.markdown(f"### Week {week['week']}: {week['title']}")
        st.write(f"Daily practice: {week['daily_minutes']} minutes")
        for topic in week["topics"]:
            st.write(f"- {topic}")

st.divider()

st.header("2. Today’s Exercise")

if st.button("Generate Exercise"):
    with st.spinner("Generating lesson with Ollama LLM..."):
        response = requests.post(
            f"{API_URL}/exercise",
            json={
                "level": level,
                "goal": goal,
                "weeks": weeks,
                "daily_minutes": daily_minutes,
                "current_week": current_week,
            },
        )

    data = response.json()
    exercise = data["exercise"]

    st.session_state["exercise"] = exercise

if "exercise" in st.session_state:
    exercise = st.session_state["exercise"]

    st.subheader(exercise["title"])
    st.write("**Topic:**", exercise["topic"])

    if "generated_lesson" in exercise:
        st.markdown("## 🤖 AI-generated lesson")
        st.markdown(exercise["generated_lesson"])

    st.write("**Question:**", exercise["question"])
    st.info(exercise["hint"])

    user_answer = st.text_input("Your answer")

    if st.button("Check Answer"):
        response = requests.post(
            f"{API_URL}/evaluate",
            json={
                "level": level,
                "goal": goal,
                "weeks": weeks,
                "daily_minutes": daily_minutes,
                "current_week": current_week,
                "user_answer": user_answer,
            },
        )

        result = response.json()

        st.subheader("Feedback")
        st.write(result["feedback"]["feedback"])

        st.subheader("Progress")
        st.write(f"Correct answers: {result['progress']['correct_answers']}")
        st.write(f"Total answers: {result['progress']['total_answers']}")
        st.write(f"Accuracy: {result['progress']['accuracy']}%")

        st.success(result["motivation"])

        with st.expander("Show agent flow"):
            st.write(" → ".join(result["agent_flow"]))