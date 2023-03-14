import pyautogui
import time


# 使用时需要将页面放大到110%
# 并且进入到最近登陆页面即可运行
#   普通点击
def click(img, t, text, l=0):
    left, top, width, height = pyautogui.locateOnScreen(f'./img/{img}.png', grayscale=False, confidence=0.65)
    center = pyautogui.center((left + l, top, width, height))  # 寻找 图片的中心
    pyautogui.click(center)  # 点击
    time.sleep(t)
    print(text)


def zsrwclick(img, t, text):
    # 进入钻石任务列表
    left, top, width, height = pyautogui.locateOnScreen(f'./img/zsrw.png', grayscale=False, confidence=0.5)
    center = pyautogui.center((left, top, width, height))  # 寻找 图片的中心
    pyautogui.click(center)  # 点击
    time.sleep(3)
    left, top, width, height = pyautogui.locateOnScreen(f'./img/{img}.png', grayscale=False, confidence=0.9)
    center = pyautogui.center((left + 180, top, width, height))  # 寻找 图片的中心
    pyautogui.click(center)  # 点击
    time.sleep(t)
    print(text)


def denglu():
    click('zhdl', 2, '账号登陆')
    click('ksksyx', 15, '快速开始游戏')


def xx():
    try:
        click('xx', 4, 'xx1')
        click('xx', 4, 'xx1')
        click('xx2', 4, 'xx2')
        click('xx3', 4, 'xx3')
    except:
        pass
    finally:
        print('已×完！')
    pass


def lm():
    click('lm', 2, '联盟')
    click('jrlmly', 2, '进入联盟领域')
    try:
        click('lmbd', 4, '联盟报道')
        click('tbl', 3, '太棒了')
        click('xx4', 3, 'xx4')
    except:
        pass
    click('lmjlb', 3, '俱乐部')
    click('jxgz', 3, '吉星高照')
    try:
        click('yj', 5, '摇吉')
        click('zdl', 2, '知道了')
    finally:
        try:
            while True:
                click('jsyj', 5, '继续摇吉')
                click('zdl', 2, '知道了')
        except:
            pass
        finally:
            click('xx5', 2, 'xx5')
            click('xx5', 2, 'xx5')
            click('tclm', 3, '退出联盟')

    pass


# 在线奖励
def zxjl():
    zsrwclick('zxjl', 3, '在线奖励')
    click('zxjl2', 2, '金币')
    click('zdl', 2, '知道了')
    click('xx2', 2, 'xx2')
    pass


# 采摘缤纷树
def czbfs():
    click('cjbfs', 2, '采摘缤纷树')
    click('jxcz', 2, '继续采摘')
    click('zdl', 2, '知道了')
    click('kscz', 2, '开始采摘')
    pass


# 资源秘境
def zrmj():
    # zsrwclick('zymj', 3, '资源秘境')
    click('jrmj', 2, '进入秘境')
    try:
        count = 0
        while True:
            try:
                click('bx2', 2, '补血2')
                if pyautogui.locateOnScreen(f'./img/qd4.png', grayscale=False, confidence=0.5):
                    click('qd4', 2, '确定2')
                click('kstz2', 10, '开始挑战2')
                click('tg1', 5, '跳过', 55)
                click('qd1', 5, '确定1')
                click('wzdl', 2, '我知道了')
            except:
                pass
            finally:
                count += 1
                if count > 8:
                    break
    except:
        pass
    finally:
        print('挑战完成!')

    pass


# 参与航海
def cyhh():
    zsrwclick('cyhh', 5, '参与航海')
    click('wzdl2', 3, '我知道了2')
    click('zdl', 3, '知道了')
    click('chdb', 3, '出海夺宝')
    click('xz', 3, '选择')
    click('ljwc', 3, '立即完成')
    click('qd3', 3, '确定3')
    click('tc', 3, '退出航海')
    pass


# 每日签到
def mrqd():
    zsrwclick('mrqd', 2, '每日签到')
    click('mrqd2', 3, '每日签到')
    click('zdl', 2, '知道了')
    click('xx6', 2, 'xx6')
    pass


# 佣兵奖励
def ybjl():
    zsrwclick('ybjl', 2, '佣兵奖励')
    click('kspq', 2, '开始派遣')
    click('lqjl', 2, '领取奖励')
    click('zdl', 2, '知道了')
    click('pqjl', 2, '派遣精灵')
    click('kspq2', 3, '快速派遣')
    click('ksrw', 2, '开始任务')
    click('xx7', 2, 'xx7')
    click('xx8', 2, 'xx8')


# 钻石任务
def zsrw():
    zxjl()  # 15
    czbfs()  # 20
    zrmj()  # 30
    ybjl()  # 10
    mrqd()  # 10
    cyhh()  # 10


def tz():
    try:

        while True:
            click('kstz1', 10, '开始挑战')
            click('tg1', 2, '跳过', 55)
            click('qd1', 5, '确定1')
            click('tbl2', 2, '太棒了2')
            click('qd2', 2, '确定2')
            click('bx1', 2, '补血')
            try:
                click('qd4', 2, '确定1')
            except:
                pass
    except:
        pass


def libao():
    click('zsrw', 3, '钻石任务')
    click('baox1', 3, '1')
    click('zdl', 2, 'tbl')
    click('baox2', 3, '2')
    click('zdl', 2, 'tbl')
    click('baox3', 3, '3')
    click('zdl', 2, 'tbl')
    click('baox4', 3, '4')
    click('zdl', 2, 'tbl')
    click('baox5', 3, '5')
    click('zdl', 2, 'tbl')


count = 0
while True:
    if pyautogui.locateOnScreen('./img/kstz1.png', grayscale=False, confidence=0.5):
        denglu()  # 登陆
        xx()    # xx
        # lm()    # 联盟摇吉    10    如果加入了联盟就可以不注释
        # tz()
        zsrw()  # 钻石任务
        libao() # 领取礼包

        break
    else:
        count += 1
        print(f'继续查找中!{count}')
