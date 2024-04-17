import random
import pyautogui
from cnocr import CnOcr
import time

ocr = CnOcr()


def moveDuration():
    return random.uniform(0.2, 0.8)


def moveToMenu():
    menuPos = pyautogui.locateOnScreen("assets/menu.png")
    pyautogui.moveTo(
        menuPos.left + int(random.random() * 15),
        menuPos.top + int(random.random() * 15),
        duration=moveDuration(),
        tween=pyautogui.easeInOutQuad,
    )


def scrollDownVidsList():
    print("scroll down")
    menuPos = pyautogui.locateOnScreen("assets/menu.png")
    pyautogui.moveTo(
        menuPos.left + int(random.random() * 100),
        menuPos.top + 50 + int(random.random() * 250),
        duration=moveDuration(),
        tween=pyautogui.easeInOutQuad,
    )
    pyautogui.scroll(-240 - int(random.random() * 120))
    time.sleep(0.5)


def blankImage(img):
    bytes = img.tobytes()

    white = True
    for byte in bytes:
        if byte != 255:
            white = False
            break

    return white


def ocrVidSecs(vidLenImg) -> tuple[int, str]:
    out = ocr.ocr(vidLenImg)[0].get("text")
    out = "".join(filter(lambda x: x.isdigit(), out))
    if len(out) < 6:
        out = out + "0" * (6 - len(out))

    h = int(out[0:2])
    m = int(out[2:4])
    s = int(out[4:6])

    out = f"{h:02d}:{m:02d}:{s:02d}"

    return h * 3600 + m * 60 + s, out


def closeSingleQuiz():
    closeBox = pyautogui.locateOnScreen("assets/singleQuizClose.png")
    pyautogui.click(
        closeBox.left,
        closeBox.top,
        duration=moveDuration(),
        tween=pyautogui.easeInOutQuad,
    )


def startPlayVideo():
    pyautogui.click(random.randint(300, 900), random.randint(300, 600))


def backHome():
    backBtn = pyautogui.locateOnScreen("assets/backHome.png")
    pyautogui.click(
        backBtn.left + 20,
        backBtn.top + 10,
        duration=moveDuration(),
        tween=pyautogui.easeInOutQuad,
    )
