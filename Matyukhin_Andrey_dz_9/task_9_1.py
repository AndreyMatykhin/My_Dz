import time


class TrafficLight:
    __color = "Red"
    __time_red = 7
    __time_yellow = 2
    time_green = 10

    def color_timer(self, n, col):
        print(f'Traffic light color: {self.__color}', end=" ")
        for i in range(n, 0, -1):
            print(f' {i}', end=(" " if i != 1 else "\n"))
            time.sleep(1)
            self.__color = col

    def running(self, number_of_switches=15):
        while number_of_switches:
            if self.__color == "Red":
                self.color_timer(self.__time_red, "Yellow")
            elif self.__color == "Yellow":
                self.color_timer(self.__time_yellow, "Green")
            elif self.__color == "Green":
                self.color_timer(self.time_green, "Red")
            number_of_switches -= 1
        print("Traffic light stopped")


a = TrafficLight()
a.running()
