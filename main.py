# -*- coding: utf-8 -*-
"""Flow Launcher plugin: `mc <file path>` -> compress the file via micompress.com."""

import os
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

import webbrowser

from flowlauncher import FlowLauncher, FlowLauncherAPI

from micompress_client.api import CompressError, UTM, compress_file
from micompress_client.categories import category_for

ICON = "Images/app.png"
SITE = "https://micompress.com/?" + UTM
PRESETS = [
    ("recommended", "Recommended", "Best balance of size and quality"),
    ("lossless", "Lossless", "No quality change, smaller where the format allows it"),
    ("extreme", "Extreme", "Smallest possible file"),
]


def _clean_path(query):
    # Explorer's "Copy as path" wraps the path in double quotes.
    return query.strip().strip('"').strip("'")


def _human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return ("%d %s" % (n, unit)) if unit == "B" else ("%.1f %s" % (n, unit))
        n /= 1024.0


def output_path(path):
    root, ext = os.path.splitext(path)
    return root + "-min" + ext


class MiCompress(FlowLauncher):

    def query(self, query):
        path = _clean_path(query)
        if not path:
            return [{
                "Title": "Compress a file with MiCompress",
                "SubTitle": "Type or paste a file path, e.g. mc C:\\Users\\me\\photo.jpg",
                "IcoPath": ICON,
                "JsonRPCAction": {"method": "open_url", "parameters": [SITE]},
            }]
        if not os.path.isfile(path):
            return [{
                "Title": "File not found",
                "SubTitle": path,
                "IcoPath": ICON,
            }]
        if not category_for(os.path.basename(path)):
            return [{
                "Title": "This file type is not supported",
                "SubTitle": "Press Enter to see all supported formats on micompress.com",
                "IcoPath": ICON,
                "JsonRPCAction": {"method": "open_url", "parameters": ["https://micompress.com/all-tools?" + UTM]},
            }]
        size = _human(os.path.getsize(path))
        return [{
            "Title": "Compress %s — %s" % (os.path.basename(path), label),
            "SubTitle": "%s · %s · saves to %s" % (size, hint, os.path.basename(output_path(path))),
            "IcoPath": ICON,
            "JsonRPCAction": {"method": "compress", "parameters": [path, preset]},
        } for preset, label, hint in PRESETS]

    def compress(self, path, preset):
        try:
            data, meta = compress_file(path, preset=preset)
        except CompressError as e:
            FlowLauncherAPI.show_msg("MiCompress: compression failed", str(e), ICON)
            return
        if len(data) >= os.path.getsize(path):
            FlowLauncherAPI.show_msg("MiCompress", "Already optimal — no smaller version found.", ICON)
            return
        out = output_path(path)
        with open(out, "wb") as fh:
            fh.write(data)
        FlowLauncherAPI.show_msg(
            "MiCompress: %d%% smaller" % (meta.get("savedPercent") or 0),
            "%s → %s (%s)" % (os.path.basename(path), os.path.basename(out), _human(len(data))),
            ICON,
        )

    def open_url(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    MiCompress()
