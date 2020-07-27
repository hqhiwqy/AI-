import time
# 类方法


class Clock:
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """构造方法"""
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        """当前时间"""
        ctime = time.localtime()
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)


if __name__ == "__main__":

    clock = Clock().now()

    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()

    # ctime = time.localtime()
    #
    # print(ctime)
    # print(ctime.tm_hour)