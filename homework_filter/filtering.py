import cv2
import numpy as np

img = cv2.imread('image.jpg')
H, W, C = img.shape

print("Kich thuoc anh: H =", H, ", W =", W, ", so kenh =", C)
print("Pixel goc tai (0, 0) - dang [B, G, R]:", img[0, 0])
print("  - B (xanh duong):", img[0, 0, 0])
print("  - G (xanh la)   :", img[0, 0, 1])
print("  - R (do)        :", img[0, 0, 2])
print()


def grayscale():
    gray_img = np.zeros((H, W), dtype=np.uint8)
    for y in range(H):
        for x in range(W):
            b = int(img[y, x, 0])
            g = int(img[y, x, 1])
            r = int(img[y, x, 2])
            gray_img[y, x] = (b + g + r) // 3
    return gray_img


def threshold(gray_img, t=100):
    bin_img = np.zeros((H, W), dtype=np.uint8)
    for y in range(H):
        for x in range(W):
            if gray_img[y, x] > t:
                bin_img[y, x] = 255
            else:
                bin_img[y, x] = 0
    return bin_img


def filtering(gray_img):
    out = np.zeros((H, W), dtype=np.uint8)

    for y in range(1, H - 1):
        for x in range(1, W - 1):
            p1 = int(gray_img[y - 1, x - 1])
            p2 = int(gray_img[y - 1, x    ])
            p3 = int(gray_img[y - 1, x + 1])

            p4 = int(gray_img[y    , x - 1])
            p5 = int(gray_img[y    , x    ])
            p6 = int(gray_img[y    , x + 1])

            p7 = int(gray_img[y + 1, x - 1])
            p8 = int(gray_img[y + 1, x    ])
            p9 = int(gray_img[y + 1, x + 1])

            tong = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
            out[y, x] = tong // 9

    return out


def show():
    gray_img = grayscale()
    print("Pixel xam tai (0, 0):", gray_img[0, 0])
    print("Pixel xam tai (10, 10):", gray_img[10, 10])
    print("\nGoc tren trai cua anh xam (5x5):")
    print(gray_img[:5, :5])

    thres_img = threshold(gray_img, t=100)
    print("\nPixel nhi phan tai (0, 0):", thres_img[0, 0])
    print("Goc tren trai cua anh nhi phan (5x5):")
    print(thres_img[:5, :5])

    filt_img = filtering(gray_img)
    print("\nPixel sau loc tai (10, 10):", filt_img[10, 10])
    print("Goc tren trai cua anh sau loc (5x5):")
    print(filt_img[:5, :5])

    cv2.imshow("original", img)
    cv2.imshow("gray (manual)", gray_img)
    cv2.imshow("threshold t=100 (manual)", thres_img)
    cv2.imshow("3x3 average filter (manual)", filt_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


show()
