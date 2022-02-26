import os
from core import Docsprogress


def main():
    path = os.environ["INPUT_PATH"]
    multilang = os.environ["INPUT_MULTILANG"]
    ignore_langs = os.environ["INPUT_IGNORE-LANGUAGES"]

    docsp = Docsprogress(path, multilang=multilang, ignore_langs=ignore_langs)
    translated = docsp.translated()
    """
    if docsp.warnings:
        for wrn in docsp.warnings:
            print("::warning ::Review needed")
    """
    print(f"::set-output name=progress::{translated}")


if __name__ == "__main__":
    main()
