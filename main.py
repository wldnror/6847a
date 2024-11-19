import spidev
import time
import matplotlib.pyplot as plt
from collections import deque

# SPI 설정
spi = spidev.SpiDev()
spi.open(0, 0)  # 버스 0, 디바이스 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    if channel < 0 or channel > 7:
        return -1
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

# 데이터 저장을 위한 deque 설정
max_length = 100
data = deque([0]*max_length, maxlen=max_length)

# 그래프 설정
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(0, 100)  # 퍼센트 범위 (0~100%)
ax.set_xlabel('시간')
ax.set_ylabel('퍼센트 (%)')
ax.set_title('공기압 센서 실시간 그래프')

# 현재 퍼센트 값을 표시하기 위한 텍스트
text = ax.text(0.8, 0.9, '', transform=ax.transAxes, fontsize=14)

# 메인 루프
try:
    while True:
        # ADC에서 값 읽기
        adc_value = read_adc(0)
        # 퍼센트로 변환 (0~100%)
        percent = (adc_value / 1023.0) * 100
        data.append(percent)
        
        # 그래프 업데이트
        line.set_ydata(data)
        text.set_text(f'{percent:.2f}%')
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # 콘솔에 값 출력
        print(f"퍼센트: {percent:.2f}%")
        
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    spi.close()
