import  string

class  Clock(object):
    def __init__(self, hours : int, minutes : int, seconds : int, alarm_h=0, alarm_m=0, alarm_s = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        self.__alarm_h = alarm_h
        self.__alarm_m = alarm_m
        self.__alarm_s = alarm_s

    # method checks to see if users input fits the time format ( h, m ,s)
    def check_time(self, time: string) -> bool:
        try:
            hours, minutes, seconds = time.split(":")
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)

            if  hours > 24 or hours < 0 or minutes > 59 or minutes < 0 or seconds > 59 or seconds < 0:
                return False
            return True
        except:
            return False


    def change_time(self, time: string) -> None:
        if self.check_time(time):
            hours, minutes, seconds = [int(n) for n in time.split(':')]
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
        else:
            print('wrong argument format!\n')

    def __str__(self):
        clck_str = '{} hours, {} minutes, {} seconds.'.format(self.__hours, self.__minutes, self.__seconds)
        return clck_str


    def add_time(self, time: string) -> None:
        # calls method to see if the input fits the format first
        if not self.check_time(time):
            print('wrong argument format!\n')
            return

        hours, minutes, seconds = [int(n) for n in time.split(':')]

        # the following calculations add the times being passed to the current time stored
        carry_minutes, seconds = divmod((self.__seconds + seconds), 60)
        carry_hours, minutes = divmod((self.__minutes + minutes), 60)
        carry_days, hours = divmod((self.__hours + hours), 24)

        self.___hours = hours + carry_hours
        self.___minutes = minutes + carry_minutes
        self.___seconds = seconds

        self.__str__()


    def set_alarm(self, time : string) -> None:
        # check if parameter fits format
        if not self.check_time(time):
            print('wrong argument format\n')
            return

        hours, minutes, seconds = [int(n) for n in time.split(':')]
        self.__alarm_h = hours
        self.__alarm_m = minutes
        self.__alarm_s = seconds


    def print_alarm(self):
        alarm_clck = '{} hours, {} minutes, {} seconds'.format(self.__alarm_h, self.__alarm_m, self.__alarm_s)
        print(alarm_clck)


    def ring_alarm(self, current_time : string) -> None:
        # prints a song if  the current time is the alarm time
        if not self.check_time(current_time):
            print('wrong argument format\n')
            return

        hours, minutes, seconds = [int(n) for n in current_time.split(':')]

        # checks if the current times is the same as the alarm time
        if hours == self.__hours and minutes == self.__minutes and seconds == self.__minutes:
            print("🎸🤘🎼🎵♬🎸🤘🎼🎵♬🎸🤘🎼🎵♬")
        else:
            print('it isnt time to ring the alarm')


clock_1 = Clock(5, 28, 12)
print(clock_1) # 5 hours, 28 minutes, 12 seconds
clock_1.add_time("00:10:00")# 5 hours, 38 minutes, 12 seconds
print(clock_1)
clock_1.add_time("00:20:00")
print(clock_1) # 5 hours, 58 minutes and 12 seconds

clock_1.set_alarm("05:00:14") # Alarm: 3 hours, 0 minutes and 14 seconds
clock_1.ring_alarm("05:00:14") # 🎸🤘🎼🎵♬🎸🤘🎼🎵♬🎸🤘🎼🎵♬
clock_1.ring_alarm("05:45:14") # It is not time to ring the alarm yet





