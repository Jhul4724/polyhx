# Polyhx - Backend

This folder contains the `app.py` script that launches the backend.

# Environment Setup

To run the backend, the user must first ensure that the project is correctly setup. In this demo, we follow a `conda` environment setup.

## `conda` Environment
First, create the `conda` environment:
```bash
conda create -n polyhx python=3.11
```

Then, activate the environment:
```bash
conda activate polyhx
```

## Environment Variables
Under the `backend/config/` folder, create the `env_vars.json` file as follows:
```json
{
    "project_path": "your_project_path",
    "config_file": "config/config.json",
    "database":
    {
        "username": "username",
        "password": "password"
    }
}
```

Naturally, replace the information accordingly.

## Install Requirements
Finally, install the required dependecies:
```bash
pip install -r requirements.txt
```

# Launch the Application
From the backend folder, the user can launch the application:
```bash
python app.py
```

The backend will then be listening on port 5000 (default).

Note that the database is hosted on the port 5432 by default (see [config](/backend/config/config.json#L8)).