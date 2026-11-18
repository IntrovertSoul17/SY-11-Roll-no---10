
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different logging levels
logging.debug("This is a debug message")
logging.info("Program started successfully")
logging.warning("This is a warning message")
logging.error("An error occurred")
logging.critical("Critical error occurred")

# Demonstrating logging in a function
def divide(a, b):
    try:
        result = a / b
        logging.info("Division performed successfully")
        print("Result:", result)

    except ZeroDivisionError:
        logging.error("Cannot divide by zero")
        print("Error: Cannot divide by zero")

divide(10, 2)
divide(10, 0)

print("Logging demonstration completed.")
