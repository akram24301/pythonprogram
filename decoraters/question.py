import time
def timer(func):
    def inner():
        start = time.time()
        func()
        end= time.time()
        print(f'Time taken to answer question:- {end-start} secs ')

    return inner

@timer
def question1():
    print('who is the prime minister of India :- ')
    response = input('enter your response :- ')

@timer
def question2():
    print('who is the  chief minister of Andra pradesh :- ')
    response = input('enter your response :- ')

question1()
question2()