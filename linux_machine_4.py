import re
from collections import defaultdict


def count_errors(logfile):
    error_counts = defaultdict(int)
    error_pattern = re.compile(r'^(user\d+): Error')

    with open(logfile, 'r') as file:
        for line in file:
            match = error_pattern.match(line)
            if match:
                user = match.group(1)
                error_counts[user] += 1

    return error_counts


def find_user_with_most_errors(error_counts):
    max_errors = -1
    user_with_max_errors = None
    for user, count in error_counts.items():
        if count > max_errors:
            max_errors = count
            user_with_max_errors = user
    return user_with_max_errors, max_errors


def main():
    logfile = '%SystemRoot%\System32\winevt\Logs'  # Change this to the path of your log file

    error_counts = count_errors(logfile)

    for user, count in error_counts.items():
        print(f'{user} has filed {count} error messages.')

    user_with_max_errors, max_errors = find_user_with_most_errors(error_counts)

    if user_with_max_errors:
        print(f'The user with the most error messages is {user_with_max_errors} with {max_errors} errors.')


if __name__ == '__main__':
    main()
