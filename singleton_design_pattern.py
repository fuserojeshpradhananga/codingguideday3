# Singleton Configuration Manager class
class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.initialize_config()
        return cls._instance

    def initialize_config(self):
        # Here, you can read the configuration settings from a file.
        # For demonstration purposes, we'll use a dictionary as a placeholder.

        # Replace this dictionary with your actual implementation to read from a file.
        self.config = {
            "server_ip": "127.0.0.1",
            "port": 8080,
            "max_connections": 100,
            "timeout": 60,
        }

    def get_config(self):
        return self.config

# Client code
if __name__ == "__main__":
    config_manager1 = ConfigurationManager()
    config1 = config_manager1.get_config()

    config_manager2 = ConfigurationManager()
    config2 = config_manager2.get_config()

    print(config1)
    print(config2)

    # Both config1 and config2 point to the same configuration dictionary
    print(config1 is config2)  # Output: True
