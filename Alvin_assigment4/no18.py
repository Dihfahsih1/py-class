# when using lists in a Queue, we use the append and the pop methods

def que():
    # initialize a Queue
    my_queue = []
    # Add elements to the queue
    my_queue.append('a')
    my_queue.append('b')
    my_queue.append('c')
    my_queue.append('d')
    print (my_queue)

    # Removing elements using FIFO
    print(my_queue.pop(0))
    print(my_queue.pop(0))
    print(my_queue.pop(0))
    print(my_queue.pop(0))
    
    # Removing elements using LIFO
    # print(my_queue.pop())
    # print(my_queue.pop())
    # print(my_queue.pop())
    # print(my_queue.pop())
que()