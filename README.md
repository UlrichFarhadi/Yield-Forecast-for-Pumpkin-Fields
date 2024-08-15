# Yield Forecast for Pumpkin Fields

This project focuses on performing yield forecasting for pumpkin fields by estimating the number of pumpkins present. The approach leverages a counting algorithm based on the Yolov5 neural network foundation model to detect pumpkins. The project also employs a tiling method to partition a large orthomosaic into smaller, manageable tiles (200x200 or 500x500 pixels) for model processing. To avoid double-counting, the algorithm accounts for overlap between tiles.

### Overview

Aerial photographs captured via drone were processed using Agisoft Metashape (or a preferred alternative) to create an orthomosaic image.

![Orthomosaic](Orthomosaic%20Files/Orthomosaic.jpg)

The orthomosaic was divided into tiles of either 200x200 or 500x500 pixels. While the 500x500 tiles provided better performance, they were significantly slower to process. Given that rapid computation was not a priority, the 500x500 tiling approach was adopted. The orthomosaic was split into 2266 tiles for the 200x200px configuration and 369 tiles for the 500x500px configuration.

### Dataset Creation and Model Training

To fine-tune the Yolov5 model, a dataset was created using 100 tiles (416x416 pixels each). These tiles were manually labeled and annotated using LabelMe 3.0, with the annotations saved in Pascal VOC format.

The dataset was divided into:
- **Training Set:** 66 tiles (augmented to 180 tiles for better generalization)
- **Validation Set:** 20 tiles
- **Test Set:** 14 tiles

Data augmentation was employed to enhance the training set, improving the model's robustness to variations in lighting, noise, and other environmental factors. Below is a showcase of the training data before and after augmentation:

<p align="center">
  <img src="Dataset%20Showcase/Non_Augmented_train_data_GT_showcase.jpg" alt="Non-Augmented Training Data" width="45%">
  <img src="Dataset%20Showcase/Augmented_train_data_GT_showcase.jpg" alt="Augmented Training Data" width="45%">
</p>

### Detection and Post-Processing

The `detect.py` script detects bounding boxes in each tile and counts the detected pumpkins. Subsequently, the `postprocess_mosaic.py` script reconstructs the orthomosaic by stitching together the tiles, highlighting the detected pumpkins.

![Detected Pumpkins](Orthomosaic%20Files/mosaic_pumpkins_detected_500px.jpg)

### Accuracy

The yield forecasting pipeline estimates the total pumpkin count with an accuracy of approximately 95%.
