from config.config_handler import YamlHandler

YAML=YamlHandler('D:\pythonProject1\config\config.yaml')
yaml_data=YAML.read_yaml()
password=yaml_data['mysql']['password']
print(password)

