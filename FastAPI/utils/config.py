import os
import yaml

class ConfigLoader:

    def __init__(self, filename='config.yml'):
        config_dir = os.path.join(os.getcwd(), 'config')
        self.config_path = os.path.join(config_dir, filename)
        
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config_data = yaml.safe_load(f)
            return config_data
        except FileNotFoundError:
            raise FileNotFoundError(f'Archivo de configuración no encontrado: {self.config_path}')

    def get_config(self):
        return self.config

