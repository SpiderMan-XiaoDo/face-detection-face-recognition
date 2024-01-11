# Face detection and recognition
This project will utilize the MTCNN model for face detection and employ the FaceNet model for face recognition. Subsequently, it will use the Streamlit library to build an application with the constructed models.

## Abstract:
This project was created by six students from HUSC: Nguyen Luon Mong Do, Vo Dat Van, Nguyen Tien Nhat, Nguyen Ngoc Quang Huy and Nguyen Hoai Nam.


## Installation:

1.Clone this respository:
```
    git clone https://github.com/SpiderMan-XiaoDo/ung_dung_diem_danh.git
```
2.Install the required dependencies:
```
    pip install -r requirements.txt
```
## Data set:

To train the face classification model, you need a dataset of labeled face images.

Our dataset includes 15 videos from 15 students. There are a total of 6879 images in this dataset.

## Method:

* Use MTCNN to detect face and create datasets.
* After that, use Facenet model (apply CASIA-WebFace pre-trained) to train model.
* Finally, use Streamlit to build an application.


## Result:
Run the file ```main.py``` to test your result trained model online in video (You can test your result in camera by change the line ```v_cap = cv2.VideoCapture(0)``` to ```v_cap = cv2.VideoCapture()``` in ```giaodiendiemdanh.py```).

```
cd .\face_recognition\app\app_page
```

```
streamlit run main.py
```


