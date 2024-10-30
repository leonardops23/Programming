from run import create_app
from config import a

from flask import Flask

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

