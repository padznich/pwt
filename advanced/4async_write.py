# coding=utf-8
import threading
import time

class AsyncWrite(threading.Thread):

    def __init__(self, text, out):
        threading.Thread.__init__(self)

        self.text = text
        self.out = out

    def run(self):
        with open(self.out, 'a') as f:
            f.write(self.text + '\n')
        time.sleep(2)
        print("Finished Background File Write to " + self.out)

def main():
    message = input("Enter message: \n")
    background = AsyncWrite(message, "4out.txt")
    background.start()
    print("The program can continue while it writes in another thread.")

    background.join()
    print("Waited until thread was completed")

if __name__ == '__main__':
    main()