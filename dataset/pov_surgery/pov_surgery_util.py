import numpy as np
import json
import os
import cv2
from PIL import Image
import trimesh

def load_objects_POV_SURGERY(obj_root):
    object_names = ['diskplacer', 'friem', 'scalpel']
    all_models = {}
    for obj_name in object_names:
        obj_path = os.path.join(obj_root, f'{obj_name}.stl')
        mesh = trimesh.load(obj_path)
        all_models[obj_name] = np.array(mesh.vertices)
    return all_models