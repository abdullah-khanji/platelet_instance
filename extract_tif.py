from PIL import Image
import os


def extract_images_from_tif(tif_path, output_folder):
    """
    Extracts images from a multi-page TIFF file and saves each image as a PNG file.

    :param tif_path: Path to the multi-page TIFF file.
    :param output_folder: Folder to save the extracted PNG images.
    """
    # Open the multi-page TIFF file
    tif = Image.open(tif_path)
    
    # Make sure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Loop through all the frames/pages in the TIFF file
    for i in range(tif.n_frames):
        # Set the frame/page to the current index
        tif.seek(i)
        
        # Save the current frame as a PNG file
        output_path = os.path.join(output_folder, f"image_{i+1}.png")
        tif.save(output_path, format="PNG")
        print(f"Saved {output_path}")

if __name__ == "__main__":
    # Example usage
    
    labels=['./platelet-em/labels-semantic/24-semantic.tif']
    output_labels = ['./data/test_labels']
   

    # images_paths=['./platelet_data/train-images.tif', './platelet_data/eval-images.tif']
    # labels=['./platelet_data/train-labels.tif', './platelet_data/eval-labels.tif']
    # output_images=['./data/output/train_images/', './data/output/val_images/']
    # output_labels=['./data/output/train_labels/', './data/output/val_labels/']

        
    for i in range(0, len(labels)):
        extract_images_from_tif(labels[i], output_labels[i])

