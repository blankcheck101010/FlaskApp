# flaskblog is the directory of the package we just created.
# and the __init__.py must have the variable app, which it does.
from flaskblog import app

# naming this run.py since that is it's main job.
if __name__ == '__main__':
    app.run(debug=True)
