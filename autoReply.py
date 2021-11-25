import pyautogui
import pyperclip
import time
import random

# this task list is designed for wechat pc version
taskList = [
    { "action": "单击图片", "content": "red.png" },
    { "action": "输入文字", "content": [ "宝 我在输液 想你的夜", "天青色等烟雨，而我在等你", "哼 妹妹 这都拿不下你吗"] },
    { "action": "单击图片", "content": "send.png" },
    { "action": "切换至另外聊天框", "content": "other.png" }
]

def mouseClick(img):
    location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
    if location is not None:
        pyautogui.click(location.x,location.y,clicks=1,interval=0.2,duration=0.2,button="left")
        return True
    else:
        return False

def handleTask(task):
    if task["action"] == "单击图片":
        img = task["content"]
        return mouseClick(img)
    elif task["action"] == "输入文字":
        # use default sentences if the file is empty
        contentArr = task["content"]
        try:
            textFile = open("input.txt", "r", encoding='UTF-8')
        except:
            print("An error happens when reading input.txt")
        if (textFile != None) & (len(textFile.readlines()) > 0):
            contentArr = textFile.readlines()
        randomIndex = random.randint(0, len(contentArr) - 1)
        text = contentArr[randomIndex]
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'V')
        return True
    elif task["action"] == "切换至另外聊天框":
        img = task['content']
        return mouseClick(img)

while True:
    i = 0
    # proceed task on the list
    while i < len(taskList):
        if(handleTask(taskList[i])):
            i += 1
        else:
            # logging message while listening
            print("等待消息中。。。", time.ctime())