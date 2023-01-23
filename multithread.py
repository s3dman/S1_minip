import threading

def run_parallel(func,*args):
    x = threading.Thread(target=func,args=args)
    x.start()

