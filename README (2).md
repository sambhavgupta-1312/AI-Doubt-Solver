
# 🤖 AI Doubt Solver💡

Preparing for interviews can be a daunting task, especially for college students navigating a competitive job market. With diverse topics to cover, ranging from technical subjects to behavioral questions, having a reliable and efficient system
to streamline preparation becomes essential.
To address this challenge, our project is designed as an intelligent interview preparation tool tailored for college students.
The primary objective of this project is to provide instant and accurate answers to questions posed by the user, enhancing their preparation process. Students can either enter specific questions or broader topics, and the system dynamically fetches contextually relevant answers.

By leveraging a Retrieval-Augmented Generation (RAG) pipeline combined with vectorization techniques, the project ensures the answers are not only precise but also contextually aligned with the user's input.
At the heart of the system lies the integration of a well-curated knowledge base, referred to as "the book," which serves as the primary source of information.

This book comprises a comprehensive collection of material covering technical, analytical, and conceptual topics crucial for interviews. Using advanced natural language processing (NLP) techniques, the project efficiently vectorizes the content within the book, enabling quick retrieval and generation of responses tailored to the query or topic entered by the user.

The RAG pipeline enhances this process by merging the capabilities of retrieval systems and generative models. Upon receiving a query, the pipeline identifies the most relevant segments from the book using vector search and subsequently refines the content using generative AI techniques to provide a human-like and refined response. This ensures the user receives high-quality answers without the need to sift through lengthy documents or multiple resources.

Our project is designed to be intuitive and user-friendly, enabling students to focus on learning and building confidence for their interviews. By simplifying the preparation process, this tool empowers users with quick access to curated knowledge, ultimately bridging the gap between theoretical learning and practical application in interviews.
## Demo

https://drive.google.com/file/d/1AA73Irzk73cVHE51zOGQXq1csN9BRcIs/view?usp=sharing


## 💡Features

• Multi-Topic Query Resolution: Handles technical queries across   Operating Systems, DSA, and General Topics, providing tailored answers for each domain.

• Advanced Search with RAG Integration: Combines LLMs with vectorized search to deliver accurate, context-aware answers using Retrieval-Augmented Generation (RAG).

• User-Friendly Interface & Navigation: Features a clean, black-themed UI with easy navigation between modules, all within a single page for a seamless experience.

• History and Session Management: Retains past queries and answers, allowing users to access their query history and maintain context throughout the session.


## 🛠Installation and Usage
1. Setup DOCKER on your local system
```bash
https://www.youtube.com/watch?v=ZyBBv1JmnWQ
```
2. Setup QDRANT on your local system
```bash
https://qdrant.tech/documentation/quickstart/
```
3. Install OLLAMA on your system
```bash
https://ollama.com/download/windows
```
4. Install llama2 model from cmd
```bash
ollama run llama2
```
5. Clone this repository:
```bash
git clone https://github.com/sambhavgupta-1312/AI-Doubt-Solver.git
cd AI-Doubt-Solver
```
6. Install the required packages:
```bash
pip install -r requirements.txt
```
7. Run this cmd on terminal
```bash
python OS\8new_vectorize_book.py
```
8. Setup QDRANT by running this on cmd
```bash
docker run -p 6333:6333 -p 6334:6334 -v %cd%/qdrant_storage:/qdrant/storage:z qdrant/qdrant
```
9. Run this on terminal
```bash
streamlit run main2.py
```
10. Open your browser and navigate to http://localhost:8501.