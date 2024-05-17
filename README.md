# ISIC 2018 Skin Lesion Segmentation Challenge

This repository contains the implementation of a U-Net model for binary skin lesion area segmentation based on dermatoscopic images, using PyTorch. The dataset used is derived from the ISIC 2018 Task 1 challenge.

## Dataset

The ISIC 2018 dataset provides images and binary segmentations for skin lesion analysis. The dataset is divided into three phases:

- **Train Phase**: Contains images and corresponding binary segmentation masks.
- **Validation Phase**: Contains images used to validate the model's performance.
- **Test Phase**: Contains images used for the final evaluation.

The dataset can be accessed via the ISIC Archive Challenge Submission Page [here](https://challenge2018.isic-archive.com/task1/).

For further information about the dataset and to access additional images, metadata, and segmentations, visit the [ISIC Archive](https://www.isic-archive.com/).

If you use this data, please reference the following paper:
```
Noel Codella, Veronica Rotemberg, Philipp Tschandl, M. Emre Celebi, Stephen Dusza, David Gutman, Brian Helba, Aadi Kalloo, Konstantinos Liopyris, Michael Marchetti, Harald Kittler, Allan Halpern: “Skin Lesion Analysis Toward Melanoma Detection 2018: A Challenge Hosted by the International Skin Imaging Collaboration (ISIC)”, 2018; https://arxiv.org/abs/1902.03368
```

## Model: U-Net

The U-Net architecture is widely used for biomedical image segmentation tasks. The model consists of an encoder-decoder structure with skip connections to capture both high-level and low-level features effectively.

### Training and Validation

The U-Net model was trained using the ISIC 2018 dataset. Below are the training and validation loss values at epoch 4:

- **Train Loss (Epoch 4)**: 0.3614
- **Validation Loss (Epoch 4)**: 0.3658

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:
- PyTorch
- Torchvision
- NumPy
- OpenCV
- Matplotlib

You can install the required packages using:
```sh
pip install torch torchvision numpy opencv-python matplotlib
```

## Results

The model shows promising results with a training loss of 0.3614 and a validation loss of 0.3658 at epoch 4. Further training and hyperparameter tuning are recommended to improve the performance.

## Acknowledgements

We acknowledge the efforts of the ISIC 2018 challenge organizers and contributors for providing the dataset and hosting the challenge.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [2021ucs0110@iitjammu.ac.in](mailto:2021ucs0110@iitjammu.ac.in).

---

