import csv
import random
import string

# Function to generate random strings for SQL injection payloads
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate SQL injection payloads
def generate_sql_payloads(num_payloads):
    payloads = []
    for _ in range(num_payloads):
        # Generate random SQL injection payloads
        payload = f"' OR {generate_random_string(5)}='"
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
    num_payloads = 100  # Change this to the desired number of payloads
    payloads = generate_sql_payloads(num_payloads)
    csv_filename = 'sql_injection_payloads.csv'
    save_payloads_to_csv(payloads, csv_filename)
    print(f'{num_payloads} SQL injection payloads saved to {csv_filename}')

if __name__ == '__main__':
    main()
