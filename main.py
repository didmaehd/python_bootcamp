# # #딕셔너리에서 밸류값이 가장 큰 키 찾기
# # dict = {"a":4, "b":6,"c":9,"d":3,"e":7}
# # score = 0
# # winner = "o"
# # for name in dict:
# #     if dict[name] > score :
# #         score = dict[name]
# #         winner =  name
# #         print(name)
# # print(winner, score)



# dict={"a":"A","b":6,"c":9,"d":3,"e":7}
# # print (dict["a"])

# # import random
# # result = random.randrange(1,11)
# # print(result)

# # a = "global"
# # def tykim():
# #     a = "local"
# #     print(a)

# # tykim()
# # print(a)


# #함수 개념
# #인풋을 받아서 어떤 처리를 거친후에 아웃풋을 만들어야 하는 경우
# #나온 결과를 재활용 할 경우

# #인풋을 받아서 

# # def testa (a):
# #     return a + 100


# # def testb (b):
# #     return testa(100) + b

# # result = testb(100)
# # print(result) 

# import random
# dic = [
#     {
#     "이름":"진", 
#     "팔로어": 234,
#     },
#     {
#     "이름":"뷔", 
#     "팔로어 ": 342,
#     }
#        ]

# a = random.choice(dic)
# print(a["이름"])
# print(a["팔로어"])


dic = {"asa": 1, "b": 2}
print(dic["asa"])
