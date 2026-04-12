# SPDX-FileCopyrightText: 2026-present Alexander Puck Neuwirth <alexander@neuwirth-informatik.de>
#
# SPDX-License-Identifier: MIT

import requests
import sys

def get_inspire_bibtex(query: str) -> str:
    url = "https://inspirehep.net/api/literature"
    params = {
        "q": query,
        "format": "bibtex",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.text

def main():
    query = " ".join(sys.argv[1:])
    print(get_inspire_bibtex(query))

if __name__ == "__main__":
    main()