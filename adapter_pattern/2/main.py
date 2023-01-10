import json
from bs4 import BeautifulSoup

from xml_adapter import XMLConfig
from experiment import Experiment

def main() -> None:
    with open('config.xml', encoding='utf-8') as file:
        config = file.read()
    bs = BeautifulSoup(config, 'lxml')
    adapter = XMLConfig((bs))
    experiment = Experiment(adapter)
    experiment.run()

if __name__ == "__main__":
    main()