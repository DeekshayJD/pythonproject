import logging

# Configure logging
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("error.log"),
                              logging.StreamHandler()])

logger = logging.getLogger(__name__)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        logger.error(f"The file {file_path} was not found.", exc_info=True)
        return None

if __name__ == "__main__":
    file_path = 'nonexistent_file.txt'
    content = read_file(file_path)
    if content is None:
        file_path = input("Please provide an alternative file path: ")
        content = read_file(file_path)
        if content is None:
            print("Failed to read the file. Exiting.")
        else:
            print("File read successfully.")
