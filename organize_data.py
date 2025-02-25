import numpy as np
import os
from PIL import Image
from tqdm import tqdm
import random
import math

def organize_data(image_path, mask_path, types_path, test_split):
    '''
    Organizes the images and masks and splits it into train and val splits
    '''
    cell_names = ["neoplastic", "inflammatory", "connective", "dead", "epithelial"]
    
    # Loading the data
    images = np.load(image_path)
    masks = np.load(mask_path)
    types = np.load(types_path)
    
    print('----------Loaded data----------')
    print(f'Images shape: {images.shape}')
    print(f'Masks shape: {masks.shape}')
    print(f'Types shape: {types.shape}')
    
    # Changing the datatype to reduce the size
    images = images.astype(np.uint8)
    masks = masks.astype(np.uint8)
    
    print('----------Reduced size----------')
    
    # Selecting the list of indexes of images with no cells
    if images.shape[0] == 2656:
        index = [584, 586, 604, 748, 750, 780, 811, 812, 813, 828, 830, 832, 833,
                 996, 998, 1147, 1148, 1149, 1152, 1155, 1158, 1160, 1161, 1164,
                 1166, 1432, 1433, 1512, 1578, 1614, 1615, 1616, 1617, 1618, 1619,
                 1620, 1629, 1632, 1704, 1705, 1707, 1708, 1709, 1723, 1724, 1725,
                 1748, 1749, 1750, 1751, 1752, 1753, 1859, 1864, 1870, 1880, 1923,
                 1939, 1940, 1945, 1946, 1966, 1967, 1968, 1969, 1970, 1971, 1972,
                 1973, 1974, 1975, 1976, 1977, 1978, 1979, 2007, 2009, 2019, 2020,
                 2022, 2098, 2108, 2109, 2110, 2111, 2115, 2131, 2132, 2133, 2134,
                 2135, 2137, 2163, 2164, 2165, 2174, 2176, 2202, 2263, 2264, 2265,
                 2267, 2406, 2407, 2462, 2463, 2464, 2465, 2515, 2550, 2551, 2552,
                 2626, 2636, 2639, 2640]
        
        print('----------Removing images with no cells----------')
        
        # Deleting indexes with images which contain no cells
        images = np.delete(images, index, 0)
        masks = np.delete(masks, index, 0)
        types = np.delete(types, index, 0)
    
    print(f'Images shape after removal: {images.shape}')
    print(f'Masks shape after removal: {masks.shape}')
    print(f'Types shape after removal: {types.shape}')
    
    indices = list(range(len(images)))
    random.shuffle(indices)
    train_indices = indices[:math.floor(test_split*len(indices))]
    
    print('----------Splitting indices----------')
    
    # Organising folders
    main_dir = '/mnt/storage2/PanNuke/fold_01'
    if not os.path.isdir(main_dir):
        os.mkdir(main_dir)
    
    for i, (img, mask, tissue_type) in enumerate(tqdm(zip(images, masks, types), total=len(images))):
        phase = "train" if i in train_indices else "val"
        
        tissue_dir = os.path.join(main_dir, tissue_type, phase)
        img_dir = os.path.join(tissue_dir, 'images')
        os.makedirs(img_dir, exist_ok=True)
        
        im = Image.fromarray(img)
        im.save(os.path.join(img_dir, f'image_{i}.png'))
        
        for k in range(mask.shape[2] - 1):  # Subtract 1 to exclude the background channel
            cell_type = cell_names[k]
            
            cell_mask = mask[:,:,k]
            unique_colors = np.unique(cell_mask)
            
            if len(unique_colors) > 1:
                mask_dir = os.path.join(tissue_dir, 'masks', cell_type)
                os.makedirs(mask_dir, exist_ok=True)
                
                for color in unique_colors[1:]:  # Skip background (0)
                    instance_mask = (cell_mask == color).astype(np.uint8) * 255
                    ms = Image.fromarray(instance_mask)
                    ms.save(os.path.join(mask_dir, f'image_{i}_instance_{color}.png'))
            else:
                print(f"No instances found for image {i}, cell type {cell_type}")
    
    print('----------Finished organising----------')

# Usage
image_path = '/mnt/storage2/PanNuke/fold1/images.npy'
mask_path = '/mnt/storage2/PanNuke/fold1/masks.npy'
types_path = '/mnt/storage2/PanNuke/fold1/types.npy'

# Call the function
organize_data(image_path, mask_path, types_path, test_split=0.8)
