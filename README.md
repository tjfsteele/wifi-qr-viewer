# Wi-Fi QR Viewer

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-qrcode%20%7C%20Pillow%20%7C%20tkinter-orange.svg)

A Python utility to recover and transfer Wi-Fi credentials from Windows to a new phone.



\## Features

\- Extracts all saved Wi-Fi profiles using `netsh`.

\- Generates QR codes for each SSID + password.

\- Interactive viewer: press → for next, ← for previous.

\- Skips open networks (no password).

\- Displays SSID and progress counter (e.g. `CafeNet (12/87)`).



\## Requirements

\- Windows 10/11

\- Python 3.9+

\- Packages: `qrcode`, `Pillow`, `tkinter`



Install dependencies:

```bash

pip install qrcode[pil]

pip install tkinter

