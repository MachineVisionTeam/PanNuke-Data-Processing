import os
import shutil
from pathlib import Path

# Base directory for your dataset
base_dir = Path("/mnt/storage2/PanNuke/fold_01")

# New directories for connective images and masks
new_image_dir = Path("/mnt/storage2/PanNuke/neoplastic/neoplastic_images")
new_mask_dir = Path("/mnt/storage2/PanNuke/neoplastic/neoplastic_masks")

# Create new directories if they don't exist
new_image_dir.mkdir(parents=True, exist_ok=True)
new_mask_dir.mkdir(parents=True, exist_ok=True)

# List of tissue types
tissue_types = [
    "Adrenal_gland", "Bile-duct", "Bladder", "Breast", "Cervix", "Colon",
    "Esophagus", "HeadNeck", "Kidney", "Liver", "Lung", "Ovarian",
    "Pancreatic", "Prostate", "Skin", "Stomach", "Testis", "Thyroid", "Uterus"
]

# Function to process the specified fold
def process_fold():
    for tissue in tissue_types:
        for split in ['train', 'val']:
            mask_dir = base_dir / tissue / split / "masks" / "neoplastic"
            image_dir = base_dir / tissue / split / "images"
            
            if not mask_dir.exists():
                continue
            
            for mask_file in mask_dir.glob("*.png"):
                # Get the corresponding image file name
                image_name = f"{mask_file.name.split('_instance_')[0]}.png"
                image_file = image_dir / image_name
                
                if image_file.exists():
                    shutil.copy(mask_file, new_mask_dir / f"{tissue}_{split}_{mask_file.name}")
                    shutil.copy(image_file, new_image_dir / f"{tissue}_{split}_{image_name}")


process_fold()

print("Processing complete. Epithelial images and masks have been copied to new directories.")
