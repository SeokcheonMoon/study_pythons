# class 초기화 방법(두가지)
dict_initial = {}           # empty
dict_initial = dict()       # empty

list_car_infor = ["Ford", "Mustang", 1964]

# key(주로 str 형식임) : value(여러 데이터 타입 가능),(끊임없이 집어넣을 수 있음.)
# 데이터를 가져올 경우 이런식으로 가져옴.
dict_carinfor = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "items" : []
}
model = dict_carinfor["model"]
print("dict_carfor 있는 model name: {}".format(model))

# key 에 대한 value를 변경
dict_carinfor['year'] = 1970
#새로운 key와 값 정의
dict_carinfor["color"] = "red"
dict_carinfor["color"] = ["red", "green", "yellow", "blue"]

pass