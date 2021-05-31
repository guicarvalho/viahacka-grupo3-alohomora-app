import os

from app import create_app

port = int(os.getenv("PORT", 8000))
env = os.getenv("ENVIRONMENT", "dev")

if __name__ == "__main__":
    app = create_app(environment=env)
    app.run(host="0.0.0.0", port=port, debug=False if env != "dev" else True)
