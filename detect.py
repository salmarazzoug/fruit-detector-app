from roboflow import Roboflow
import sys
import json

image_path = sys.argv[1]

rf = Roboflow(api_key="OEsKx9i1PzEx5sEdAtKW")
project = rf.workspace("zineb-lcfgm").project("fruites-82sjk")
model = project.version(11).model

prediction = model.predict(image_path, confidence=40).json()

print(json.dumps(prediction['predictions']))
