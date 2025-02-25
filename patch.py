import os
import numpy as np
import cv2
from skimage.measure import regionprops, label
import glob

def generate_patches(image, mask, padding, patch_size):
    labeled_mask = label(mask)
    regions = regionprops(labeled_mask)
    image_patches = []
    mask_patches = []

    for region in regions:
        # Get bounding box coordinates with padding
        minr, minc, maxr, maxc = region.bbox
        minr = max(minr - padding, 0)
        minc = max(minc - padding, 0)
        maxr = min(maxr + padding, image.shape[0])
        maxc = min(maxc + padding, image.shape[1])

        # Extract and resize image patch
        img_patch = image[minr:maxr, minc:maxc]
        img_patch = cv2.resize(img_patch, patch_size, interpolation=cv2.INTER_AREA)
        
        # Extract and resize mask patch
        msk_patch = mask[minr:maxr, minc:maxc]
        msk_patch = cv2.resize(msk_patch, patch_size, interpolation=cv2.INTER_NEAREST)
        msk_patch = np.where(msk_patch > 0, 255, 0).astype(np.uint8)  # Binarize

        image_patches.append(img_patch)
        mask_patches.append(msk_patch)

    return image_patches, mask_patches

def process_all_patches(image_folder, mask_folder, output_folder):
    """Process all images and create aligned patches"""
    patch_configs = {
        '16x16': {'size': (16, 16), 'padding': 10},
        '32x32': {'size': (32, 32), 'padding': 30},
        '64x64': {'size': (64, 64), 'padding': 30}
    }

    # Create output directories
    for size in patch_configs:
        os.makedirs(os.path.join(output_folder, 'original', size), exist_ok=True)
        os.makedirs(os.path.join(output_folder, 'annotation', size), exist_ok=True)

    # Process each image
    for img_path in glob.glob(os.path.join(image_folder, '*.png')):
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        image = cv2.imread(img_path)
        
        # Find corresponding masks
        mask_paths = glob.glob(os.path.join(mask_folder, f'{base_name}_instance_*.png'))
        
        for mask_path in mask_paths:
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            instance_num = os.path.basename(mask_path).split('_instance_')[-1].split('.')[0]

            for size_name, config in patch_configs.items():
                img_patches, mask_patches = generate_patches(
                    image, mask,
                    padding=config['padding'],
                    patch_size=config['size']
                )

                # Save patches
                for i, (img_patch, mask_patch) in enumerate(zip(img_patches, mask_patches)):
                    patch_id = f"{base_name}_instance_{instance_num}_{i}"
                    
                    # Save original patch
                    cv2.imwrite(
                        os.path.join(output_folder, 'original', size_name, f'{patch_id}.png'),
                        img_patch
                    )
                    
                    # Save annotation patch
                    cv2.imwrite(
                        os.path.join(output_folder, 'annotation', size_name, f'{patch_id}.png'),
                        mask_patch
                    )

        print(f'Processed {base_name}')

# Configuration
image_folder = '/mnt/storage2/PanNuke/neoplastic/neoplastic_images'
mask_folder = '/mnt/storage2/PanNuke/neoplastic/neoplastic_masks'
output_folder = '/mnt/storage2/PanNuke/neoplastic/neoplastic_patch_dataset'

process_all_patches(image_folder, mask_folder, output_folder)

print("Patch generation complete.")

