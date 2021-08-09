Contribute
==========

Fork this repo, then clone your fork.
-------------------------------------

```
git clone git@github.com:<yourusername>/StreamBerry.git
```

Create a virtual environment
----------------------------

Create a virtual environments inside the project's folder. This makes it easier for VSCode to detect and use it.

```
cd StreamBerry
python3 -m venv venv
```

Activate the virtual environment and install the dependencies. The following assumes you are using bash.

```
. venv/bin/activate
python3 -m pip install -r requirements.txt
```

Run VSCode
----------

Deactivate the virtual environment, then run `vscode` from the project's folder :

```
deactivate
code .
```

`vscode` should find the virtual env automatically, and you should have no linting error.

Final checks
------------

To make sure everything is properly installed and configured, open a terminal inside `vscode` (`Terminal` > `New terminal`). You should see the virtual environment being automatically activated.

Then type `pylint src` to check that the linter works properly. 

