def translate(landmark_xcors, landmark_ycors, landmark_zcors, handedness):

    def right_condition_for_a():
        if not (landmark_ycors[6] > landmark_ycors[7] > landmark_ycors[8]):
            return False
        if not landmark_ycors[10] > landmark_ycors[11] > landmark_ycors[12]:
            return False
        if not landmark_ycors[14] > landmark_ycors[15] > landmark_ycors[16]:
            return False
        if not landmark_ycors[18] > landmark_ycors[19]:
            return False
        if max(landmark_xcors[1:5]) - min(landmark_xcors[1:5]) > abs(landmark_xcors[2] - landmark_xcors[9]):
            return False
        # if landmark_zcors[6] >
        return True


    #Note: On a forward facing camera, handedness has to be switched. Thus, what is called "Left" is actually "Right"
    if handedness == "Left":
        if right_condition_for_a():
            print("A")


