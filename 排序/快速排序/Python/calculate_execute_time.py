import time

def d_calculate_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        print(f"函数{func.__name__}的执行时间为:{execute_time}秒")
        return result
    return wrapper