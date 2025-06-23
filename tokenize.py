import re

def read_toolbox_file(file_path):
    """Reads the content of a Toolbox file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_lc_ps_pairs(text):
    """
    Extracts all \lc and \ps pairs from Toolbox-formatted text.
    Returns a list of (lc, ps) pairs where lc contains exactly one word (no spaces).
    """
    pattern = re.findall(r'\\lc\s+([^\n\\]+)\s+\\ps\s+([^\n\\]+)', text)
    pairs = []
    for lc_entry, ps in pattern:
        lc_entry = lc_entry.strip()
        if ' ' not in lc_entry:  # Only include single-word \lc entries
            pairs.append((lc_entry, ps.strip()))
    return pairs

def max_match(sentence, dictionary):
    """
    Tokenize string using the max-match algorithm.
    """
    if not sentence:
        return []

    max_len = max((len(word) for word in dictionary), default=1)

    for i in range(min(max_len, len(sentence)), 0, -1):
        first_word = sentence[:i]
        if first_word in dictionary:
            return [first_word] + max_match(sentence[i:], dictionary)
            
    return [sentence]

def print_tagged_tokens_grouped(lc_ps_pairs, dictionary, output_file=None):
    """
    Print one \lc entry per line:
    tokens separated by spaces, then one POS tag at line end (tab-separated).
    Also writes to output_file if provided.
    """
    lines = []
    for lc, ps in lc_ps_pairs:
        tokens = max_match(lc, dictionary)
        line = f"{' '.join(tokens)}\t{ps}"
        print(line)
        lines.append(line)
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')

def tokenize_input_line(line, dictionary, pos_dict):
    """
    Tokenize an input line (string) using whitespace split and max-match on each chunk.
    Prints each token with its POS tag (if available).
    """
    chunks = line.strip().split()
    tokens = []
    for chunk in chunks:
        tokens.extend(max_match(chunk, dictionary))
    for token in tokens:
        pos = pos_dict.get(token, 'UNK')
        print(f"{token}\t{pos}")


if __name__ == "__main__":
    # Path to Toolbox file
    toolbox_file_path = "Torwali_DB.txt"

    # Load and process Toolbox file
    toolbox_text = read_toolbox_file(toolbox_file_path)
    lc_ps_pairs = extract_lc_ps_pairs(toolbox_text)

    # Create a lookup dictionary for POS tags
    pos_dict = {lc: ps for lc, ps in lc_ps_pairs}

    # Print and save tokenized entries from Toolbox with POS
    print_tagged_tokens_grouped(lc_ps_pairs, dictionary, output_file="tokenized_output.txt")

    # Interactive input line tokenization with POS print
    print("\nEnter a line to tokenize (or empty line to exit):")
    while True:
        user_input = input("> ").strip()
        if not user_input:
            break
        tokenize_input_line(user_input, dictionary, pos_dict)
