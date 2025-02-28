# def san(a,b,c):
#     if a+b>c and a+c>b and c+b>a:
#         print("是")
#     else:
#         print("不是")
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# print(san(a,b,c))
#
# a=float(input("输入学生成绩:"))
# if a<60:
#     print("不及格")
# elif a<70:
#     print("及格")
# elif a<80:
#     print("中")
# elif a<90:
#     print("良")
# else:
#     print("优")
#
# for a in range(2,101,1):
#     for i in range(2, a):
#         if a % i == 0:
#             break
#     else:
#         print(a)
#
# s=1
# print(type(s))
#
# import random
#
# # Define a list of responses
# responses = [
#     "Hello!",
#     "How can I help you today?",
#     "What's on your mind?",
#     "I'm here to assist you.",
#     "Ask me anything!"
# ]
#
# # Define a function to generate a response
# def get_response():
#     return random.choice(responses)
#
# # Main loop to interact with the chatbot
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
#     else:
#         print("AI: " + get_response())
def  showNnumber(numbers):
    for n in numbers:
        print(n)
numbers=(12,4,5)
print(showNnumber(numbers))