import time
import timeit

# Function to read documents from a file
def read_documents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

# Map function: Tokenizes and maps each word to a count of 1
def map_function(document):
    tokens = document.strip().split()
    return [(token.lower(), 1) for token in tokens]  # Convert tokens to lowercase to ensure uniqueness

# Reduce function: Aggregates count for each word
def reduce_function(items):
    word, counts = items[0], items[1]
    return (word, sum(counts))

# Perform basic statistical analysis on the word counts
def analyze_data(reduced_results):
    # Convert map object to list for multiple iterations
    word_counts = list(reduced_results)

    # Find most and least common words
    most_common = max(word_counts, key=lambda x: x[1])
    least_common = min(word_counts, key=lambda x: x[1])

    # Calculate average word frequency
    average_count = sum(count for _, count in word_counts) / len(word_counts)

    print(f"Most common word: {most_common}")
    print(f"Least common word: {least_common}")
    print(f"Average word frequency: {average_count:.2f}")

    return word_counts

# Main function to run the MapReduce job and additional analysis
def main(file_path = 'text_10k.txt'):
    documents = read_documents(file_path)

    # Map phase
    mapped_results = []
    for document in documents:
        mapped_results.extend(map_function(document))

    # Organize mapped results by key to prepare for reduce phase
    intermediate = {}
    for key, value in mapped_results:
        if key not in intermediate:
            intermediate[key] = []
        intermediate[key].append(value)

    # Reduce phase
    reduced_results = map(reduce_function, intermediate.items())

    # Perform data analysis and aggregation on the reduced results
    word_counts = analyze_data(reduced_results)


if __name__ == "__main__":
    # Time each file and round the value to 2 decimal places
    print("--------------------------------------------------")
    print(f"Runtime: {round(timeit.timeit(main, number=1), 2)} seconds")
    print("--------------------------------------------------")
    start_time = time.time()
    main('text_30k.txt')
    print(f"Runtime: {round(time.time() - start_time, 2)} seconds")
    print("--------------------------------------------------")
    start_time = time.time()
    main('text_100k.txt')
    print(f"Runtime: {round(time.time() - start_time, 2)} seconds")
    print("--------------------------------------------------")
