import streamlit as st

# --- Personal Info ---
PERSONAL_INFO = {
    "Greeting": "Welcome To My Profile, You Have Landed To",
    "name": "Sandip Madde Portfolio",
    "title": "Process Engineer",
    "location": "Pune, India",
    "email": "Sandipomprakash@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sandipomprakash",
    "github": "https://github.com/yourusername",
    "bio": """Hi.. I'm an Engineering professional with 8.5 years' experience in process design, plant operations, troubleshooting
            and optimization in ASU, hydrogen, gasification, and cryogenic systems. Expertise includes PFDs, P&IDs, simulations,
           equipment sizing, commissioning and FEED/Detailed Engineering with strong coordination and technical problem-solving skills."""
}

# --- Work Experience ---
WORK_EXPERIENCE = [
    {
        "role": "Sr. Process Engineer",
        "company": "ENPRO Industries Pvt. Ltd., Pune (2nd Jan 2024 – Present)",
        "description": """
• Prepared core engineering deliverables including PFDs, P&IDs, mass & energy balances, equipment datasheets, instrument datasheets, and utility consumption summaries.
• Leading process engineering for Green Hydrogen, Pyrolysis, Gasification, and Electrochemical Hydrogen Compression projects.
• Executed FEED & Detailed Design for complete Balance of Plant (BoP) packages.
• Designed and rated shell & tube heat exchangers; performed technical vendor reviews.
• Supported proposal engineering and contributed to technical bids and design philosophies.
• Hands-on experience with AutoCAD, Inventor, SolidWorks, and Navisworks.
• Served as primary technical contact for international clients.
• Ensured QA/QC compliance and contributed to process document standardization.
"""
    },
    {
        "role": "Proposal & Project Engineer",
        "company": "Economy Process Solutions Pvt Ltd, Chakan (Oct 2023 – Dec 2023)",
        "description": """
• Prepared technical and commercial proposals for process equipment skids.
• Developed PFDs, P&IDs, equipment layouts, GA drawings, and supported 3D modeling.
• Created equipment datasheets for pumps, heat exchangers, valves, motors, and instruments.
• Single-point contact for customers and internal sales teams.
• Coordinated fabrication, document control, and cost tracking.
• Tools used: AutoCAD, SolidWorks, Navisworks.
"""
    }
]

EDUCATION = [
    {"info": "• B.E. in Chemical Engineering from PVPIT, Sangli (Shivaji University Kolhapur 2012-216) with aggregate 66.81%"}
]

CERTIFICATION = [
    {"info": "• Process Design Engineering from SB Technologies, Mumbai an ISO  9001:2015 Certified training center"}
]

ACADEMIC_PROJECTS_AND_SEMINARS = [
    {"Title": "• Design of Agitation vessel"}
]

PERSONAL_ATTRIBUTES_and_SKILLS = [
    {
        "info1": "• Co-operative nature & like to work with team.",
        "info2": "• Positive attitude.",
        "info3": "• Ready to learn new ideas and technical knowledge.",
        "info4": "• Quick learner, versatile and ability to manage several assignments simultaneously."
    }
]

# --- Layout ---
st.set_page_config(page_title=f"{PERSONAL_INFO['name']} Portfolio", page_icon=":tada:", layout="wide")

# --- Initialize session_state for navigation ---
if "section" not in st.session_state:
    st.session_state.section = "Home"

# --- Fade in Greeting ---
st.markdown(
    f"""
    <style>
    .fade-text {{
        font-size: 32px;
        font-weight: 700;
        text-align: center;
        animation: fadeInOut 3s infinite;
        color: #4a4a4a;
        margin-top: 20px;
    }}
    @keyframes fadeInOut {{
        0% {{ opacity: 0; }}
        50% {{ opacity: 1; }}
        100% {{ opacity: 0; }}
    }}
    </style>
    <div class="fade-text">{PERSONAL_INFO['Greeting']}</div>
    """,
    unsafe_allow_html=True
)

# --- Top Navigation Buttons ---
cols = st.columns(6)
with cols[0]:
    if st.button("Home"):
        st.session_state.section = "Home"
with cols[1]:
    if st.button("Work Experience"):
        st.session_state.section = "Work Experience"
with cols[2]:
    if st.button("Education"):
        st.session_state.section = "Education"
with cols[3]:
    if st.button("Certification"):
        st.session_state.section = "Certification"
with cols[4]:
    if st.button("Projects"):
        st.session_state.section = "Projects"
with cols[5]:
    if st.button("Skills"):
        st.session_state.section = "Skills"

# --- Home Section ---
if st.session_state.section == "Home":
    st.title(PERSONAL_INFO["name"])
    st.subheader(PERSONAL_INFO["title"])
    st.write(f"{PERSONAL_INFO['location']} • [{PERSONAL_INFO['email']}](mailto:{PERSONAL_INFO['email']})")
    st.write(PERSONAL_INFO["bio"])
    st.image("photo.jpg", width=200)
    st.markdown(f"[LinkedIn]({PERSONAL_INFO['linkedin']}) | [GitHub]({PERSONAL_INFO['github']})")

# --- Work Experience Section ---
elif st.session_state.section == "Work Experience":
    st.header("Work Experience")
    for w in WORK_EXPERIENCE:
        st.subheader(w["company"])
        st.markdown(f"**{w['role']}**")
        st.write(w["description"])
        st.markdown("---")

# --- Education Section ---
elif st.session_state.section == "Education":
    st.header("Education")
    for e in EDUCATION:
        st.write(e["info"])

# --- Certification Section ---
elif st.session_state.section == "Certification":
    st.header("Certification")
    for c in CERTIFICATION:
        st.write(c["info"])

# --- Projects Section ---
elif st.session_state.section == "Projects":
    st.header("Academic Projects & Seminars")
    for a in ACADEMIC_PROJECTS_AND_SEMINARS:
        st.write(a["Title"])

# --- Skills Section ---
elif st.session_state.section == "Skills":
    st.header("Personal Attributes & Skills")
    for p in PERSONAL_ATTRIBUTES_and_SKILLS:
        st.write(p["info1"])
        st.write(p["info2"])
        st.write(p["info3"])
        st.write(p["info4"])

# --- Contact Form (Always visible at bottom) ---
st.header("Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! Your message has been sent.")
