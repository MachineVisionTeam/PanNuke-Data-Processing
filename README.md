# PanNuke Dataset Processing

This repository contains scripts to process the PanNuke dataset, organize it into train and validation sets, and generate image patches for further analysis. The PanNuke dataset consists of 19 tissue types with 5 class types, and this repository focuses on processing `fold1` of the dataset.

## Overview

The PanNuke dataset is a large-scale dataset for nuclei instance segmentation and classification in histology images. It contains images and masks for 19 different tissue types, with 5 class types: `neoplastic`, `inflammatory`, `connective`, `dead`, and `epithelial`. This repository provides scripts to:

1. Organize the dataset into train and validation splits.
2. Extract specific cell types (e.g., neoplastic cells) and their corresponding masks.
3. Generate image patches at different resolutions (16x16, 32x32, 64x64) for training machine learning models.

## Repository Structure

```plaintext
PanNuke-Data-Processing/
├── README.md         # This file
├── organize_data.py  # Script to organize the dataset into train/val splits
├── celltypes.py      # Script to extract specific cell types (e.g., neoplastic)
├── patch.py          # Script to generate image patches
└── requirements.txt  # List of Python dependencies
```

## Dataset Preparation

The PanNuke dataset is organized into 3 folds (`fold1`, `fold2`, `fold3`). This repository processes `fold1`, which contains the following files:

*   `images.npy`: NumPy array of images.
*   `masks.npy`: NumPy array of masks.
*   `types.npy`: NumPy array of tissue types.

**Important:** You must download the PanNuke dataset `fold1` separately from the official source (https://warwick.ac.uk/fac/cross_fac/tissueimageanalytics/data/panuke/)  and place the `images.npy`, `masks.npy`, and `types.npy` files in a directory accessible to the scripts.

### Step 1: Organize the Dataset

The `organize_data.py` script organizes the dataset into train and validation splits. It removes images with no cells and saves the images and masks into a structured directory format.

#### Usage

1.  **Modify Paths:**  Edit the `image_path`, `mask_path`, and `types_path` variables in the `organize_data.py` script to point to the correct locations of your downloaded `.npy` files.
2.  **Run the script:**

    ```
    python organize_data.py
    ```

#### Output Directory Structure

After running the script, the dataset will be organized as follows:


