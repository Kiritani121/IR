# Define a dictionary of documents
docs = {
    1: 'the quick brown fox',
    2: 'jumps over the lazy dog',
    3: 'this is a sample document',
    4: 'just another day',
    5: 'at the office'
}

# Take input query from the user
query = input('Enter query: ')

# Split the query into individual words
query_words = query.split()

# Initialize a list to hold the matching document IDs
matching_docs = []

# Loop through each document in the dictionary
for doc_id, doc_text in docs.items():
    # Initialize a variable to hold the bitwise operations
    result = 0
    
    # Loop through each word in the query
    for word in query_words:
        # Check if the word is present in the document
        if word in doc_text:
            # Perform bitwise OR operation on the matching words
            result = result | 1
        
    # Check if all query words match the document
    if result == 1:
        # Append the document ID to the matching_docs list
        matching_docs.append(doc_id)

# Print the matching document IDs
print('Matching documents:', matching_docs)