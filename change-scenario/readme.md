## change_scenario.py script

This script manages scenario switching for a game server by updating scenario configuration files and logging the changes.

### Configure paths
   Edit the script to set the correct paths for:
   - `SERVER_CONFIG_PATH`
   - `SCENARIO_CONFIG_PATH`
   - `LOG_FILE_PATH`

### What it does

- Loads server and scenario configuration from JSON files.
- Logs the current scenario information.
- Advances to the next scenario (with wrap-around).
- Updates the server config with the new scenario ID.
- Saves changes to both config files.
- Logs all actions and errors.

### Logging

All actions and errors are logged to the file specified by `LOG_FILE_PATH`.

### Requirements

- Python 3.x

## cron setup

### 1 - Open your crontab file

Run this command:

~~~bash
crontab -e
~~~


### 2 - Add the cron job
At the bottom of the file, add this line:

~~~cron
0 7 * * 3 /usr/bin/python3 /path/to/your/script.py
~~~

Explanation:

- `0 7 * * 3`: means 7:00 AM every Wednesday (3 = Wednesday)
- `/usr/bin/python3`: the full path to Python 3 (verify with which python3)
- `/path/to/your/script.py`: replace with the actual path to your script

### 3 - Save and exit
In nano, press CTRL+O, Enter to save, then CTRL+X to exit.