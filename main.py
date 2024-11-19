import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 설정
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave', color='blue')

# 그래프 제목 및 레이블 설정
plt.title('사인파 그래프')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.legend()

# 그래프 표시
plt.show()
