
from roboflow import Roboflow
rf = Roboflow(api_key="MsL4eC0bOuqhldoW7zSA")
project = rf.workspace("myfirstproject-hutog").project("ecotrash")
version = project.version(3)
dataset = version.download("yolov8")
                