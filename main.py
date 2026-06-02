#!/usr/bin/env python3

# Author: jcolours
# Date: 2026-06-02
# Description: ...

import subprocess
import requests
import click
from console import console
from bs4 import BeautifulSoup


def main():
    info = requests.get("https://store.steampowered.com/")

    subprocess.run(["echo"])  # print() does the same thing...

    soup = BeautifulSoup(info.text, "html.parser")

    console.print(f"[bold red]{soup.find_all('a')}")
    console.print(f"[green]{soup.title.text}")


if __name__ == "__main__":
    main()
