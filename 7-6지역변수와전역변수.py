gun = 10

# def checkpoint(soldiers):
#   # gun = 20 # 지역변수
#   global gun # 전역변수
#   gun = gun - soldiers
#   print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
