import os
from datetime import date

import pandas as pd
import streamlit as st


# ======================= PROFILE DATA ==========================
NAME = "Talledo, Mike Joseph V."
SECTION = "CSIT 349 - Section F1"
PROGRAM = "BS Your Program, Year 3" 
TAGLINE = "Turning ideas into code, one line at a time.."
EMAIL = "mikejosephtalledo@gmail.com"
GITHUB = "https://github.com/nameless1016"
LINKEDIN = "https://www.linkedin.com/in/mikejosephtalledo/"
PHOTO_PATH = "2x2 pic.jpg"
EXTRA = (
    "I am a highly motivated and enthusiastic individual with a strong passion for technology and innovation.\n "
    "I have a keen interest in exploring new technologies and finding creative solutions to complex problems.\n"
    "I am a quick learner and enjoy taking on new challenges that allow me to expand my knowledge and skills.\n "
    "I am also a team player and enjoy collaborating with others to achieve common goals.\n\n"
    "In my free time, I enjoy reading about the latest trends in technology, playing video games, and exploring the outdoors.\n"
)


BIO_SHORT = (
    "HELLLLO, I'm Mike Joseph V. Talledo, a passionate and dedicated individual with a strong interest in technology and innovation. "
)

MILESTONES = {
    2006: "Born on March 20, 2006 in Negros Oriental.",
    2016: "Started Coding with HTML/CSS as first languages", 
    2018: "Graduated from elementary school. School: Sage Prep Schoolhouse",
    2022: "Graduated Junior High School: Still at Sage Prep Schoolhouse",
    2024: "Graduate Senior High School. School: University Of Cebu Main Campus",
    2026: "Currently Enrolled Computer Science. School: Cebu Institute of Technology - University",
}

EDUCATION = [
    {"Level": "College", "School": "TODO", "Years": "2024 - present"},
    {"Level": "Senior High", "School": "TODO", "Years": "2022 - 2024"},
    {"Level": "Junior High", "School": "TODO", "Years": "2018 - 2022"},
]

INTERESTS = ["Game Development", "Outdoor Activities/Sports", "Machine Learnning", "Robotics"]

SKILLS = pd.DataFrame(
    {
        "Skill": ["Python", "SQL", "Web Dev", "Game Development", "Data Analysis", "Communication", "Teamwork"],
        "Level": [55, 65, 40, 85, 75, 80, 85],
        "Category": ["Programming", "Programming", "Programming", "Programming", "Programming", "Soft", "Soft"],
    }
)

PROJECTS = [
    {
        "title": "Encore",
        "role": "Programmer",
        "tools": ["GDScript, Godot Game Engine"],
        "outcome": "Featured In WildCats PlayLab 2026",
        "link": "https://asterialumi.itch.io/encore",
    },
    {
        "title": "[Un]-Becoming",
        "role": "Programmer",
        "tools": ["GDScript, Godot Game Engine"],
        "outcome": "Not Finished yet, but to be submitted for Global Game Jam 2026",
        "link": "",
    },
]

# ======================= PAGE SETUP ============================
st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Session state: visit counter and saved messages
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1
if "messages" not in st.session_state:
    st.session_state.messages = []

# Light custom styling
st.markdown(
    """
    <style>
    .hero {padding: 1.5rem 2rem; border-radius: 16px;
           background: linear-gradient(135deg, #4F46E5, #9333EA); color: white;}
    .hero h1 {color: white; margin-bottom: 0;}
    .hero p {margin-top: .25rem; font-size: 1.1rem; opacity: .9;}
    </style>
    """,
    unsafe_allow_html=True,
)


def show_photo(width=None):
    """Show the photo if it exists, else a clearly labeled stand-in."""
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, caption=NAME, width=width, use_container_width=width is None)
    else:
        st.info("📷 Placeholder: add photo.jpg next to app.py")


# ======================= SIDEBAR ===============================
with st.sidebar:
    show_photo()
    st.header(NAME)
    st.caption(f"{PROGRAM}\n\n{SECTION}")
    st.divider()

    st.subheader("Quick links")
    st.link_button("GitHub", GITHUB, use_container_width=True)
    st.link_button("LinkedIn", LINKEDIN, use_container_width=True)
    st.divider()

    st.subheader("Settings")
    show_balloons = st.checkbox("Celebrate when I send a message", value=True)
    theme_choice = st.radio("Chart style", ["Bar", "Line"], horizontal=True)
    st.divider()
    st.metric("Page views this session", st.session_state.visits)

# ======================= HEADER ================================
st.markdown(
    f"""
    <div class="hero">
        <h1>{NAME}</h1>
        <p>{TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Skills tracked", len(SKILLS))
m3.metric("Avg. skill level", f"{SKILLS['Level'].mean():.0f}/100")
m4.metric("Year", date.today().year)

# ======================= TABS ==================================
tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    ["🙋 About", "📖 Autobiography", "🛠️ Skills", "💼 Projects", "✉️ Contact"]
)

# ---------- ABOUT ----------
with tab_about:
    c1, c2 = st.columns([1, 2])
    with c1:
        show_photo()
    with c2:
        st.header("About me")
        st.write(BIO_SHORT)
        st.subheader("Interests")
        chosen = st.multiselect("Pick the ones you want to see", INTERESTS, default=INTERESTS)
        for item in chosen:
            st.markdown(f"- {item}")

# ---------- AUTOBIOGRAPHY ----------
with tab_story:
    st.header("My story")

    st.subheader("Timeline")
    years = sorted(MILESTONES)
    year = st.select_slider("Drag through my life", options=years, value=years[-1])
    st.success(f"**{year}**: {MILESTONES[year]}")

    st.subheader("Background")
    st.write("TODO: Write your background in your own words: where you grew up, family, what shaped you.")

    st.subheader("Education")
    st.table(pd.DataFrame(EDUCATION))

    with st.expander("More about me"):
        st.write(EXTRA)

# ---------- SKILLS ----------
with tab_skills:
    st.header("Skills")
    st.write("TODO: A sentence or two about how you learned these and what you want to improve.")

    category = st.selectbox("Category", ["All"] + sorted(SKILLS["Category"].unique()))
    min_level = st.slider("Minimum level", 0, 100, 0)

    view = SKILLS if category == "All" else SKILLS[SKILLS["Category"] == category]
    view = view[view["Level"] >= min_level]

    left, right = st.columns(2)
    with left:
        st.subheader("Table")
        st.dataframe(view, use_container_width=True, hide_index=True)
    with right:
        st.subheader("Chart")
        chart_data = view.set_index("Skill")[["Level"]]
        if theme_choice == "Bar":
            st.bar_chart(chart_data)
        else:
            st.line_chart(chart_data)

    st.subheader("Progress bars")
    for _, row in view.iterrows():
        st.progress(int(row["Level"]), text=f"{row['Skill']}: {row['Level']}/100")

# ---------- PROJECTS ----------
with tab_projects:
    st.header("Projects")
    all_tools = sorted({t for p in PROJECTS for t in p["tools"]})
    tool_filter = st.multiselect("Filter by tool", all_tools)

    shown = [p for p in PROJECTS if not tool_filter or set(tool_filter) & set(p["tools"])]
    if not shown:
        st.warning("No projects match that filter.")

    cols = st.columns(3)
    for i, p in enumerate(shown):
        with cols[i % 3]:
            with st.container(border=True):
                st.subheader(p["title"])
                st.markdown(f"**Role:** {p['role']}")
                st.markdown("**Tools:** " + ", ".join(f"`{t}`" for t in p["tools"]))
                st.write(p["outcome"])
                if p["link"]:
                    st.link_button("View project", p["link"])

# ---------- CONTACT ----------
with tab_contact:
    st.header("Get in touch")
    form_col, info_col = st.columns([2, 1])

    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            sender = st.text_input("Your name")
            sender_email = st.text_input("Your email")
            topic = st.selectbox("Topic", ["Feedback", "Collaboration", "Question", "Other"])
            rating = st.slider("How did you find this site?", 1, 5, 4)
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send")

        if submitted:
            if not sender or not message:
                st.error("Please enter your name and a message.")
            else:
                st.session_state.messages.append(
                    {"From": sender, "Topic": topic, "Rating": rating, "Message": message}
                )
                st.toast("Message sent!", icon="✅")
                st.success(f"Thanks, {sender}! I'll get back to you soon.")
                if show_balloons:
                    st.balloons()

    with info_col:
        st.subheader("Other ways to reach me")
        st.write(f"📧 {EMAIL}")
        st.write(f"🎓 {PROGRAM}")
        st.write(f"🏫 {SECTION}")
        st.link_button("📧 Email me directly", f"https://mail.google.com/mail/?view=cm&to={EMAIL}")
        st.code(EMAIL, language=None)

    if st.session_state.messages:
        st.subheader("Messages this session")
        st.dataframe(pd.DataFrame(st.session_state.messages), use_container_width=True, hide_index=True)

# ======================= FOOTER ================================
st.divider()
summary = f"{NAME}\n{PROGRAM}\n{SECTION}\n\n{BIO_SHORT}\n\nSkills:\n" + "\n".join(
    f"- {r.Skill}: {r.Level}/100" for r in SKILLS.itertuples()
)
f1, f2 = st.columns([3, 1])
f1.caption(f"© {date.today().year} {NAME} · {SECTION} · Built with Streamlit")
f2.download_button("⬇️ Download summary", summary, file_name="profile_summary.txt")
