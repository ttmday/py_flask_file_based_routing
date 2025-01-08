# py_flask_file_based_routing

REGISTER BLUEPRINTS BY FILEROUTING LIKE FRAMEWORKS NEXTJS OR REMIX OR ASTRO

```python

from flask import Flask

from lib.blueprints import register_blueprints


def create_app():
    app = Flask(__name__)

    register_blueprints(app, blueprints_glob="src/modules/**/__init__.py")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

```
