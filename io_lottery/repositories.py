class UserRepository:
    def __init__(self, dao):
        self.dao = dao

    def get_all_users(self):
        return self.dao.get_all_users()

    def get_user_by_id(self, user_id):
        return self.dao.get_user_by_id(user_id)

    def create_user(self, user):
        return self.dao.create_user(user)

    def update_user(self, user_id, user):
        return self.dao.update_user(user_id, user)

    def delete_user(self, user_id):
        return self.dao.delete_user(user_id)


class UserDao:
    def __init__(self, db):
        self.db = db

    def get_all_users(self):
        return self.db.query("SELECT * FROM users")

    def get_user_by_id(self, user_id):
        return self.db.query("SELECT * FROM users WHERE id = ?", user_id)

    def create_user(self, user):
        self.db.execute("INSERT INTO users (name, email) VALUES (?, ?)", user["name"], user["email"])
        return user

    def update_user(self, user_id, user):
        self.db.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", user["name"], user["email"], user_id)
        return user

    def delete_user(self, user_id):
        self.db.execute("DELETE FROM users WHERE id = ?", user_id)
