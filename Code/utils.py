import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def parse_pose_from_TF(input, output):
    # Read the text file
    with open(input, 'r') as file:
        content = file.read()
    
    # Define regular expressions for pattern matching
    time_regex = r"At time (\d+\.\d+)"
    translation_regex = r"\[([\d\.\-]+), ([\d\.\-]+), ([\d\.\-]+)\]"
    rpy_regex = r"in RPY \(radian\) \[([\d\.\-]+), ([\d\.\-]+), ([\d\.\-]+)\]"
    
    # Initialize lists to store extracted data
    time_list = []
    x_list = []
    y_list = []
    z_list = []
    roll_list = []
    pitch_list = []
    yaw_list = []
    
    # Find matches and extract data using regular expressions
    matches = re.findall(time_regex + r".*?" + translation_regex + r".*?" + rpy_regex, content, re.DOTALL)
    for match in matches:
        time_list.append(float(match[0]))
        x_list.append(float(match[1]))
        y_list.append(float(match[2]))
        z_list.append(float(match[3]))
        roll_list.append(float(match[4]))
        pitch_list.append(float(match[5]))
        yaw_list.append(float(match[6]))
    
    # Create a pandas DataFrame
    data = {
        'Time': time_list,
        'X': x_list,
        'Y': y_list,
        'Z': z_list,
        'Roll': roll_list,
        'Pitch': pitch_list,
        'Yaw': yaw_list
    }
    df = pd.DataFrame(data)

    
    # Save the DataFrame to a new text file
    df.to_csv(output, sep=',', header=True, index=False)


