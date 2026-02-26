#Portfolio Website using stremlit

import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Mayur's Portfolio", layout="wide")

st.subheader("Hi, I am ")
st.title("Mayur Panchal")
#sidebar for skills, projects, achievements, contact

with st.sidebar:
    selected = option_menu(
        menu_title="Mayur'sPortfolio",
        options=["About Me", "Skills", "Projects","Achievements", "Contact"],
        icons=["person", "tools", "folder", "award", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

st.write("Selected:", selected)
st.sidebar.markdown("---")

#about me section
st.markdown("---")
def about():
    st.subheader("Data scientist")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("profile.jpg", use_container_width=True)

    with col2:
        st.write("I am a data scientist with a passion for machine learning and data analysis. I have experience in building predictive models, data preprocessing, and visualization.""I am always eager to learn new techniques and apply them to solve real-world problems.")
        st.write("I have a strong background in Python, SQL, and various machine learning libraries. I enjoy working on projects that involve data-driven decision making and insights generation.") 
        st.write("Completed IBM Generative AI Internship where I built a Code Snippet Generator using Gemini API.")

        st.write("📧 Email: mayurpanchal2715@gmail.com")
        st.write("📱 Phone: +91 9313635057")
        st.write("🔗 LinkedIn: https://linkedin.com/in/mayur-panchal-9204a6313")
        st.write("💻 GitHub: https://github.com/codehub2715")

    st.divider()

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects Built", "6+")
    col2.metric("Certifications", "3")
    col3.metric("Internships", "1")

    st.divider()

    with open("resume.pdf", "rb") as file:
        st.download_button(label="📄 Download Resume",data=file,file_name="resume.pdf",mime="application/pdf")
 
#skills section
def skills():
    st.header("🛠 Skills")

    skills_data = [
        ("python.png", "Python", 90),
        ("streamlit.jpg", "Streamlit", 85),
        ("ml.png", "Machine Learning", 88),
        ("dl.png", "Data Analysis", 82),
        ("dv.png", "Data Visualization", 80),
        ("sql.png", "SQL", 75)
    ]

    col1, col2 = st.columns(2)

    for i, (img, skill, percent) in enumerate(skills_data):
        column = col1 if i % 2 == 0 else col2

        with column:
            sub_col1, sub_col2 = st.columns([1, 3])

            with sub_col1:
                st.image(img, width=60)

            with sub_col2:
                st.subheader(f"{skill} ")
                st.progress(percent)
                st.write(f"{percent}%")

            st.divider()


#projects section
def projects():
    st.header("🚀 Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.image("inventory.jpeg", width=300)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📦 Inventory Management System")
        st.write("Stock tracking system built using Streamlit & SQLite. A business-oriented application that helps small stores manage stock, monitor inventory levels, and track product movement.")
        st.link_button("View Project", "https://inventorymanage1.streamlit.app")
        st.markdown("---")

    with col2:
        st.image("expense.jpeg", width=250)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("💰 Personal Expense Tracker")
        st.write("Interactive dashboard using Streamlit & Plotly.A web-based dashboard built using Streamlit that allows users to upload their expense data and visualize their spending patterns.")
        st.link_button("View Project", "https://code-snippet-1-ewvd.onrender.com")
        st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.image("snippet.jpeg", width=350)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🤖 Code Snippet Generator")
        st.write("Generative AI project using Gemini 1.5 Flash API.AI-powered code generation tool built using Gemini 1.5 Flash API that generates optimized, structured, and ready-to-use code snippets across multiple programming languages.")
        st.link_button("View Project", "https://personal-expense-1.streamlit.app")
        
    with col4:
        st.image("lifestyle.jpeg", width=300)
        st.subheader("📊 Lifestyle Prediction App")
        st.write("Predicts daily energy levels based on lifestyle factors using a Random Forest model and User will enter daily habit details (sleep, steps, workout, junk food, screen time, stress level).The model will predict an energy score for the day (0–100).")
        st.link_button("View Project", "https://lifestyle-prediction-fx6f9hgs2ccsergfxvlh5y.streamlit.app")
        
def achievements():
    st.header("🏆 Achievements & Certifications")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("IBM Generative AI Internship")
        st.link_button(
            "View Certificate",
            "https://ibmcep.cognitiveclass.ai/certificates/d32b176b-1189-43c5-89f8-97cbe12abb62"
        )

    with col2:
        st.info("Deloitte Data Analytics Job Simulation")
        st.link_button(
            "View Certificate",
            "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_3AkFBsEc7n6dsLpit_1747040949837_completion_certificate.pdf"
        )

    with col3:
        st.info("Tata GenAI Data Analytics Simulation")
        st.link_button(
            "View Certificate",
            "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/gMTdCXwDdLYoXZ3wG_ifobHAoMjQs9s6bKS_3AkFBsEc7n6dsLpit_1749798116696_completion_certificate.pdf"
        )


def contact():
    st.header("📬 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if not name or not email or not message:
            st.warning("⚠️ Please fill all fields")
        else:
            st.success("✅ Message sent successfully!")
            st.info("Thanks for reaching out! I will get back to you soon.")

    if st.button("Contact Details"):
        st.write("Name: Mayur Panchal")
        st.write("Email: mayurpanchal2715@gmail.com")
        st.write("Phone: +91 9313635057")
    

if selected == "About Me":
    about()
elif selected == "Skills":
    skills()
elif selected == "Projects":
    projects()
elif selected == "Achievements":
    achievements()
elif selected == "Contact":
    contact()