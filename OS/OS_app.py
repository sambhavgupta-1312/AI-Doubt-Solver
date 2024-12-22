import streamlit as st
from final_rag_pipeline import initialize_llm, load_qdrant_retriever, process_query
from sklearn.feature_extraction.text import TfidfVectorizer


def extract_semantic_summary(question):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform([question])
    feature_array = vectorizer.get_feature_names_out()
    return " ".join(feature_array[:5])


def main():
    st.sidebar.title("Chat History")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for i, entry in enumerate(st.session_state.chat_history):
        st.sidebar.write(f"{i + 1}. {entry['title']}")

    st.title("OS Query Assistant")
    st.write("Enter your Operating Systems-related question below, and I will help you!")

    user_query = st.text_input("Your Question:", placeholder="Enter your question here...")

    if st.button("Submit"):
        if not user_query.strip():
            st.warning("Please enter a valid question!")
            return

        qdrant_db_path = "http://localhost:6333"
        collection_name = "1books"
        llm = initialize_llm()
        retriever = load_qdrant_retriever(qdrant_db_path, collection_name)

        if retriever is None:
            st.error("Failed to load Qdrant retriever. Please check your database connection.")
            return

        try:
            answer = process_query(llm, retriever, user_query)

            # Display the answer in the main area
            st.write("### Answer:")
            st.write(answer)

            # Extract semantic summary for chat history
            semantic_title = extract_semantic_summary(user_query)

            # Add to Chat History
            st.session_state.chat_history.append({
                "title": semantic_title,
                "question": user_query,
                "answer": answer
            })

        except Exception as e:
            st.error(f"An error occurred while processing your query: {e}")


if __name__ == "__main__":
    main()
