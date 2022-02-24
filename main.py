import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    translations_path = os.environ["INPUT_TRANSLATIONS_PATH"]
    only_languages = os.environ["INPUT_ONLY_LANGUAGES"]
    token = os.environ["INPUT_TOKEN"]
    min_coverage = os.environ["INPUT_MIN_COVERAGE"]

    progress = f"""
        translations_path = {translations_path}
        only_languages = {only_languages}
        token = {token}
        min_coverage = {min_coverage}
    """

    print(f"::set-output name=progress::{progress}")


if __name__ == "__main__":
    main()
