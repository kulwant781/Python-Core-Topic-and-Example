import argparse
import urllib.request
import os

def download_image(image_url, save_path):
    try:
        # Request the image
        request = urllib.request.Request(image_url)
        response = urllib.request.urlopen(request)
        
        print(f"Downloading: {image_url}")
        
        # Save the image
        with open(save_path, 'wb') as local_file:
            local_file.write(response.read())

        print(f"Image saved as: {save_path}")
        return save_path

    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def main():
    # Create an ArgumentParser object with a description
    parser = argparse.ArgumentParser(description="Download an image from a URL.")
    
    # Define command-line arguments
    parser.add_argument("image", help="URL of the image to download")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Define save location
    save_directory = "bewimag1e" # this is the creating a folder  and directory in local system
    os.makedirs(save_directory, exist_ok=True)  # Create folder if it doesn't exist
    save_path = os.path.join(save_directory, "new_pdf.pdf")

    # Download the image
    result = download_image(args.image, save_path)

    # Display the result
    if result:
        print(f"The image was successfully downloaded to: {result}")
    else:
        print("Failed to download the image.")

if __name__ == "__main__":
    main()



