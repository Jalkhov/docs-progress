import os
import requests

def main():
    translations_path = os.environ["INPUT_PATH"]
    print(f"::set-output name=progress::{translations_path}")


if __name__ == "__main__":
    main()
