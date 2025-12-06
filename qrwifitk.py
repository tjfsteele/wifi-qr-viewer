import subprocess
import re
import qrcode
from PIL import Image, ImageTk
import tkinter as tk

# Step 1: get all profile names
profiles_output = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"], encoding="utf-8"
)
profiles = re.findall(r"All User Profile\s*:\s*(.*)", profiles_output)

# Step 2: build QR images
qr_images = []
labels = []

for ssid in profiles:
    try:
        details = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", f"name={ssid}", "key=clear"],
            encoding="utf-8",
            errors="ignore"
        )
        match = re.search(r"Key Content\s*:\s*(.*)", details)
        password = match.group(1).strip() if match else ""
        if not password:
            continue
        qr_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
        img = qrcode.make(qr_data)
        qr_images.append(img)
        labels.append(ssid)
    except subprocess.CalledProcessError:
        pass

# Step 3: Tkinter viewer
root = tk.Tk()
root.title("Wi-Fi QR Viewer")

index = 0
total = len(qr_images)
# Convert first QR to Tk image
tk_img = ImageTk.PhotoImage(qr_images[index])
label_img = tk.Label(root, image=tk_img)
label_img.pack()

label_text = tk.Label(root, text=f"{labels[index]} ({index+1}/{total})", font=("Arial", 16))
label_text.pack()

def show_qr(new_index):
    global index, tk_img
    if 0 <= new_index < len(qr_images):
        index = new_index
        tk_img = ImageTk.PhotoImage(qr_images[index])
        label_img.config(image=tk_img)
        label_text.config(text=f"{labels[index]} ({index+1}/{total})")

def on_key(event):
    if event.keysym == "Right":
        show_qr(index + 1)
    elif event.keysym == "Left":
        show_qr(index - 1)

root.bind("<Key>", on_key)
root.mainloop()
