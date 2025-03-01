from threading import Thread

thread = Thread(target=print,
                args=['Cats', 'Dogs', 'Frogs'],
                kwargs={'sep': ' & '})
thread.start()
