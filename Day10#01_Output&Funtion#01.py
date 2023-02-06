
#스페이스로 스플릿해서 슬라이싱으로 첫번째 문자만 대문자로 변환
a = "ty kim"
b = (a.split(" "))
c = b[0][0].upper() + b[0][1:]
d = b[1][0].upper() + b[1][1:]
print(c,d)


#title 함수를 사용하여 첫번째 글자를 대문자로 변환
x = "life is so funny"
print (x.title())


#입력 받은 이름을 성과 이름으루 구분해서 출력하기, 첫번째 글자는 대문자
# def format_name(fullname):
#     list_name = fullname.split(" ")
#     print(list_name)
#     f_name = list_name[0][0].upper() + list_name[0][1:]
#     l_name = list_name[1][0].upper() + list_name[1][1:]
#     return f_name, l_name
# print (format_name("james bond"))

def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't privide vaild inputs."
    elif f_name is not str or l_name != str :
        return "You didn't privide vaild inputs.\nPlease input your name."
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Result : {f_name} {l_name}"

print (format_name(input("What is your first name? : "),input("What is your last name? : ")))


