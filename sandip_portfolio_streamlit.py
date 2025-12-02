# sandip_portfolio_streamlit.py
import streamlit as st

# --- Personal Info ---
PERSONAL_INFO = {
    "name": "Sandip Madde",
    "title": "Process Engineer",
    "location": "Pune, India",
    "email": "Sandipomprakash@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sandipomprakash",
    "github": "https://github.com/yourusername",
    "bio": "Hi — Engineering professional with 8.5 years' experience in process design, plant operations, troubleshooting and optimization in ASU, hydrogen, gasification, and cryogenic systems. Expertise includes PFDs, P&IDs, simulations, equipment sizing, commissioning and FEED/Detailed Engineering with strong coordination and technical problem-solving skills."
}

# --- Work Experience ---
WORK_EXPERIENCE = [
    {
        "role": "Sr. Process Engineer",
        "company": "ENPRO Industries Pvt. Ltd., Pune 2nd Jan-2024 – Present",
        "description":"Prepared core engineering deliverables including PFDs, P&IDs, mass & energy balances, equipment datasheets, Instrument data sheets and utility consumption summaries. Led process engineering activities for Green Hydrogen, Pyrolysis, Gasification, and Electrochemical Hydrogen Compression projects."
    },
    {
        "role": "Proposal & Project Engineer",
        "company": "Economy Process Solutions Pvt Ltd, Chakan -Oct 2023 – Dec 2023",
        "description":"Prepared technical and commercial proposals for customized process skids. Developed PFDs, P&IDs, equipment layouts, GA drawings, and supported 3D modelling teams. Acted as single-point contact for customers and internal sales teams throughout project execution."
    },
    {
        "role": "Engineer-Operations",
        "company": "Inox Air Products Pvt Ltd - Dec 2021 – June 2023",
        "description":"Delivered detailed process engineering deliverables (PFD, P&ID, Line List, Equipment List, PDS, Instrument List) for 200 TPD Air Separation Unit (ASU). Conducted line sizing and pump hydraulic calculations, including preparation of mass & energy balances."
    }
]

# --- Layout ---
st.set_page_config(page_title=f"{PERSONAL_INFO['name']} Portfolio", page_icon=":tada:", layout="wide")

# Header
st.title(PERSONAL_INFO["name"])
st.subheader(PERSONAL_INFO["title"])
st.write(f"{PERSONAL_INFO['location']} • [{PERSONAL_INFO['email']}](mailto:{PERSONAL_INFO['email']})")
st.write(PERSONAL_INFO["bio"])

# Photo
st.image("photo.jpg", width=200)  # Make sure photo.jpg is in the same folder

# Social links
st.markdown(f"[LinkedIn]({PERSONAL_INFO['linkedin']}) | [GitHub]({PERSONAL_INFO['github']})")

# Work Experience
st.header("Work Experience")
for w in WORK_EXPERIENCE:
    st.subheader(w["role"])
    st.write(w["company"])
    st.write(w["description"])
    st.markdown("---")

# Contact Form
st.header("Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks! Your message has been sent.")
        # Optional: Add code to email this or save to Google Sheets
