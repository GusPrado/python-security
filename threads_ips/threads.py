import time
from threading import Thread

def car(speed, driver):
    path = 0
    while path <= 100:
        path += speed
        time.sleep(0.5)
        print('Piloto: {} Km: {}\n'.format(driver, path))


thread_car1 = Thread(target=car, args=[10, 'Java'])
thread_car2 = Thread(target=car, args=[20, 'Python'])

thread_car1.start()
thread_car2.start()
