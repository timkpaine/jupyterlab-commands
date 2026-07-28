from .extension import load_jupyter_server_extension

__version__ = "0.4.0"


def _jupyter_server_extension_paths():
    return [{"module": "jupyterlab_commands"}]


def _jupyter_server_extension_points():
    return [{"module": "jupyterlab_commands"}]


def _load_jupyter_server_extension(nb_server_app, nb6_entrypoint=False):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    load_jupyter_server_extension(nb_server_app)


def _jupyter_nbextension_paths():
    return [
        {
            "section": "tree",
            "src": "nbextension/static",
            "dest": "jupyterlab_commands",
            "require": "jupyterlab_commands/notebook",
        }
    ]
