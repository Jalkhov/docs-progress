import os
import requests
from docspro import DocsPro


def main():
    docs_path = os.environ["INPUT_PATH"]
    docsp = DocsPro(docs_path)
    translated = docsp.translated()

    print(f"::set-output name=progress::{translated}")


if __name__ == "__main__":
    main()
