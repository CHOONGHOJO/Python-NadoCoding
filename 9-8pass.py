# 다중상속 : 2이상의 부모에게서 상속 받음

# 일반 유닛
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방량으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
  def __init__(self, name, hp, speed, damage):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

  def damaged(self, damage):
    print("{0} : {1} damage를 입었습니다".format(self.name, damage))
    self.hp -= damage
    print("{0} : 현재 체력은  {1} 입니다".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다.".format(self.name))

# drop ship: 공중유닛, 수송기, 마린/파이어벳/텡크등을 수송 공격x

# 날 수 있는 기능을 가진 클라스
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 틀라스
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0
    Flyable.__init__(self, flying_speed)

  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

#건물
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    pass

# 서플라이 디포: 건물, 1개 건물 = 8 유닛
sullpy_depot = BuildingUnit("서플라이 디포", 500, "7시")
