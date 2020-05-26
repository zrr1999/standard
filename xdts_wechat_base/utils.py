import cv2


def predict(img, h, w, net):
    blob = cv2.dnn.blobFromImage(img, 1.0, (w, h),
                                 (103.939, 116.779, 123.680), swapRB=False, crop=False)
    net.setInput(blob)
    out = net.forward()
    out = out.reshape((3, out.shape[2], out.shape[3]))
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.680
    out /= 255.0
    out = out.transpose(1, 2, 0)
    return out


def resize_img(img, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    h, w = img.shape[:2]

    if width is None and height is None:
        return img
    elif width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    elif height is None:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(img, dim, interpolation=inter)
    return resized


def transform(img, width=None, model_n=0):
    model_name = ["la_muse.t7", "composition_vii.t7"]
    net = cv2.dnn.readNetFromTorch(f"models/eccv16/{model_name[model_n]}")
    if width is not None:
        img = resize_img(img, width)
    h, w = img.shape[:2]
    out = predict(img, h, w, net)
    return out
