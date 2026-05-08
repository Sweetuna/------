#버스 줄 서기
bus_line = ['김수뭉', '이사슴', '박밀레']
bus_line.append('최자하')
print(bus_line)

#버스 좌석 만들기
bus_seat = ['구백년', '서교수']
print(bus_seat)

#버스 뒷자리부터 채워 앉기
print(f"{bus_line[0]} 탑승합니다.")
bus_seat.append(bus_line.pop(0))
print(bus_seat)

print(f"{bus_line[0]} 탑승합니다.")
bus_seat.append(bus_line.pop(0))
print(bus_seat)

print(f"{bus_line[0]} 탑승합니다.")
bus_seat.append(bus_line.pop(0))
print(bus_seat)

print(f"{bus_line[0]} 탑승합니다.")
bus_seat.append(bus_line.pop(0))
print(bus_seat)

#버스 앞자리부터 3명 내리기
print(f"{bus_seat[0]} 하차합니다.")
bus_seat.pop(0)
print(bus_seat)

print(f"{bus_seat[0]} 하차합니다.")
bus_seat.pop(0)
print(bus_seat)

print(f"{bus_seat[0]} 하차합니다.")
bus_seat.pop(0)
print(bus_seat)

print("세 명 하차 완료했습니다.")