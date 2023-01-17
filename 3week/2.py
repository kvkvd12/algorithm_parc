# def solution(phone_number):
#     secret_phone = []
#     for i in range(len(phone_number)-4):
#         phone_number[i] = "*"

#     return phone_number

# print(solution("01033334444"))


# def solution(phone_number):
#     for phone in phone_number:
#         phone = 1
#         print(phone)

#     return phone_number

# print(solution("01033334444"))


def solution(phone_number):
    secret_phone = []
    for i in range(len(phone_number)-4):
        secret_phone.append("*")
    for i in range(len(phone_number)-4, len(phone_number)):
        secret_phone.append(phone_number[i])

    return ''.join(secret_phone)

print(solution("01033334444"))