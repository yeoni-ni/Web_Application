
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작!')
#         func(input_text)
#         print('함수 끝!')
#     return decorated
#
# @ decorator
# def hello_world(input_text):
#     print(input_text)
#
# hello_world('hello_world!')
#

# # Q1. 높이, 너비
def decorator(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
        return decorated

@ decorator
def triangle(width, height):
    return (width * height)/2

answer = triangle(20, 10)
print(answer)

## Q2.user 클래스 사용
class user():
    def __init__(self,auth):
        self.is_authenticated = auth

user = User(auth = False)
answer = triangle(user,20, 10)
print(answer)
