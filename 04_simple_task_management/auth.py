# task_manager/auth.py
import hashlib
from user_repository import UserRepository

class Auth:
    def __init__(self):
        self.repo = UserRepository()

    def hash_password(self, password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        """Registers a new user."""
        if self.repo.get_user(username):
            return False, "Username already exists."
        
        hashed_password = self.hash_password(password)
        self.repo.add_user(username, hashed_password)
        return True, "User registered successfully."

    def login(self, username, password):
        """Logs in an existing user."""
        user = self.repo.get_user(username)
        if user and user['password'] == self.hash_password(password):
            return True, "Login successful."
        return False, "Invalid username or password."
