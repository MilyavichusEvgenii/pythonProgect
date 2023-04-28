from core.controller import controller
import threading
controller.start()
thread_meth = threading.Thread(target=controller.start())

# if __name__ == '__main__':
#     print_hi('PyCharm')


