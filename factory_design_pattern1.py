from abc import ABC, abstractmethod

# Interface for the Logger
class Logger(ABC):
    @abstractmethod
    def write_log(self, message):
        pass

# Concrete implementation of FileLogger
class FileLogger(Logger):
    def write_log(self, message):
        with open("logfile.txt", "a") as file:
            file.write(f"File Log: {message}\n")

# Concrete implementation of ConsoleLogger
class ConsoleLogger(Logger):
    def write_log(self, message):
        print(f"Console Log: {message}")

# Concrete implementation of DatabaseLogger
class DatabaseLogger(Logger):
    def write_log(self, message):
        # Code to write logs to the database
        print(f"Database Log: {message}")
        # Add your actual database logging code here

# LoggerFactory class to generate loggers
class LoggerFactory:
    @staticmethod
    def get_logger(logger_type):
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type.")

# Sample usage of the logging system
if __name__ == "__main__":
    logger_type = "database"  # Change this to "console" or "database" for different loggers

    logger = LoggerFactory.get_logger(logger_type)
    logger.write_log("This is a log message.")