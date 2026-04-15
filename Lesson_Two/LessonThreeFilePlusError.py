def safe_process(file_path):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    results.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    
    return results