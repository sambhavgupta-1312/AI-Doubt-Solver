import pandas as pd

book_index = pd.read_csv('OS/index_data.csv')

def retrieve_book_pages(umbrella_topic, book_index):
    # Remove the parentheses from the search string and use more flexible matching
    search_term = umbrella_topic.replace('(', '').replace(')', '')
    relevant_entries = book_index[book_index['Topic'].str.contains(search_term, case=False, na=False)]

    # Check if any entries were found
    if len(relevant_entries) == 0:
        return "Not enough data found under this topic."
    
    # Get the pages
    pages = []
    for _, row in relevant_entries.iterrows():
        page_range = list(range(int(row['PageStart']), int(row['PageEnd']) + 2))
        pages.extend(page_range)
        if len(pages) >= 4:
            break
    
    return pages[:4] if pages else "Not enough data found under this topic."

umbrella_topic_info = "Linkers and Loaders"
pages = retrieve_book_pages(umbrella_topic_info, book_index)
print("Pages Retrieved:", pages)
