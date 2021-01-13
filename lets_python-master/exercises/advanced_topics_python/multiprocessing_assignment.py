from multiprocessing import Process, Lock,Pool
lock = Lock()

def sqr(item):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print(item*item)
        return item*item
    finally:
        lock.release()


 
if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    pool = Pool(processes=2)
    print(pool.map(sqr, numbers))

    

        