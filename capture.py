#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title log
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "text" }
# @raycast.argument2 { "type": "text", "placeholder": "source" }
# @raycast.packageName furigana

# Documentation:
# @raycast.description generate html ruby snippets
# @raycast.author onemouth

import webbrowser
import sys

url = f"logseq://x-callback-url/quickCapture?content={sys.argv[1]}&url={sys.argv[2]}"

webbrowser.open(url, new=0)
