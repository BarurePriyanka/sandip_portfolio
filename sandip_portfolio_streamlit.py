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
    "bio": """Hi — Engineering professional with 8.5 years' experience in process design, plant operations, troubleshooting
            and optimization in ASU, hydrogen, gasification, and cryogenic systems. Expertise includes PFDs, P&IDs, simulations,
           equipment sizing, commissioning and FEED/Detailed Engineering with strong coordination and technical problem-solving skills."""
}

# --- Work Experience ---
WORK_EXPERIENCE = [
    {
        "role": "Sr. Process Engineer",
        "company": "ENPRO Industries Pvt. Ltd., Pune 2nd Jan-2024 – Present",
        "description":"""Experienced in preparing core engineering deliverables (PFDs, P&IDs, MEBs, datasheets, and utility summaries) and
                      leading process engineering for Green Hydrogen, Pyrolysis, Gasification, and hydrogen compression projects. Delivered
                      FEED and Detailed Design for BoP systems, designed and rated heat exchangers, and handled technical vendor evaluations.
                      Skilled in AutoCAD, Inventor, SolidWorks, and Navisworks for process layouts. Supported proposals, prepared technical documents,
                      coordinated with international clients, and ensured QA/QC compliance while improving design standards and workflows."""
    },
    {
        "role": "Proposal & Project Engineer",
        "company": "Economy Process Solutions Pvt Ltd, Chakan -Oct 2023 – Dec 2023",
        "description":"""Prepared technical and commercial proposals for customized process skids, and developed key engineering deliverables
                         including PFDs, P&IDs, equipment layouts, and GA drawings while supporting 3D modelling activities. Created detailed
                         equipment datasheets and served as the primary interface for customers and internal sales teams. Coordinated fabrication,
                         documentation,and cost tracking during execution. Proficient in AutoCAD, SolidWorks, and Navisworks."""
    },
    {
        "role": "Engineer-Operations",
        "company": "Inox Air Products Pvt Ltd - Dec 2021 – June 2023",
        "description":"""Delivered detailed process engineering for a 200 TPD Air Separation Unit, including PFDs, P&IDs, equipment lists,
                         hydraulic calculations, and mass & energy balances. Supported plant operations, troubleshooting, and prepared control
                         philosophies and process documentation. Participated in L200 ASU commissioning with solo runs on rotary equipment.
                         Used Aspen Plus for simulation and HTRI for thermal design, and collected site data for performance validation and root cause analysis."""
    },
    {
        "role": "Engineer Production",
        "company": "Ellenbarrie Industrial Gases Ltd, Hyderabad - Feb 2021 - Nov 2021",
        "description":"""Optimized a 120 TPD LOX–LIN process plant by reviewing PFDs/P&IDs, performing mass & energy balances, and preparing SOPs,
                         operating manuals, and QA-compliant documentation. Developed datasheets and specifications for major equipment including centrifugal
                         compressors, TSA units, turbines, cryogenic columns, and heat exchangers. Conducted line sizing,hydraulic calculations, and
                         supported interdisciplinary coordination while gaining strong exposure to ASME and API standards for EPC projects."""
    },
    {
        "role": "Jr. Engineer",
        "company": "Inox air products Pvt Ltd, Ville, Raigad - May 2017 - Feb 2021",
        "description":"""Reviewed PFDs, P&IDs, equipment and instrument lists to ensure alignment with design intent and process efficiency.
                         Supported preparation and validation of equipment datasheets and contributed to design reviews for plant upgrades.
                         Worked with design teams and plant leadership to implement process improvements, troubleshoot inefficiencies, and optimize control strategies.
                         Performed natural gas analysis, validated design parameters, and provided real-time input for refining control logic.
                         Participated in commissioning support and internal audits for process documentation and SOP standardization.
                         Gained hands-on exposure to PSA, SMR, cryogenic distillation, and rotary equipment, strengthening understanding of unit operations and design optimization."""
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
