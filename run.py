# run.py

from api import create_app

# create api
app = create_app()

if __name__ == '__main__':
    app.run()