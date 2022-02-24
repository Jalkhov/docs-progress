import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    translations_path = os.environ["INPUT_TRANSLATIONS_PATH"]
    only_languages = os.environ["INPUT_ONLY_LANGUAGES"]
    token = os.environ["INPUT_TOKEN"]
    min_coverage = os.environ["INPUT_MIN_COVERAGE"]

    print(f"::set-output name=translations_path::{translations_path}")
    print(f"::set-output name=only_languages::{only_languages}")
    print(f"::set-output name=token::{token}")
    print(f"::set-output name=min_coverage::{min_coverage}")


if __name__ == "__main__":
    main()
