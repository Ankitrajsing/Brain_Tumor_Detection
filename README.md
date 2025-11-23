The main objective of this project is to develop an efficient and accurate system for
detecting Brain Tumor using advanced image processing techniques. Utilizing the latest
YOLO v12 technology, The project aims to:

1. To perform annotation and segmentation on the brain tumor dataset using the
LabelMe tool, converting annotations into a YOLO-compatible format.

3. To evaluate model performance using key metrics such as mAP (Mean Average
Precision), IoU (Intersection over Union), Precision, Recall, and F1-score,
ensuring high segmentation accuracy.

5. To deploy the trained model for real-time brain tumor detection and segmentation,
making it accessible for medical applications such as diagnosis and treatment
planning.

*3.4 Modules and Their Functionalities*
1. Data Collection and Annotation Module
This module involves the compilation and preprocessing of a brain MRI dataset
containing images labeled into two categories: Tumor and Healthy. Image data is
collected from publicly available repositories and manually annotated using tools
such as LabelMe to provide pixel-wise segmentation masks. These masks are
crucial for training the YOLOv12-Seg model for precise tumor boundary
segmentation. Image dimensions are resized and standardized for compatibility
with the model architecture.

<img width="576" height="313" alt="image" src="https://github.com/user-attachments/assets/53a2a719-2298-4c72-af2a-88baa9d29ca3" />

Accurate annotation plays a crucial role in deep-learning-based medical image
analysis, as it directly impacts the model’s performance and diagnostic reliability. In
this work, brain tumor areas were manually segmented from MRI data using the
LabelMe annotation program. The accurate identification of tumor boundaries was
made possible by the use of a polygon-based annotation approach, which is crucial
considering the irregular and non-uniform geometries of brain tumors. By capturing
the actual structure of the tumor, the polygon-based approach guaranteed a higher
degree of accuracy than bounding-box annotations, which can include non-tumor
regions. To retain a binary classification strategy, a polygon was used to annotate the
full image of healthy brain MRI scans to show whether a tumor was present or not.
This process is visually represented in Photo 3.2, where an original MRI scan (Img1) and its corresponding annotated version (Img-2) are displayed.
*Training and Their Output*
Confusion Matrix
<img width="627" height="763" alt="image" src="https://github.com/user-attachments/assets/c6ce4fae-3472-425d-94bf-4dc228df8d1b" />
Data From Confusion Matrix
<img width="545" height="153" alt="image" src="https://github.com/user-attachments/assets/70de32e1-9a4b-4f8e-8dd7-97d0991d2df8" />
Calculations
<img width="559" height="683" alt="image" src="https://github.com/user-attachments/assets/133aac09-92ad-4e49-a7e8-ae30aef0b8a7" />
F1 Score and P curve
<img width="621" height="875" alt="image" src="https://github.com/user-attachments/assets/792435ed-686d-4018-a74d-bc6d1864294e" />

1. Class Distribution
The dataset consists of two primary object classes:
• Tumor instances: ~1220
• Healthy instances: ~1190
which indicates a well-balanced dataset with nearly equal representation of both
categories, ensuring minimal class imbalance bias during training.
2. Bounding Box Spatial Distribution
The training labels indicate that the bounding boxes are distributed evenly across the
image frame, based on the scatter plot:
• X-center (x): Concentrated between 0.2 and 0.8
• Y-center (y): Mostly within 0.2 to 0.9
which suggests tumors and healthy regions can occur in various spatial locations,
supporting the generalization capability of the model.
3. Bounding Box Dimensions
The normalized width and height of bounding boxes (Figure 1, bottom-right):
• Width: Mostly within 0.05 to 0.35
• Height: Primarily between 0.05 to 0.4
• One rare outlier was observed with both width and height ≈ 1.0, which might
be due to annotation error or background.
This confirms the annotated regions are relatively compact in size, consistent with
typical medical ROI (regions of interest) detection tasks.
🔹 Model Performance Metrics 🔹
✅ Precision: 0.9327
✅ Recall: 0.9245
✅ F1 Score: 0.9286
✅ Accuracy (mAP@50): 0.9536

5. Bounding Box Overlay Map
The top-right subfigure of the label image shows multiple bounding boxes overlaid:
The boxes are concentrated in the central image region, which may indicate a
spatial bias in the dataset (regions of interest are more frequently located centrally)
<img width="616" height="561" alt="image" src="https://github.com/user-attachments/assets/0164f2ad-cfc4-45be-b72c-c2342c5f3d25" />
* PR Curve and R Curve *
  <img width="555" height="728" alt="image" src="https://github.com/user-attachments/assets/e739f3dd-2ac0-44d0-b7df-a7cb34369d1b" />
  Results
  <img width="587" height="345" alt="image" src="https://github.com/user-attachments/assets/c80f14ca-06a0-4218-8b42-fe63436847f1" />


  
  
