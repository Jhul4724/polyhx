import json

# Config Schema
class ConfigSchema:
    '''
    Variables for the config file
    '''
    PROJECT_ROOT_FOLDER = 'project_root_folder'
    DATA_FOLDER = 'data_folder'
    
    # Database
    DATABASE = 'database'
    DBNAME = 'DATABASE_NAME'
    DB_USERNAME = 'USER_NAME'
    DB_PASSWORD = 'PASSWORD'
    DB_HOST = 'HOST'
    DB_PORT = 'PORT'
    
    # User Credentials
    MIN_PASSWORD_LENGTH = 'min_password_length'


def load_config():
    '''
    Loads the configuration file for the project
    '''
    
    # Get env vars
    with open('config/env_vars.json') as f:
        env_vars = json.load(f)
        project_path = env_vars['project_path']
        config_file = env_vars['config_file']
        db_creds = env_vars['database']

    # Load config
    config = None
    config_path = f'{project_path}/{config_file}'
    with open(
        config_path,
        'r',
    ) as f:
        config = json.load(f)
        config['project_root_folder'] = project_path
        print(f' * Loaded config from {config_path}')

    # Check if config loaded
    if config is None:
        raise RuntimeError('Error: could not load config')
    
    # Set root path
    root_path = config['project_root_folder'] + '/'
    
    # Add root path to folders
    for key in [
        'images',
    ]:
        if key in config.keys():
            config[key] = root_path + config[key]
        
    # Database
    config[ConfigSchema.DATABASE][ConfigSchema.DB_USERNAME] = db_creds['username']
    config[ConfigSchema.DATABASE][ConfigSchema.DB_PASSWORD] = db_creds['password']

    # Return config
    return config

# Load config
config = load_config()
