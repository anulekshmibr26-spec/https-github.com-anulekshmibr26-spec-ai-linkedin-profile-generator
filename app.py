import streamlit as st

st.set_page_config(page_title="AI LinkedIn Profile Generator", page_icon="💼")
st.title("💼 AI LinkedIn Profile Generator")
st.write("Create a professional LinkedIn profile draft from your details.")

with st.form("profile"):
    name = st.text_input("Your name")
    education = st.text_input("Education", placeholder="First-year ECE student")
    skills_text = st.text_input("Skills (comma-separated)", placeholder="Python, communication, teamwork")
    career = st.selectbox("Career goal", ["Electronics Engineer", "Software Developer", "AI / Machine Learning", "Embedded Systems Engineer", "Data Analyst", "Still exploring"])
    interests = st.text_input("Interests (optional)")
    submitted = st.form_submit_button("Generate LinkedIn Profile")

if submitted:
    if not name.strip() or not education.strip() or not skills_text.strip():
        st.error("Please enter your name, education, and at least one skill.")
    else:
        skills = [x.strip() for x in skills_text.split(",") if x.strip()]
        headlines = {
            "Electronics Engineer": "ECE Student | Interested in Electronics, Circuits & Embedded Systems",
            "Software Developer": "ECE Student | Python Learner | Aspiring Software Developer",
            "AI / Machine Learning": "Engineering Student | Exploring AI & Machine Learning",
            "Embedded Systems Engineer": "ECE Student | Interested in Embedded Systems & IoT",
            "Data Analyst": "Engineering Student | Developing Python & Data Analysis Skills",
            "Still exploring": "Engineering Student | Curious Learner | Exploring Technology",
        }
        headline = headlines[career]
        if any(x.lower() == "python" for x in skills):
            headline += " | Python"
        focus = interests.strip() or career.lower()
        about = (f"I am {name.strip()}, a {education.strip()} interested in {focus}. "
                 f"My current skills include {', '.join(skills)}. I enjoy learning new technologies, "
                 f"solving problems, and improving through practical work. I am working toward my goal "
                 f"of becoming a {career.lower()} and looking for opportunities to learn and collaborate.")
        st.success("Your profile draft is ready!")
        st.subheader("Suggested LinkedIn Headline")
        st.text_area("Headline", headline, height=90)
        st.subheader("About section")
        st.text_area("About", about, height=180)
        st.subheader("Skills to highlight")
        st.write(", ".join(skills))
        st.subheader("Suggested next steps")
        for item in [
            f"Build a small project related to {career.lower()}.",
            "Add the project to the Projects or Featured section of your LinkedIn profile.",
            "Follow professionals and organisations in your chosen field.",
            "Edit the draft so it accurately reflects your real experience."
        ]:
            st.markdown("- " + item)
        st.caption("Prototype note: This starter app uses templates and simple rules, not a live AI model or LinkedIn integration. Review all text before publishing.")
else:
    st.info("Enter your details and tap Generate LinkedIn Profile.")
