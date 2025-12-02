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
        "company": "ENPRO Industries Pvt. Ltd., Pune (2nd Jan 2024 – Present)",
        "description": """
        • Prepared core engineering deliverables including PFDs, P&IDs, mass & energy balances, equipment datasheets, instrument datasheets, and utility consumption summaries.
        \n• Leading process engineering for Green Hydrogen, Pyrolysis, Gasification, and Electrochemical Hydrogen Compression projects.
        \n• Executed FEED & Detailed Design for complete Balance of Plant (BoP) packages.
        \n• Designed and rated shell & tube heat exchangers; performed technical vendor reviews.
        \n• Supported proposal engineering and contributed to technical bids and design philosophies.
        \n• Hands-on experience with AutoCAD, Inventor, SolidWorks, and Navisworks.
        \n• Served as primary technical contact for international clients.
        \n• Ensured QA/QC compliance and contributed to process document standardization.
        """
    },
    {
        "role": "Proposal & Project Engineer",
        "company": "Economy Process Solutions Pvt Ltd, Chakan (Oct 2023 – Dec 2023)",
        "description": """
        \n• Prepared technical and commercial proposals for process equipment skids.
        \n• Developed PFDs, P&IDs, equipment layouts, GA drawings, and supported 3D modeling.
        \n• Created equipment datasheets for pumps, heat exchangers, valves, motors, and instruments.
        \n• Single-point contact for customers and internal sales teams.
        \n• Coordinated fabrication, document control, and cost tracking.
        \n• Tools used: AutoCAD, SolidWorks, Navisworks.
        """
    },
    {
        "role": "Engineer - Operations",
        "company": "Inox Air Products Pvt Ltd (Dec 2021 – June 2023)",
        "description": """
        • 200 TPD ASU Project involvement.
        \n• Conducted line sizing and pump hydraulic calculations.
        \n• Worked as operations support and led plant troubleshooting.
        \n• Prepared control philosophies, process descriptions, and utility balance documents.
        \n• Participated in L200 ASU plant commissioning.
        \n• Utilized Aspen Plus for simulation and HTRI for thermal design.
        \n• Collected site performance data and performed RCA for deviations.
        """
    },
    {
        "role": "Engineer - Production",
        "company": "Ellenbarrie Industrial Gases Ltd, Hyderabad (Feb 2021 – Nov 2021)",
        "description": """
        • Optimized LOX-LIN process plant (120 TPD).
        \n• Developed SOPs, operating manuals, and QA documentation.
        \n• Reviewed PFDs, P&IDs, and conducted mass & energy balance calculations.
        \n• Created datasheets for compressors, TSA units, turbines, columns, and heat exchangers.
        \n• Performed line sizing and supported multidisciplinary coordination.
        \n• Gained exposure to ASME, API standards and EPC project workflows.
        """
    },
    {
        "role": "Jr. Engineer",
        "company": "Inox Air Products Pvt Ltd, Raigad (May 2017 – Feb 2021)",
        "description": """
        • Reviewed PFDs, P&IDs, equipment lists, and instrument lists.
        \n• Prepared equipment datasheets and participated in design reviews.
        \n• Implemented process improvements and troubleshooting.
        \n• Conducted natural gas analysis and validated design parameters.
        \n• Supported commissioning and internal audits for documentation.
        \n• Gained exposure to PSA, SMR, cryogenic distillation, and rotary equipment.
        """
    }
]

EDUCATION = [
      {"info": "• B.E. in Chemical Engineering from PVPIT, Sangli (Shivaji University Kolhapur 2012-216) with aggregate 66.81%"}   
    ]

CERTIFICATION = [
      {"info": "• Process Design Engineering from SB Technologies, Mumbai an ISO  9001:2015 Certified training center "}   
    ]

ACADEMIC_PROJECTS_AND_SEMINARS = [
      {"Title": "• Design of Agitation vessel"}
    ]

PERSONAL_ATTRIBUTES_and_SKILLS = [
    {
        "info1": "•  Co-operative nature & like to work with team.",
        "info2": "•  Positive attitude.",
        "info3": "•  Ready to learn new ideas and technical knowledge.",
        "info4": "•  Quick learner, versatile and ability to manage several assignments simultaneously."
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
#EDUCATION
st.header("EDUCATION")
for e in EDUCATION:
      st.write(e["info"])

#CERTIFICATION
st.header("CERTIFICATION")
for c in CERTIFICATION:
      st.write(c["info"])

#ACADEMIC_PROJECTS_AND_SEMINARS
st.header("ACADEMIC_PROJECTS_AND_SEMINARS")
for a in ACADEMIC_PROJECTS_AND_SEMINARS:
      st.write(a["Title"])


#PERSONAL_ATTRIBUTES_and_SKILLS
st.header("PERSONAL_ATTRIBUTES_&_SKILLS")
for p in PERSONAL_ATTRIBUTES_and_SKILLS:
      st.write(p["info1"])
      st.write(p["info2"])
      st.write(p["info3"])
      st.write(p["info4"])

      
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
