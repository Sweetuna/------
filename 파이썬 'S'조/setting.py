import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, TextBox
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import platform

# =========================================================
# 한글 폰트 및 마이너스 기호 설정
# =========================================================
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False


# =========================================================
# 1. 현재 시간 불러오기
# =========================================================

KST = ZoneInfo("Asia/Seoul")
BASE_DATE = datetime(2026, 1, 1, tzinfo=KST)

current_date = datetime.now(KST)
elapsed_days = (current_date - BASE_DATE).total_seconds() / 86400
