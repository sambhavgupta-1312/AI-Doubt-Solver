import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Doubt Solver",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for Full Black Background and Sidebar
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #000000;
    }

    /* Sidebar */
    .css-1d391kg, .css-1d391kg:hover {
        background-color: #111111;
        color: #ffffff;
    }
    
    /* Sidebar Titles and Text */
    .css-145kmo2 {
        color: #ffffff;
    }

    /* Main page headers and text */
    .stText, .stTitle, .stMarkdown {
        color: #ECF0F1;
    }

    /* Headers */
    .css-10trblm {
        color: #E74C3C;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background-color: #3498DB;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #1F618D;
        color: white;
    }
    
    /* Return Button */
    .return-btn {
        background-color: #27AE60;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    
    .return-btn:hover {
        background-color: #1E8449;
    }

    /* Divider Line */
    .css-18e3th9 {
        background-color: #333333;
    }
    
    /* Navigation Radio Button */
    .css-1cpxqw2 {
        color: #ffffff;
    }

    .css-1cpxqw2:hover {
        color: #E74C3C;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
selection = st.sidebar.radio("Explore:", [
    "🏠 Home",
    "💻 OS Query Solver",
    "🔄 OS - Similar Questions",
    "📊 DSA Query Solver",
    "🔍 DSA - Similar Questions",
    "📖 General Topic Query"
])

# Main Page Layout
if selection == "🏠 Home":
    st.title("🤖 AI Doubt Solver")
    st.markdown("### Empowering Students with AI-based Problem Solving")
    st.markdown("---")
    
    st.markdown("""
    **Welcome to the AI Doubt Solver Platform!**  
    This app is designed to assist with problem-solving across multiple domains:  
    - **💻 Operating Systems (OS)** – Solve OS-related queries.  
    - **📊 Data Structures and Algorithms (DSA)** – Get solutions to DSA problems.  
    - **🔄 Similar Problem Finder** – Discover related problems to refine your skills.  
    - **📖 General Queries** – Ask general technical questions across topics.  
    
    Built for students, by students.  
    """)

    st.info("**Quick Tip**: Use the sidebar to switch between sections seamlessly.")

elif selection == "💻 OS Query Solver":
    from OS.OS_app import main as os_query_solver
    os_query_solver()
    if st.button("Return to Main Page", key="return_os"):
        st.sidebar.radio("Explore:", ["🏠 Home"])

elif selection == "🔄 OS - Similar Questions":
    from OS.OS_similar_app import main as os_similar_solver
    os_similar_solver()
    if st.button("Return to Main Page", key="return_os_similar"):
        st.sidebar.radio("Explore:", ["🏠 Home"])

elif selection == "📊 DSA Query Solver":
    from dsa.DSA_app import main as dsa_solver
    dsa_solver()
    if st.button("Return to Main Page", key="return_dsa"):
        st.sidebar.radio("Explore:", ["🏠 Home"])

elif selection == "🔍 DSA - Similar Questions":
    from dsa_similarity.ui import main as dsa_similar_solver
    dsa_similar_solver()
    if st.button("Return to Main Page", key="return_dsa_similar"):
        st.sidebar.radio("Explore:", ["🏠 Home"])

elif selection == "📖 General Topic Query":
    from topic.app import main as topic_solver
    topic_solver()
    if st.button("Return to Main Page", key="return_topic"):
        st.sidebar.radio("Explore:", ["🏠 Home"])
