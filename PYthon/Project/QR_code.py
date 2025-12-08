# =============================================================================
# Description    : Generates a customizable QR code for any website URL
#                  Saves it as an image file (PNG by default)
#                  Requires: qrcode[pil] → pip install qrcode[pil]
# Usage          : Run → python3 qr_code.py
#                  Enter a valid URL and desired filename (e.g. mywebsite.png)
# =============================================================================

# Run these commands once in terminal:
'''
python3 -m venv qr-env
source qr-env/bin/activate
pip install "qrcode[pil]"
# Then run the script
deactivate   # when done
'''
import qrcode                  # Main library for generating QR codes
# Note: Make sure you've installed it with: pip install "qrcode[pil]"

print("QR Code Generator for Websites")
print("=" * 42)

# Get input from user
data = input("\nEnter URL (include https://) : ").strip()

# Basic validation to avoid empty input
if not data:
    print("Error: URL cannot be empty!")
    exit()

# Add https:// if user forgot it (optional convenience)
if not data.startswith(("http://", "https://")):
    data = "https://" + data
    print(f"Added https:// → {data}")

# Get desired filename (recommended to include .png)
file_name = input("\nEnter file name to save (e.g. website.png) : ").strip()

# Default to .png if no extension provided
if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
    file_name += ".png"
    print(f"Using filename: {file_name}")

# Create QR code instance with nice styling
qr = qrcode.QRCode(
    version=1,                 # Controls size (1-40); None = auto
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # ~7% error tolerance
    box_size=10,               # Size of each "box" in pixels
    border=4,                  # White border thickness (minimum 4 is recommended)
)

# Add the URL data and generate the QR code
qr.add_data(data)
qr.make(fit=True)              # Automatically adjust size to fit data

# Generate image (black on white)
image = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Save the QR code image
try:
    image.save(file_name)
    print(f"\nSuccess: QR code saved as '{file_name}'")
    print("You can now scan it with your phone!")
except Exception as e:
    print(f"Error saving file: {e}")

print("\nEND", end='')