from Fees import apply_fee #applys the fee to the amount

def safe_process(file_path, threshold):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    numbers = int(line.strip())
                    if numbers > threshold: #only process numbers above the threshold "Filtering"
                        results.append(numbers * 1.2) #apply fee to the number
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return results

print(safe_process("D:\\Documents\\Development\\PythonLearning\\Lesson_Two\\File_Issues.txt", 10))