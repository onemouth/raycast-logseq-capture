#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title log
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🪵
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.argument2 { "type": "text", "placeholder": "source" }
# @raycast.packageName logseq-log

# Documentation:
# @raycast.description generate html ruby snippets
# @raycast.author onemouth

import webbrowser
import sys
from urllib.parse import urlencode

content = sys.argv[1]
content_url = sys.argv[2]
query_params = {'content': content, 'url': content_url, 'append': 'true', 'page': 'TODAY'}
query_string = urlencode(query_params)


url = f"logseq://x-callback-url/quickCapture?{query_string}"

webbrowser.open(url, new=0)
