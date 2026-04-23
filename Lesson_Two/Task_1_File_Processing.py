from Fees import apply_fee #applys the fee to the amount

def safe_process(file_path, threshold):
    results = []
    skipped = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    numbers = int(line.strip())
                    if numbers > threshold: #only process numbers above the threshold "Filtering"
                        results.append(numbers * 1.2) #apply fee to the number
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    skipped += 1
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return results, skipped

print(safe_process("D:\\Documents\\Development\\PythonLearning\\Lesson_Two\\File_Issues.txt", 30))