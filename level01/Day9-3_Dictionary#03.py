#Nesting 


capital = {
    "Frace" : "Paris",
    "Germany" : "Berlin"
}


#Nesting a list in a dictionary
travel_log = {
    "Korea" : ["Seoul","Busan","Inchon"],
    "Japan" : ["Tokyo","Osaka","Nagoya"],
}

#Nesting dictionary in a dictionary

travel_log = {
    "Korea" : [
        {"Seoul":{"Sindang":4,"Gangnam":3}},
        {"Busan":{"Nampo":4,"Seomyun":3}},
        {"Inchon":{"Airport":3}}
        ],
    # "Japan" : {"cities_visited" : ["Tokyo","Osaka","Nagoya"], "Total_visit": 32},
    "Japan" : {
        "Seoul":{"Sindang":4,"Gangnam":3},
        "Busan":{"Nampo":4,"Seomyun":3},
        "Inchon":{"Airport":3}
        },
    # "korea" : {"seoul" : {"a":1,"b":2},"busan": {"n" : 3, "s":3}}
}


english_dictionary = {}
english_dictionary["a"] = {"apple":"사과", "application":"응용프로그램"}
english_dictionary["a"]["anything"] = "어떤것도" 
print(english_dictionary)

dic= {1:"a"}
dic[2] = "b" # 딕셔너리 키 밸류 추가
dic[3] = [1,2,3] # 딕셔너리 밸류를 리스트로 추가
dic[3].append(4) # 리스트 밸루에 값 추가
dic[4] = {"u" : "you"} # 딕셔너리 밸류를 딕셔너리로 추가
dic[4]["s"] = "S" # 딕셔너리 밸류내 키 밸류 추가
print(dic)
