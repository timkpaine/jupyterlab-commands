# jupyterlab commands

Arbitrary python commands for notebooks in JupyterLab

[![Build Status](https://github.com/timkpaine/jupyterlab-commands/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/timkpaine/jupyterlab-commands/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/timkpaine/jupyterlab-commands/branch/main/graph/badge.svg)](https://codecov.io/gh/timkpaine/jupyterlab-commands)
[![License](https://img.shields.io/github/license/timkpaine/jupyterlab-commands)](https://github.com/timkpaine/jupyterlab-commands)
[![PyPI](https://img.shields.io/pypi/v/jupyterlab-commands.svg)](https://pypi.python.org/pypi/jupyterlab-commands)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/timkpaine/jupyterlab-commands/main?urlpath=lab)

## About

This extension adds arbitrary Python commands to JupyterLab's command palette.
Commands can run outside notebooks and consoles, making them useful for tasks
such as:

- running predefined `nbconvert` functions without adding code to a notebook
- interacting with version control without recording that interaction in a
  notebook

## Installation

```bash
pip install jupyterlab-commands
```

## Configuration

Install the server extension and add commands to `jupyter_lab_config.py`:

```python
def convert(request, *args, **kwargs):
    import json
    import os
    import subprocess

    import tornado

    data = json.loads(tornado.escape.json_decode(request.body))
    path = os.path.join(os.getcwd(), data["path"])
    subprocess.run(["jupyter", "nbconvert", path, "--to", "html"], check=True)
    return {"body": "ok"}


c.JupyterLabCommands.commands = {"convert": convert}
```

Commands appear in the command palette:

![Command palette](https://raw.githubusercontent.com/timkpaine/jupyterlab-commands/main/docs/2.png)

Command output appears in the terminal:

![Terminal output](https://raw.githubusercontent.com/timkpaine/jupyterlab-commands/main/docs/3.png)

## Related projects

[jupyterlab-nbconvert-nocode](https://github.com/timkpaine/jupyterlab-nbconvert-nocode)
provides notebook conversion with code cells removed.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
