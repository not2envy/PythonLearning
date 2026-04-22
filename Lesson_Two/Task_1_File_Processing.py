from Fees import apply_fee #applys the fee to the amount

def safe_process(file_path):
    results = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    numbers = int(line.strip())
                    filtered_number = [numbers]  if numbers > 10 else []
                    results.append(filtered_number)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return apply_fee(results)

