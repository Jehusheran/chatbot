import os

def load_lines(file_path):
    lines = {}
    with open(file_path, encoding='utf-8', errors='ignore') as file:
        for line in file:
            parts = line.strip().split(" +++$+++ ")
            if len(parts) >= 5:
                lines[parts[0]] = parts[4]
    print(f"Loaded {len(lines)} lines from {file_path}")
    return lines

def load_conversations(conversations_path, lines):
    conversations = []
    with open(conversations_path, encoding='utf-8', errors='ignore') as file:
        for line in file:
            parts = line.strip().split(" +++$+++ ")
            if len(parts) == 4:
                utterance_ids = eval(parts[3])
                for i in range(len(utterance_ids) - 1):
                    input_line = lines.get(utterance_ids[i], "")
                    response_line = lines.get(utterance_ids[i + 1], "")
                    if input_line and response_line:
                        conversations.append((input_line, response_line))
    print(f"Loaded {len(conversations)} conversations from {conversations_path}")
    return conversations

def save_to_txt(conversations, filename='movie_dialogs.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for input_text, response_text in conversations:
            file.write(f"{input_text}\n{response_text}\n\n")
    print(f"Saved {len(conversations)} conversation pairs to {filename}")

def print_file_content(file_path, num_lines=5):
    print(f"Contents of {file_path}:")
    with open(file_path, encoding='utf-8', errors='ignore') as file:
        for i, line in enumerate(file):
            if i >= num_lines:
                break
            print(line.strip())

if __name__ == "__main__":
    movie_lines = "/Users/wynjehu/Desktop/Zerthwynn/project_root/data/movie_lines.txt"
    movie_conversations = "/Users/wynjehu/Desktop/Zerthwynn/project_root/data/movie_conversations.txt"
    
    # Print the first few lines of each file
    print_file_content(movie_lines)
    print_file_content(movie_conversations)
    
    lines_dict = load_lines(movie_lines)
    convos = load_conversations(movie_conversations, lines_dict)
    save_to_txt(convos)
    print(f"Saved {len(convos)} conversation pairs to movie_dialogs.txt")
