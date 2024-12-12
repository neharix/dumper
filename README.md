# PostgreSQL Auto Backup and Email Notification

This project provides an automated solution to dump a selected PostgreSQL database and send the dump file to designated email accounts. It is useful for database backup, disaster recovery, and monitoring purposes.

## Features

- Automatically dumps a selected PostgreSQL database.
- Sends the database dump to multiple email accounts.
- Configurable settings for the database and email credentials.
- Support for regular backups through scheduling.

## Requirements

- Python 3.10 or higher
- PostgreSQL installed and running
- Required Python libraries:
  - `pytz`
  - `smtplib`
  - `schedule`
    
## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/neharix/dumper.git
    cd dumper
    ```

2. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the backup script manually:
    ```bash
    python main.py
    ```

## Contact

For issues or suggestions, please open an issue or contact me at [azatjurjenov24@gmail.com].
