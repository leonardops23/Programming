from database import connect


class UserRepository:
    def add_user(self, username, password):
        cnn = connect()
        c = cnn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                  (username, password))
        cnn.commit()
        cnn.close()

    
    def get_user(self, username):
        cnn = connect()
        c = cnn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        c.close()

        if user:
            return {f"username: {user[1]} password: {user[2]}"}
        else:
            return None
