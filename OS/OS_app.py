# import streamlit as st
# from OS.final_rag_pipeline import initialize_llm, load_qdrant_retriever, process_query
# from sklearn.feature_extraction.text import TfidfVectorizer


# def extract_semantic_summary(question):
#     vectorizer = TfidfVectorizer(stop_words='english')
#     X = vectorizer.fit_transform([question])
#     feature_array = vectorizer.get_feature_names_out()
#     return " ".join(feature_array[:5])


# def main():
#     st.sidebar.title("Chat History")
#     if "chat_history" not in st.session_state:
#         st.session_state.chat_history = []

#     for i, entry in enumerate(st.session_state.chat_history):
#         st.sidebar.write(f"{i + 1}. {entry['title']}")

#     st.title("OS Query Assistant")
#     st.write("Enter your Operating Systems-related question below, and I will help you!")

#     user_query = st.text_input("Your Question:", placeholder="Enter your question here...")

#     if st.button("Submit"):
#         if not user_query.strip():
#             st.warning("Please enter a valid question!")
#             return

#         qdrant_db_path = "http://localhost:6333"
#         collection_name = "1books"
#         llm = initialize_llm()
#         retriever = load_qdrant_retriever(qdrant_db_path, collection_name)

#         if retriever is None:
#             st.error("Failed to load Qdrant retriever. Please check your database connection.")
#             return

#         try:
#             answer = process_query(llm, retriever, user_query)

#             # Display the answer in the main area
#             st.write("### Answer:")
#             st.write(answer)

#             # Extract semantic summary for chat history
#             semantic_title = extract_semantic_summary(user_query)

#             # Add to Chat History
#             st.session_state.chat_history.append({
#                 "title": semantic_title,
#                 "question": user_query,
#                 "answer": answer
#             })

#         except Exception as e:
#             st.error(f"An error occurred while processing your query: {e}")


# if __name__ == "__main__":
#     main()

import streamlit as st
from OS.final_rag_pipeline import initialize_llm, load_qdrant_retriever, process_query
from sklearn.feature_extraction.text import TfidfVectorizer

# Apply Custom CSS for Dark Theme with Red Label
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
    
    /* Sidebar Text */
    .css-145kmo2 {
        color: #ffffff;
    }
    
    /* Main Page Title */
    .stText, .stTitle, .stMarkdown {
        color: #ECF0F1;
    }
    
    /* Input Box */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #000000;
        border: 1px solid #3498DB;
        border-radius: 8px;
    }
    
    /* Placeholder Text */
    input::placeholder {
        color: #808080;
        font-style: italic;
    }
    
    /* Warning and Error Messages */
    .stAlert {
        background-color: #333333;
        color: #E74C3C;
        border-radius: 5px;
    }
    
    /* Submit Button */
    div.stButton > button:first-child {
        background-color: #3498DB;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #1F618D;
        color: white;
    }
    
    /* Answer Box */
    .stMarkdown h3 {
        color: #27AE60;
    }
    </style>
    """, unsafe_allow_html=True)

def extract_semantic_summary(question):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([question])
    feature_array = vectorizer.get_feature_names_out()
    return " ".join(feature_array[:5])

def main():
    # Sidebar for Chat History
    st.sidebar.title("🗂️ Chat History")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for i, entry in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"{i + 1}. {entry['title']}")

    # Main Title and Description
    st.markdown(
    '<h1 style="color: #E74C3C;">💻 OS Query Assistant</h1>',
    unsafe_allow_html=True
    )
    st.markdown("### Solve your Operating System Queries in Seconds")

    # User Input
    # st.markdown('<label for="Your Question:" class="custom-label">Your Question:</label>', unsafe_allow_html=True)
    st.markdown('Your Question:')
    user_query = st.text_input(
        "this is hidden label",  # Keep label empty as it's now customized
        placeholder="Enter your OS-related question here...",
        label_visibility='hidden'
    )

    # Submit Button
    if st.button("Submit"):
        if not user_query.strip():
            st.warning("⚠️ Please enter a valid question!")
            return

        qdrant_db_path = "http://localhost:6333"
        collection_name = "1books"
        llm = initialize_llm()
        retriever = load_qdrant_retriever(qdrant_db_path, collection_name)

        if retriever is None:
            st.error("❌ Failed to load Qdrant retriever. Please check your database connection.")
            return

        try:
            answer = process_query(llm, retriever, user_query)

            # Display Answer
            st.markdown("### ✅ Answer:")
            st.write(answer)

            # Extract Semantic Summary for History
            semantic_title = extract_semantic_summary(user_query)

            # Add to Chat History
            st.session_state.chat_history.append({
                "title": semantic_title,
                "question": user_query,
                "answer": answer
            })

        except Exception as e:
            st.error(f"❌ An error occurred while processing your query: {e}")

