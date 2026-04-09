print("로또 추첨을 시작합니다")

import random

lotto = random.sample(range(1,46),6)

lotto.sort()

print("추첨된 로또 번호", *lotto)