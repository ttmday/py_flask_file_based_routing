import glob
import importlib
import importlib.util

from flask import Blueprint
from typing import Protocol, Any


class Application(Protocol):
    def register_blueprint(self, blueprint: Blueprint, **options: Any) -> None:
        pass


def register_blueprints(
    app: Application, blueprints_glob="src/app/modules/**/__init__.py"
):
    """REGISTER BLUEPRINTS BY FILEROUTING LIKE FRAMEWORKS NEXTJS OR REMIX OR ASTRO

    :param blueprints_glob: location pattern of blueprints

    """

    # Find all blueprint file with pattern in glob function
    blueprints_dir_list = glob.glob(blueprints_glob)

    for bpf in blueprints_dir_list:
        module_name = bpf.split("src")[1][1:].replace("/", ".").replace(".py", "")

        spec = importlib.util.find_spec(module_name)
        if spec is None:
            continue

        module = importlib.util.module_from_spec(spec)

        if spec.loader is None:
            continue

        # If module finded and spec is not None, execute module to register blueprint
        spec.loader.exec_module(module=module)
        # Verify is module contains bp instance
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)
