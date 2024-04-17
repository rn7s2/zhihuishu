import datetime
import time
import pyautogui
import util

util.moveToMenu()

watchedSecs = 0
while watchedSecs < 28 * 60:
    selected = False

    lst = list(pyautogui.locateAllOnScreen("assets/vidBtn.png"))
    for pos in lst:
        doneIcon = pyautogui.screenshot(
            region=(int(pos.left + 275), int(pos.top - 18), 28, 28)
        )
        if not util.blankImage(doneIcon):
            continue

        selected = True

        vidLenImg = pyautogui.screenshot(
            region=(int(pos.left + 20), int(pos.top), 75, 20)
        )
        vidSecs, vidLen = util.ocrVidSecs(vidLenImg)
        print(f"selected video, len={vidLen}, secs={vidSecs}")

        pyautogui.click(
            pos.left + 20,
            pos.top,
            duration=util.moveDuration(),
            tween=pyautogui.easeInOutQuad,
        )
        time.sleep(3)
        util.startPlayVideo()

        finishTime = datetime.datetime.now() + datetime.timedelta(seconds=vidSecs + 60)
        print(f"start watching video, will finish at {finishTime}")

        while datetime.datetime.now() < finishTime:
            try:
                if pyautogui.locateOnScreen("assets/singleQuiz.png") != None:
                    print("quiz (single)")
                    btns = list(pyautogui.locateAllOnScreen("assets/singleQuizBtn.png"))
                    for btn in btns:
                        pyautogui.click(
                            btn.left + 10,
                            btn.top + 5,
                            duration=util.moveDuration(),
                            tween=pyautogui.easeInOutQuad,
                        )
                        time.sleep(0.2)

                        try:
                            if (
                                pyautogui.locateOnScreen("assets/singleQuizPass.png")
                                != None
                            ):
                                print("quiz pass, close")
                                util.closeSingleQuiz()
                                time.sleep(0.5)
                                util.startPlayVideo()

                                break
                        except:
                            print("wrong answer")
                            time.sleep(0.2)
                            continue
            except:
                pass

            # else if

            time.sleep(3)

        watchedSecs += vidSecs
        break

    if not selected:
        util.scrollDownVidsList()
