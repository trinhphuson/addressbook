import json

def print_addb():
    file_path = 'data.json'
    # Open the JSON file and read it
    with open(file_path, 'r') as file:
        # Load the JSON data
        data = json.load(file)
        
        # Check for data
        if not data:
            print("No data yet!")
        else:
            # Loop through each record in the JSON data
            for record in data:
                # Extract the required fields
                id_number = record.get('id')
                name = record.get('name')
                birthday = record.get('birthday')
                phone_number = record.get('phone_number')
                email = record.get('email')
                                                                     
                # Print the extracted information
                print(f"ID: {id_number}")
                print(f"Name: {name}")
                print(f"Birthday: {birthday}")
                print(f"Phone Number: {phone_number}")
                print(f"Email: {email}")
                print("\n")  # Add a newline for readability

def add_addb(new_record):
    file_path = 'data.json'
    """Adds a new record to the JSON file"""
    try:
        # Read the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Append the new record to the data
    data.append(new_record)

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Added successfully")


def edit_addb(record_id):
    file_path = 'data.json'
    """Edits a record in the JSON file by its ID."""
    try:
        # Read the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The JSON file does not exist.")
        return

    # Find the record by ID and update it
    for record in data:
        if record['id'] == record_id:
            print(f"Editing with ID {record_id}:")
            new_name = input(f"New name (current: {record['name']}): ")
            new_birthday = input(f"New birthday (current: {record['birthday']}): ")
            new_phone_number = input(f"New phone number (current: {record['phone_number']}): ")
            new_email = input(f"New email (current: {record['email']}): ")

            if new_name:
                record['name'] = new_name
            if new_birthday:
                record['birthday'] = new_birthday
            if new_phone_number:
                record['phone_number'] = new_phone_number
            if new_email:
                record['email'] = new_email
            break
    else:
        print(f"Not found.")
        return

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Record with ID {record_id} edited successfully.") 

def del_sec(record_id):
    file_path = "data.json"
    """Deletes a record from the JSON file by its ID."""
    try:
        # Read the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The JSON file does not exist.")
        return

    # Find the record by ID and remove it
    data = [record for record in data if record['id'] != record_id]

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Record with ID {record_id} deleted successfully.")


def get_user_input():
    """Gets and validates user input for record ID."""
    while True:
        try:
            user_input = input("Enter the ID of the record to delete: ")
            record_id = int(user_input)
            return record_id
        except ValueError:
            print("Invalid input. Please enter a valid number.")
