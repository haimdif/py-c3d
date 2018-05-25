







import c3d
import numpy as np
import json
import argparse 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='convert .json to .c3d')
    parser.add_argument('points_file',   help='the json file')
    parser.add_argument('output_c3d',    help='the ouput c3d file')

    args = parser.parse_args()

    with open(args.points_file,'r') as handle:
        points_from_all_frames = json.load(handle)
        
    writer = c3d.Writer(point_labels = points_from_all_frames['label_names'])
    
    analog = np.array([])

    for frame in points_from_all_frames['Frames']:
        points_list = []
        for label in points_from_all_frames['label_names']:
            points_list.append(frame[label])
            
        points = np.array(points_list)
        writer.add_frames([(points,analog)])

    with open(args.output_c3d, 'wb') as handle:
        writer.write(handle)    






#import c3d
#import numpy as np

# with open('sample_throw.c3d', 'rb') as handle:
    # reader = c3d.Reader(handle)
    # for frame_no, points, analog in reader.read_frames(copy=False):
        # print points
        # print type(analog)
        # exit()


# writer = c3d.Writer()
# points = np.array([
# [1,2,3,0,0],
# [4,5,6,0,0],
# ])
# analog = np.array([[1,1],[1,1]])
# print analog.shape


# writer.add_frames((points,analog))

# with open('fake.c3d', 'wb') as handle:
    # writer.write(handle)    

    
# with open('sample_throw.c3d', 'rb') as handle:
    # reader = c3d.Reader(handle)
    
    # writer = c3d.Writer()

    # for i, points, analog in reader.read_frames():
        # print i
        
     
        # writer.add_frames((points,analog))
        # #print('Frame {}: {}'.format(i, points.round(2)))    
    
# with open('fake.c3d', 'wb') as handle:    
    # writer.write(handle)            
        