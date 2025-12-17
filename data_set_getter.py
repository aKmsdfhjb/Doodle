import urllib.request
import os

# 1. Define the categories you want
# Note: Use lowercase. For multi-word categories like "alarm clock", use a space.
categories = ['eye', 'dog', 'face', 'apple', 'cookie']

# 2. Define the base URL for the NumPy bitmap files
base_url = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'

# 3. Create a directory to save them
download_dir = 'quickdraw_data'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# 4. Loop and download
for category in categories:
    # Handle URL encoding for spaces (e.g., 'alarm clock' -> 'alarm%20clock')
    category_url = category.replace(' ', '%20')
    url = f"{base_url}{category_url}.npy"
    save_path = os.path.join(download_dir, f"{category}.npy")

    print(f"Downloading {category}...")
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Success: Saved to {save_path}")
    except Exception as e:
        print(f"Error downloading {category}: {e}")

print("All done!")