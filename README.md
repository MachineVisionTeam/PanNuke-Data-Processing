# PanNuke Dataset Processing

This repository contains scripts to process the PanNuke dataset, organize it into train and validation sets, and generate image patches for further analysis. The PanNuke dataset consists of 19 tissue types with 5 class types, and this repository focuses on processing `fold1` of the dataset.

![PanNuke Dataset](images/pannuke1.png)

## Citations  
If you use the PanNuke dataset or code in your research, please cite the following papers:  

### Task-Ready PanNuke and NuCLS Datasets: Reorganization, Synthetic Data Generation, and Experimental Evaluation.

**Koganti, S.C., Yellu, S., Yun, J., & Lee, S.** (2025). Task-Ready PanNuke and NuCLS Datasets: Reorganization, Synthetic Data Generation, and Experimental Evaluation. *IEEE Access*, **13**, 125275–125286. https://doi.org/10.1109/ACCESS.2025.3589477

### PanNuke: An Open Pan-Cancer Histology Dataset for Nuclei Instance Segmentation and Classification  
**Jevgenij Gamper, Navid Alemi Koohbanani, Ksenija Benes, Ali Khuram, Nasir Rajpoot**  
*European Congress on Digital Pathology, 2019, Pages 11–19.*  
[DOI: 10.1007/978-3-030-23937-4_2](https://doi.org/10.1007/978-3-030-23937-4_2)  

### PanNuke Dataset Extension, Insights and Baselines  
**Jevgenij Gamper, Navid Alemi Koohbanani, Simon Graham, Mostafa Jahanifar, Syed Ali Khurram, Ayesha Azam, Katherine Hewitt, Nasir Rajpoot**  
*arXiv preprint arXiv:2003.10778, 2020.*  
[DOI: 10.48550/arXiv.2003.10778](https://doi.org/10.48550/arXiv.2003.10778)  

---
### BibTeX Entries

For convenience, here are the BibTeX entries for inclusion in academic papers:

```bibtex
@article{11080424,
  author={Koganti, Sai Chandana and Yellu, Siri and Yun, Jihoon and Lee, Sanghoon},
  journal={IEEE Access}, 
  title={Task-Ready PanNuke and NuCLS Datasets: Reorganization, Synthetic Data Generation, and Experimental Evaluation}, 
  year={2025},
  volume={13},
  pages={125275-125286},
  doi={10.1109/ACCESS.2025.3589477}
}

@inproceedings{gamper2019pannuke,
  title={PanNuke: an open pan-cancer histology dataset for nuclei instance segmentation and classification},
  author={Gamper, Jevgenij and Koohbanani, Navid Alemi and Benes, Ksenija and Khuram, Ali and Rajpoot, Nasir},
  booktitle={European Congress on Digital Pathology},
  pages={11--19},
  year={2019},
  organization={Springer},
  doi={10.1007/978-3-030-23937-4_2}
}

@article{gamper2020pannuke,
  title={PanNuke Dataset Extension, Insights and Baselines},
  author={Gamper, Jevgenij and Koohbanani, Navid Alemi and Graham, Simon and Jahanifar, Mostafa and Khurram, Syed Ali and Azam, Ayesha and Hewitt, Katherine and Rajpoot, Nasir},
  journal={arXiv preprint arXiv:2003.10778},
  year={2020},
  doi={10.48550/arXiv.2003.10778}
}
```

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

**Important:** You must download the PanNuke dataset `fold1` separately from the official source (https://warwick.ac.uk/fac/cross_fac/tia/data/pannuke)  and place the `images.npy`, `masks.npy`, and `types.npy` files in a directory accessible to the scripts.

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

```plaintext
/mnt/storage2/PanNuke/fold_01/
├── Adrenal_gland/
│   ├── train/
│   │   ├── images/         # Training images
│   │   └── masks/
│   │       ├── neoplastic/     # Neoplastic cell masks
│   │       ├── inflammatory/   # Inflammatory cell masks
│   │       └── ... (other cell types)
│   └── val/
│       ├── images/         # Validation images
│       └── masks/
│           ├── neoplastic/     # Neoplastic cell masks
│           ├── inflammatory/   # Inflammatory cell masks
│           └── ... (other cell types)
├── Bile-duct/
│   └── ... 
└── ... (other tissue types)
```

### Step 2: Extract Specific Cell Types

The `celltypes.py` script extracts specific cell types (e.g., neoplastic cells) and their corresponding masks. It copies the relevant images and masks into new directories.

#### Usage
 ```
python celltypes.py
 ```

#### Output Directory Structure

After running the script, the extracted data will be saved as follows:

```plaintext
/mnt/storage2/PanNuke/neoplastic/
├── neoplastic_images/ # Extracted neoplastic images
└── neoplastic_masks/ # Extracted neoplastic masks
```

### Step 3: Generate Image Patches

The `patch.py` script generates image patches at different resolutions (16x16, 32x32, 64x64) from the extracted images and masks.

#### Usage
 ```
python patch.py
 ```

#### Output Directory Structure

After running the script, the patches will be saved as follows:

```plaintext
/mnt/storage2/PanNuke/neoplastic/neoplastic_patch_dataset/
├── original/
│   ├── 16x16/                  # 16x16 image patches
│   ├── 32x32/                  # 32x32 image patches
│   └── 64x64/                  # 64x64 image patches
└── annotation/
    ├── 16x16/                  # 16x16 mask patches
    ├── 32x32/                  # 32x32 mask patches
    └── 64x64/                  # 64x64 mask patches
```
![PanNuke Dataset](images/exact_size_viz_Bile-duct_train_image_1582_instance_170_0.png)

![PanNuke Dataset](images/exact_size_viz_Pancreatic_train_image_1266_instance_211_0.png)

## Requirements

To run the scripts, you need the following Python packages:

*   numpy
*   opencv-python
*   scikit-image
*   Pillow (PIL)
*   tqdm

You can install the dependencies using:
 ```
pip install -r requirements.txt
 ```

## Usage Example

1.  Clone the repository:

    ```
    git clone https://github.com/chandana-koganti14/PanNuke-Data-Processing.git
    cd PanNuke-Data-Processing
    ```

2.  Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

3.  Download the PanNuke dataset `fold1` and place the `.npy` files in a directory of your choice.

4.  Modify the file paths in `organize_data.py` to point to the correct locations of your downloaded `.npy` files.  The other scripts use hardcoded paths, so make sure your data matches those.

5.  Run the scripts in order:

    ```
    python organize_data.py
    python celltypes.py
    python patch.py
    ```



Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.




