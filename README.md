# Recyclable waste recommendation system
This project demonstrates waste detection using a YOLOv8 (You Only Look Once) object detection model. It identifies recyclable, non-recyclable, and hazardous waste items in a webcam stream.



## Setup

**Clone the Repository:**
```bash
git clone https://github.com/Tegarr123/EcoTrashTML.git
cd EcoTrashTML
```
**Install Dependencies:**
```bash
pip install -r requirements.txt
```
**Run the Application**
```bash
streamlit run app_2.py
```
Open your web browser and navigate to the provided URL (usually http://localhost:8501). You will see the EcoTrash App.

## Project Structure

- `app_2.py`: Main application file containing Streamlit code.
- `helper_2.py`: Helper functions for waste detection using the YOLO model.
- `settings_2.py`: Configuration settings, including the path to the YOLO model and waste types.
- `train.py`: To train the model
