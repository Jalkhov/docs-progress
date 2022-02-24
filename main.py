import os
import requests
from docspro import DocsPro


def main():
    docs_path = os.environ["INPUT_PATH"]
    print(os.environ)

    docsp = DocsPro(docs_path)
    translated = docsp.translated()
    """
    if docsp.warnings:
        for wrn in docsp.warnings:
            print("::warning ::Review needed")
    """
    print(f"::set-output name=progress::{translated}")


if __name__ == "__main__":
    main()
