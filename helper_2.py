from ultralytics import YOLO
import time
import streamlit as st
import cv2
import settings_2 as settings
import threading

def sleep_and_clear_success():
    time.sleep(3)
    st.session_state['botol_bekas'].empty()
    st.session_state['gelas_bekas'].empty()

def load_model(model_path):
    model = YOLO(model_path)
    return model

def classify_waste_type(detected_items):
    
    return set(detected_items)

def remove_dash_from_class_name(class_name):
    return class_name.replace("_", " ")

def _display_detected_frames(model, st_frame, image):
    image = cv2.resize(image, (640, int(640*(9/16))))
    
    if 'unique_classes' not in st.session_state:
        st.session_state['unique_classes'] = set()

    if 'gelas_bekas' not in st.session_state:
        st.session_state['gelas_bekas'] = st.sidebar.empty()
    if 'botol_bekas' not in st.session_state:
        st.session_state['botol_bekas'] = st.sidebar.empty()

    if 'last_detection_time' not in st.session_state:
        st.session_state['last_detection_time'] = 0

    res = model.predict(image, conf=0.6)
    names = model.names
    detected_items = set()

    for result in res:
        new_classes = set([names[int(c)] for c in result.boxes.cls])
        if new_classes != st.session_state['unique_classes']:
            st.session_state['unique_classes'] = new_classes
            st.session_state['gelas_bekas'].markdown('')
            st.session_state['botol_bekas'].markdown('')
            detected_items.update(st.session_state['unique_classes'])

            detected = classify_waste_type(detected_items)
            for item in detected:
                if item == "Botol bekas":
                    recommended = settings.RECOMMENDED.get("botol_bekas")
                    recommended = [f"""<img src='{r.get("link")}' alt='image'>
                                   <ul>
                                   <li>Nama Produk = {r.get("nama")}</li>
                                   <li>Tag = "gelas_bekas"</li>
                                   <li>Harga = {r.get("harga")}</li>
                                   <li>Satuan = {r.get("satuan")}</li>
                                   </ul>""" for r in recommended]
                    st.session_state['botol_bekas'].markdown(
                        "<br><br>".join(recommended),
                        unsafe_allow_html=True
                    )
                if item == "gelas bekas":
                    recommended = settings.RECOMMENDED.get("gelas_bekas")
                    recommended = [f"""<img src='{r.get("link")}' alt='image'>
                                   <ul>
                                   <li>Nama Produk = {r.get("nama")}</li>
                                   <li>Tag = "gelas_bekas"</li>
                                   <li>Harga = {r.get("harga")}</li>
                                   <li>Satuan = {r.get("satuan")}</li>
                                   </ul>""" for r in recommended]
                    st.session_state['gelas_bekas'].markdown(
                        "<br><br>".join(recommended),
                        unsafe_allow_html=True
                    )
            threading.Thread(target=sleep_and_clear_success).start()
            st.session_state['last_detection_time'] = time.time()

    res_plotted = res[0].plot()
    st_frame.image(res_plotted, channels="BGR")


def play_webcam(model):
    source_webcam = settings.WEBCAM_PATH
    if st.button('Mulai Deteksi'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(model,st_frame,image)
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))
