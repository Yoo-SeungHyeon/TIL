import csv, json

class User:
    def __init__(self):
        self.user_data = []
    
    def add_user(self, user_id, name, email):
        self.user_data.append({"user_id": user_id,
                                "name": name,
                                "email": email})
    
    def get_users(self):
        for data in self.user_data:
            print(f'User(id={data["user_id"]}, name={data["name"]}, email={data["email"]})')

    def save_to_csv(self):
        field_name = ['user_id', 'name', 'email']
        with open('user_data.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=field_name)
            writer.writeheader()
            writer.writerows(self.user_data)

    def load_to_csv(self):
        with open('user_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            self.user_data = list(reader)

    def save_to_json(self):
        with open('user_data.json', 'w') as f:
            json.dump(self.user_data, f )

    def load_to_json(self):
        with open('user_data.json', 'r') as f:
            self.user_data = list(json.load(f))


if __name__ == "__main__":
    users = User()
    users.add_user('1', 'Alice', 'alice@example.com')
    users.add_user('2', 'Bob', 'bob@example.com')
    # users.get_users()

    users.save_to_csv()
    users.load_to_csv()
    users.get_users()

    users.save_to_json()
    users.load_to_json()
    users.get_users()