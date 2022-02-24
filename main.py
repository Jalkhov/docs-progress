import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    translations_path = os.environ["INPUT_PATH"]
    token = os.environ["INPUT_TOKEN"]

    progress = f"""
        translations_path = {translations_path}
    """

    print(f"::set-output name=progress::{progress}")


if __name__ == "__main__":
    main()
