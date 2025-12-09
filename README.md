## 🏡 README.md: YOLOv8 Multi-Class Home Objects Detection

This project showcases the rapid deployment of a multi-class object detection model using the **Ultralytics YOLOv8n** architecture and the built-in, publicly available **HomeObjects-3K dataset**. The goal was to train a high-performing model for identifying common furniture and household features in indoor scenes.

---

### 1. 🌟 Project Highlights

* **Task:** Multi-Class Object Detection (12 Classes).
* **Model:** YOLOv8n (Nano).
* **Dataset Source:** Built-in `HomeObjects-3K.yaml` (3,000+ images).
* **Key Achievement:** Instant data setup and configuration by leveraging the Ultralytics alias, eliminating the need for manual data collection and annotation.

---

### 2. 📊 Performance Metrics (100 Epochs)

The final model performance was validated on the HomeObjects-3K validation set (404 images) and yielded **excellent results**, achieving a high balance between Precision and Recall.

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **mAP50-95** | **$0.4898$** | **Overall Quality Score.** Strong performance across multiple Intersection over Union (IoU) thresholds. |
| **mAP50** | $0.6893$ | **High Accuracy at $\text{IoU}=0.5$.** The model correctly identifies objects nearly $69\%$ of the time. |
| **Precision (P)** | $0.6942$ | **Low False Positives.** When the model makes a prediction, it is correct about $69.4\%$ of the time. |
| **Recall (R)** | $0.6267$ | **Strong Object Finding.** The model successfully finds $62.7\%$ of all objects present in the validation set. |
| **Inference Speed** | $56.5\text{ms}$ per image | Suitable for near real-time video processing. |

---

### 3. 🎯 Detected Classes (HomeObjects-3K)

The model is trained to recognize **12 distinct indoor objects**:

* **Furniture & Electronics:** `bed`, `sofa`, `chair`, `table`, `lamp`, `tv`, `laptop`, `wardrobe`
* **Features & Decor:** `window`, `door`, `potted plant`, `photo frame`

---

### 4. 💻 Setup and Training

The simplicity of this project lies in the training command, which handles the entire data pipeline automatically.

5. 🚀 Inference and Validation
The trained weights (best.pt) can be loaded for inference and validation on new images.

Note: The HomeObjects-3K.yaml file must be present in the local directory for the validation step to define the classes and dataset path correctly.
