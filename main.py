import math
import random
import warnings
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# 🔴 彻底屏蔽PNG颜色配置文件警告）
warnings.filterwarnings("ignore", category=UserWarning, module="cv2")
warnings.filterwarnings("ignore", category=RuntimeWarning, module="libpng")

# 初始化摄像头
cap = cv2.VideoCapture(0)  # 0为默认摄像头
cap.set(3, 1280)  # 宽度
cap.set(4, 720)  # 高度

# 初始化手部检测器
detector = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGameClass:
    def __init__(self, pathfood):
        self.points = []  # 蛇身上所有的点
        self.lengths = []  # 每个点之间的长度
        self.currentLength = 0  # 蛇的总长
        self.allowedLength = 150  # 蛇允许的总长度
        self.previousHead = (0, 0)  # 上一个头结点（元组初始化）

        # 🔴 修复：删除无效的颜色转换，用正确方式处理PNG警告
        self.imgFood = cv2.imread(pathfood, cv2.IMREAD_UNCHANGED)
        if self.imgFood is None:
            raise FileNotFoundError(f"❌ 无法找到食物图片: {pathfood}，请确保文件在当前目录")
        # 正确处理：直接复制图像，剔除iCCP配置文件，彻底解决libpng警告
        self.imgFood = self.imgFood.copy()
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = (0, 0)
        self.randomFoodLocation()  # 统一方法名，和调用一致

        self.score = 0
        self.gameOver = False

    # 🔴 修复方法名：和__init__调用完全一致
    def randomFoodLocation(self):
        # 随机生成食物位置（适配1280x720分辨率，避免超出画面）
        self.foodPoint = (
            random.randint(100, 1180),
            random.randint(100, 620)
        )

    def update(self, imgmain, currenthead):
        if self.gameOver:
            # 游戏结束显示
            cvzone.putTextRect(imgmain, "Game Over", [300, 400],
                               scale=7, thickness=5, offset=20)
            cvzone.putTextRect(imgmain, f'Your Score:{self.score}', [300, 550],
                               scale=7, thickness=5, offset=20)
        else:
            px, py = self.previousHead
            cx, cy = currenthead  # 使用传入的食指指尖坐标

            # 添加新的蛇头点
            self.points.append([cx, cy])
            # 计算与上一个点的距离
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = (cx, cy)  # 更新上一个头结点

            # 长度收缩：超过允许长度时移除尾部
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

            # 检查是否吃到食物
            rx, ry = self.foodPoint
            if (rx - self.wFood // 2 < cx < rx + self.wFood // 2 and
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2):
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                print(f"✅ 当前分数: {self.score}")

            # 绘制蛇身
            if self.points:
                for i in range(1, len(self.points)):
                    pt1 = tuple(map(int, self.points[i - 1]))
                    pt2 = tuple(map(int, self.points[i]))
                    cv2.line(imgmain, pt1, pt2, (0, 0, 255), 20)
                # 绘制蛇头（紫色）
                head_pt = tuple(map(int, self.points[-1]))
                cv2.circle(imgmain, head_pt, 20, (200, 0, 200), cv2.FILLED)

            # 绘制食物
            rx, ry = self.foodPoint
            imgmain = cvzone.overlayPNG(
                imgmain,
                self.imgFood,
                (rx - self.wFood // 2, ry - self.hFood // 2)
            )

            # 显示分数
            cvzone.putTextRect(imgmain, f'Score:{self.score}', [50, 80],
                               scale=3, thickness=5, offset=10)

            # 检查碰撞（蛇头碰到身体）
            if len(self.points) > 5:  # 点数足够时才检测碰撞
                pts = np.array(self.points[:-2], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(imgmain, [pts], False, (0, 200, 0), 3)
                mindist = cv2.pointPolygonTest(pts, (cx, cy), True)

                if -1 <= mindist <= 1:
                    print("💥 碰撞！游戏结束")
                    self.gameOver = True

        return imgmain


# 初始化游戏（确保donut.png在当前目录）
try:
    game = SnakeGameClass("donut.png")
except FileNotFoundError as e:
    print(f"❌ 错误: {e}")
    print("请确保donut.png文件和main.py在同一个文件夹下")
    exit(1)

# 主循环
try:
    while True:
        success, img = cap.read()
        if not success:
            print("❌ 无法读取摄像头画面，请检查摄像头是否被占用")
            break

        img = cv2.flip(img, 1)  # 水平翻转画面（镜像，符合操作习惯）
        hands, img = detector.findHands(img, flipType=False)  # 检测手部

        if hands:
            lmList = hands[0]['lmList']
            pointIndex = tuple(map(int, lmList[8][0:2]))  # 食指指尖坐标（转为整数）
            img = game.update(img, pointIndex)

        # 显示画面
        cv2.imshow("Snake Game", img)

        key = cv2.waitKey(1) & 0xFF
        if key in (ord('q'), 27):
            print("👋 退出游戏")
            break
        if cv2.getWindowProperty("Snake Game", cv2.WND_PROP_VISIBLE) < 1:
            print("👋 游戏窗口已关闭")
            break
        if key == ord('r'):
            # 重置游戏所有状态
            game.gameOver = False
            game.points = []
            game.lengths = []
            game.currentLength = 0
            game.allowedLength = 150
            game.previousHead = (0, 0)
            game.score = 0
            game.randomFoodLocation()  # 重置食物位置
            print("🔄 游戏已重置！")
finally:
    # 无论如何退出循环，都释放摄像头并关闭窗口
    cap.release()
    cv2.destroyAllWindows()