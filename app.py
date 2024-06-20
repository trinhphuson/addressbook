import end
import json
import sys

print("Welcome to Address Book! (Press h for help)")

while True:
    comm = input('''> ''')
    
    if comm == 'h':
        print('''
h: help
p: print all entries
a: add an entry
e: edit an entry
d: delete a entry
q: quit
''')
        continue
    
    elif comm == 'p':
        end.print_addb()
        continue
    
    elif comm == 'a':
        name = input("Name: ")
        birthday = input("Birthday (Leave blank for none):")
        phone_number = input("Phone number: ")
        email = input("Email (leave blank for none): ")

        """Adds a new record to the JSON file with an auto-incremented ID."""
        try:
            # Read the existing data
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        
        # Determine the new ID
        if data:
            last_id = max(record['id'] for record in data)
            new_id = last_id + 1
        else:
            new_id = 1

        new_record = {
            "id": new_id,
            "name": name,
            "birthday": birthday,
            "phone_number": phone_number, 
            "email": email 
        }

        end.add_addb(new_record)
        continue

    elif comm == 'e':
        id_num = end.get_user_input()
        end.edit_addb(id_num)
        continue
    
    elif comm == 'd':
        record_id_to_delete = end.get_user_input()
        end.del_sec(record_id_to_delete)  
        continue
    
    elif comm == 'q':
        break
    
    else:
        continue

sys.exit()
