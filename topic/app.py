import streamlit as st
from functionality import fetch_topic_resource

st.title('General topic Helper')

topic = st.text_input("Enter any general topic or any query")
    
if topic:
    st.write("Searching for resources on this topic...")
    topic_link = fetch_topic_resource(topic)
    st.write("Here is a resource link to get started:")
    if "http" in topic_link:
        st.markdown(f"### [Click here to explore the resource]({topic_link})", unsafe_allow_html=True)
    else:
        st.write(topic_link)