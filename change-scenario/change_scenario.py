import json
import logging

def main():
    try:
        path_server_config = r"<<SERVER_CONFIG_PATH>>.json"
        path_scenario_config = r"<<SCENARIO_CONFIG_PATH>>.json"
        path_log_file = r"<<LOG_FILE_PATH>>.log"
        
        logging.basicConfig(
            filename=path_log_file,
            level=logging.INFO,
            format="%(levelname)s\t [%(asctime)s]\t%(message)s",
            datefmt="%d.%m.%Y %H:%M:%S",
        )

        server_config = load_json(path_server_config)
        scenario_config = load_json(path_scenario_config)

        current = scenario_config.get("current")
        scenarios = scenario_config.get("scenarios", [])

        logging.info(f"Current scenario ID: {current}")
        logging.info(f"Current scenario name: {scenarios[current]['name']}")
        logging.info(f"Current scenarioId: {scenarios[current]['scenarioId']}")

        if current == -1:
            current = len(scenarios) - 1

        if current >= len(scenarios) - 1:
            current = 0

        new = current + 1

        logging.info(f"Next scenario ID: {new}")
        logging.info(f"Next scenario name: {scenarios[new]['name']}")
        logging.info(f"Next scenarioId: {scenarios[new]['scenarioId']}")

        try:
            server_config["game"]["scenarioId"] = scenarios[new]["scenarioId"]
        except Exception as e:
            logging.error(f"Error setting scenarioId in server_config: {e}")
            raise

        save_json(path_server_config, server_config)

        scenario_config["current"] = new
        save_json(path_scenario_config, scenario_config)

    except Exception as e:
        logging.error(f"Unhandled exception: {e}")

def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load {path}: {e}")
        raise

def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Failed to save {path}: {e}")
        raise

if __name__ == "__main__":
    main()
