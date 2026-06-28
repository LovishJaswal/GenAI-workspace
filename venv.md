# Virtual Environment

---

# What is a Virtual Environment?

A **Virtual Environment (venv)** is an isolated Python environment created for a specific project.

Each virtual environment has its own:

- Python interpreter
- Installed packages
- Dependencies
- Package versions

This prevents conflicts between different Python projects.

---

# Why Use a Virtual Environment?

Without a virtual environment, every package is installed globally.

Example:

- Project A requires `numpy==1.24`
- Project B requires `numpy==2.0`

Installing one version globally may break the other project.

A virtual environment solves this by keeping dependencies isolated.

---

# Advantages

- Isolates project dependencies.
- Prevents package version conflicts.
- Keeps the global Python installation clean.
- Makes projects reproducible.
- Easier collaboration with other developers.

---

# Project Structure

Example:

```text
My_Project/
│
├── .venv/
├── main.py
├── requirements.txt
└── README.md
```

The `.venv` folder contains all packages and configuration for that project.

---

# Creating a Virtual Environment

Using Python's built-in `venv` module:

```bash
python -m venv .venv
```

or

```bash
python3 -m venv .venv
```

This creates a hidden folder named `.venv`.

---

# Activating the Virtual Environment

## Windows (Command Prompt)

```bash
.venv\Scripts\activate
```

## Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

## Linux / macOS

```bash
source .venv/bin/activate
```

After activation, your terminal prompt usually changes to:

```text
(.venv) C:\Projects\My_Project>
```

This indicates that the virtual environment is active.

---

# Checking the Active Python Interpreter

Check the Python version:

```bash
python --version
```

On Windows:

```bash
where python
```

On Linux/macOS:

```bash
which python
```

These commands help verify that Python is running from the virtual environment.

---

# Installing Packages

Install a package using `pip`:

```bash
pip install requests
```

Example:

```bash
pip install numpy pandas matplotlib
```

Packages are installed **only** inside the active virtual environment.

---

# Viewing Installed Packages

List all installed packages:

```bash
pip list
```

or

```bash
pip freeze
```

`pip freeze` displays package versions, making it useful for creating dependency files.

---

# Upgrading Packages

Upgrade an installed package:

```bash
pip install --upgrade requests
```

---

# Uninstalling Packages

Remove an installed package:

```bash
pip uninstall requests
```
# Exporting Dependencies

Create a `requirements.txt` file containing all installed packages and their versions.

```bash
pip freeze > requirements.txt
```

Example:

```text
numpy==2.3.0
pandas==2.2.3
requests==2.32.4
```

This file allows other developers (or your future self) to install the exact same dependencies.

---

# Installing from `requirements.txt`

Install all dependencies listed in the file:

```bash
pip install -r requirements.txt
```

This is commonly done after cloning a project from GitHub.

---

# Deactivating the Virtual Environment

To exit the current virtual environment:

```bash
deactivate
```

Your terminal will return to the global Python environment.

---

# Deleting a Virtual Environment

A virtual environment is simply a folder.

To delete it, remove the `.venv` directory.

It can always be recreated using:

```bash
python -m venv .venv
```

---

# Using `uv`

`uv` is a modern Python package and environment manager.

Compared to `pip`, it is significantly faster and simplifies dependency management.

---

## Initialize a Project

```bash
uv init
```

Creates a new Python project with the necessary configuration files.

---

## Create a Virtual Environment

```bash
uv venv
```

Creates a virtual environment for the current project.

---

## Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Add Packages

Install a package:

```bash
uv add requests
```

Example:

```bash
uv add numpy pandas matplotlib
```

Unlike `pip`, `uv` automatically updates the project's dependency configuration.

---

## Synchronize Dependencies

```bash
uv sync
```

Installs all dependencies defined for the project.

Useful after cloning a repository.

---

## Remove a Package

```bash
uv remove requests
```

---

## Run a Python Program

```bash
uv run main.py
```

This ensures the program runs inside the project's virtual environment.

---

# `pip` vs `uv`

| Feature | `pip` | `uv` |
|----------|-------|------|
| Package Installation | ✅ | ✅ |
| Virtual Environment | Uses `venv` | Built-in |
| Speed | Moderate | Very Fast |
| Dependency Management | `requirements.txt` | Automatic |
| Modern Workflow | Limited | Excellent |

---

# Best Practices

- Create one virtual environment per project.
- Never install project dependencies globally.
- Activate the virtual environment before writing or running code.
- Add `.venv/` to `.gitignore`.
- Never push the `.venv` folder to GitHub.
- Share `requirements.txt` (or the project's dependency file) instead of the virtual environment.
- Recreate the virtual environment whenever needed instead of backing it up.

---

# Common Commands

| Task | Command |
|------|---------|
| Create Virtual Environment | `python -m venv .venv` |
| Activate (Windows) | `.venv\Scripts\activate` |
| Activate (Linux/macOS) | `source .venv/bin/activate` |
| Install Package | `pip install package_name` |
| View Packages | `pip list` |
| Export Dependencies | `pip freeze > requirements.txt` |
| Install Requirements | `pip install -r requirements.txt` |
| Upgrade Package | `pip install --upgrade package_name` |
| Uninstall Package | `pip uninstall package_name` |
| Deactivate | `deactivate` |
| Delete Virtual Environment | Delete the `.venv` folder |

---

# Summary

- A virtual environment isolates project dependencies.
- Each project should have its own virtual environment.
- `venv` is Python's built-in solution for creating isolated environments.
- `uv` provides a faster, modern workflow for managing Python projects.
- Use `requirements.txt` to share project dependencies.
- Never commit the `.venv` folder to Git.
- Recreate virtual environments whenever necessary instead of storing them.