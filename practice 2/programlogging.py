import logging

# Configure the logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler()
                    ])

# Create a logger
logger = logging.getLogger(__name__)

def some_function():
    logger.debug("Debug message from some_function")
    logger.info("Info message from some_function")
    logger.warning("Warning message from some_function")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("Error message from some_function", exc_info=True)
    logger.critical("Critical message from some_function")

if __name__ == "__main__":
    logger.info("Starting the script")
    some_function()
    logger.info("Script finished")
