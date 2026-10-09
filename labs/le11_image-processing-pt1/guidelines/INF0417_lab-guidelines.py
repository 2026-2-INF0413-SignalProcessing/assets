def test_addition():
    a = 10
    b = 15

    c = 25

    assert a + b == c

def project_point_in_image(point, camera_matrix):
    image_point = camera_matrix @ point

    return image_point

def project_camera_position():
    # Project a point that is at the same position as the camera into the image
    pass

def project_behind_camera():
    # Project a point that is behind the camera into the image
    pass

def project_point():
    # Project a sensible point that is in front of the camera into the image
    pass
