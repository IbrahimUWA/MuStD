import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pyntcloud import PyntCloud
from plyfile import PlyData, PlyElement
from mayavi import mlab

import numpy as np
import open3d as o3d
import os

# Specify the path to your .bin file
r_file_path = "/home/ibrahim/Documents/Visualize-KITTI-Objects-in-Videos-main/data/KITTI/velodyne/0001/"
w_file_path = "/home/ibrahim/Documents/Visualize-KITTI-Objects-in-Videos-main/data/KITTI/velodyne/"
files = os.listdir(r_file_path)
print(files)
count1 = 000000
numb = 00000-1
for file in files:
    print(file)
    data_format = np.float32  # Adjust the data type as needed
    num_dimensions = 4  # Assuming XYZ format
    rfile = r_file_path + file
    # Read binary data from the file
    with open(rfile, "rb") as f:
        # Read all the binary data
        binary_data = f.read()

    # Convert binary data to NumPy array
    points = np.frombuffer(binary_data, dtype=data_format)

    numpy_array = np.array(points)

    numpy_array = numpy_array.reshape(-1, num_dimensions)


    points =numpy_array[:,0:3]
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    new_file = file.replace(".bin", ".ply")
    filew = w_file_path + new_file
    o3d.io.write_point_cloud(filew, point_cloud)

