# import theater_module
# theater_module.price(3) # 3 명
# theater_module.price_morning(4) # 4명 조조할인
# theater_module.price_soldier(5) # 5명 군인할인

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as price
# price(3)

from theater_module import price_soldier as ps
ps(3)