import cv2
import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoFileClip

PLOT_FLAG = False

def pre_process(img, blur_ksize=5, canny_low=50, canny_high=100):
    """
    (1) 图像预处理：灰度-高斯模糊-Canny边缘检测
    @param img: 原RGB图像
    @param blur_ksize: 高斯卷积核
    @param canny_low: canny最低阈值
    @param canny_high: canny最高阈值
    @return: 只含有边缘信息的图像
    """
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 1)
    edges = cv2.Canny(blur, canny_low, canny_high)

    if PLOT_FLAG:
        plt.imshow(edges, cmap='gray'), plt.title("pre process: edges"), plt.show()

    return edges


def roi_extract(img, boundary):
    """
    (2) 感兴趣区域提取
    @param img: 包含边缘信息的图像
    @return: 提取感兴趣区域后的边缘信息图像
    """
    rows, cols = img.shape[:2]
    points = np.array([[(0, rows), (460, boundary), (520, boundary), (cols, rows)]])

    mask = np.zeros_like(img)
    cv2.fillPoly(mask, points, 255)
    if PLOT_FLAG:
        plt.imshow(mask, cmap='gray'), plt.title("roi mask"), plt.show()

    roi = cv2.bitwise_and(img, mask)
    if PLOT_FLAG:
        plt.imshow(roi, cmap='gray'), plt.title("roi"), plt.show()

    return roi


def hough_extract(img, rho=1, theta=np.pi/180, threshold=15, min_line_len=40, max_line_gap=20):
    """
    (3) 霍夫变换
    @param img: 提取感兴趣区域后的边缘信息图像
    @param rho, theta, threshold, min_line_len, max_line_gap: 霍夫变换参数
    @return: 提取的直线信息
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=min_line_len, maxLineGap=max_line_gap)

    if PLOT_FLAG:
        drawing = np.zeros_like(img)
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(drawing, (x1,y1), (x2,y2), 255, 2)
        plt.imshow(drawing, cmap='gray'), plt.title("hough lines"), plt.show()
        print("Total of Hough lines: ", len(lines))

    return lines


def line_fit(lines, boundary, width):
    """
    (4): 通过霍夫变换检测的直线拟合最终的左右车道
    @param lines: 霍夫变换得到的直线
    @param boundary: 裁剪的roi边界（车道下方在图像的边界，尽头是上面roi定义的325）
    @param width: 图像下边界
    @return: 
    """
    # 按照斜率正负划分直线
    left_lines, right_lines = [], []
    for line in lines:
        for x1, y1, x2, y2 in line:
            k = (y2 - y1) / (x2 - x1)
            left_lines.append(line) if k < 0 else right_lines.append(line)

    # 直线过滤
    # left_lines = line_filter(left_lines)
    # right_lines = line_filter(right_lines)
    # print(len(left_lines)+len(right_lines))
    
    # 将所有点汇总
    left_points = [(x1, y1) for line in left_lines for x1, y1, x2, y2 in line] + [(x2, y2) for line in left_lines for
                                                                                  x1, y1, x2, y2 in line]
    right_points = [(x1, y1) for line in right_lines for x1, y1, x2, y2 in line] + [(x2, y2) for line in right_lines for
                                                                                    x1, y1, x2, y2 in line]
    # 最小二乘法拟合这些点为直线
    left_results = least_squares_fit(left_points, boundary, width)
    right_results = least_squares_fit(right_points, boundary, width)
    
    # 最终区域定点的坐标
    vtxs = np.array([[left_results[1], left_results[0], right_results[0], right_results[1]]])
    return vtxs


def line_filter(lines, offset=0.1):
    """
    (4'): 直线过滤
    @param lines: 霍夫变换直接提取的所有直线
    @param offset: 斜率大于此偏移量的直线将被筛出
    @return: 筛出后的直线
    """
    slope = [(y2-y1)/(x2-x1) for line in lines for x1, y1, x2, y2 in line]
    while len(lines) > 0:
        mean = np.mean(slope)
        diff = [abs(s - mean) for s in slope]
        index = np.argmax(diff)
        if diff[index] > offset:
            slope.pop(index)
            lines.pop(index)
        else:
            break
    return lines


def least_squares_fit(points, ymin, ymax):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    fit = np.polyfit(y, x, 1)
    fit_fn = np.poly1d(fit)

    # 我们知道的是车道线的y坐标，通过拟合的函数求出x坐标
    xmin, xmax = int(fit_fn(ymin)), int(fit_fn(ymax))
    return [(xmin, ymin), (xmax, ymax)]


def lane_line_detection(img):
    pre_process_img = pre_process(img)

    roi_img = roi_extract(pre_process_img, boundary=325)

    lines = hough_extract(roi_img)
    
    vtxs = line_fit(lines, 325, img.shape[0])

    cv2.fillPoly(img, vtxs, (0, 255, 0))
    if PLOT_FLAG:
        plt.imshow(img[:, :, ::-1]), plt.title("final output"), plt.show()
    return img


if __name__ == '__main__':
    # img = cv2.imread('../../resources/opencv/lane2.jpg')
    # detected_img = lane_line_detection(img)

    clip = VideoFileClip('../../resources/opencv/lane.mp4')
    out_clip = clip.fl_image(lane_line_detection)
    out_clip.write_videofile('lane-detected.mp4', audio=False)

