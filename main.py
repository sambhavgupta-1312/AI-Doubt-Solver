import streamlit as st
import os

st.set_page_config(
    page_title="AI Doubt Solver",
    page_icon="🤖",
    layout="centered"
)

# st.markdown(
#     """
#     <style>
#     /* Set background color for the main app */
#     .main {
#         background-color: #0E1117;
#         color: white;
#     }

#     /* Set background color for the sidebar */
#     [data-testid="stSidebar"] {
#         background-color: #262730;
#     }

#     /* Customize other elements as needed */
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


st.title("🤖 AI Doubt Solver")
st.subheader("Your own all-purpose doubt solution stop.")

st.markdown("###")  # Add a line break

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("OS Query Solver"):
        os.system("streamlit run OS/OS_app.py")  # Call OS Query Solver app
    
    if st.button("OS - Find Similar Questions to Your solved Problem"):
        os.system("streamlit run OS/OS_similar_app.py")  # Call OS Similar Questions app
    
    if st.button("DSA Query Solver"):
        os.system("streamlit run dsa/DSA_app.py")  # Call DSA Query Solver app
    
    if st.button("DSA - Find Similar Questions to Your solved Problem"):
        os.system("streamlit run dsa_similarity/ui.py")  # Call DSA Similar Questions app
    
    if st.button("General Topic Query"):
        os.system("streamlit run topic/app.py")  # Call General Topic Query app

# Footer with credits
st.markdown("---")  # Horizontal line
st.markdown(
    """
    **Built by:**  
    Sambhav Gupta - 22103181  
    Rahul Singh - 22103152  
    Shivesh Dixit - 22103159
    """,
    unsafe_allow_html=True,
)
