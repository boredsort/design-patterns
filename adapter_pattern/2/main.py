import json

from experiment import Experiment

def main() -> None:
    with open('config.xml', encoding='utf-8') as file:
        config = file.read()

    experiment = Experiment(config)
    experiment.run()

if __name__ == "__main__":
    main()