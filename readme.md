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
## Dataset:

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
The results achieved by the face detection and classification model trained on your dataset will vary depending on various factors such as the quality of your dataset, the size of the training set, and the hyperparameters. We recommend you to experiment with different configurations to achieve the best results for your specific use case.


<p align="center">
  <img src="asset/img/diemdanh.png"width="541" height="241">
</p>

## References
* Rongrong Jin; Hao Li; Jing Pan; Wenxi Ma; and Jingyu Lin. Face recognition based on mtcnn and facenet. 2020.
* Siyao Qi, Xinyu Zuo, Weijia Feng, and I G Naveen. Face recognition model based on mtcnn and facenet. In 2022 IEEE 2nd International Conference on Mobile Networks and Wireless Communications (ICMNWC), pages 1–5, 2022.
* Florian Schroff, Dmitry Kalenichenko, and James Philbin. Facenet: A unified embedding for face recognition and clustering. In 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 815–823, 2015.
* F. Schroff; D. Kalenichenko and J. Philbin. Facenet: A unified embedding for face recognition and clustering. 2015.
* Application: Streamlit