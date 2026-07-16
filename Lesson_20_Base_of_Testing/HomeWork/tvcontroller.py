CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels:list):
        self.channels = channels
        self.current_index = 0


    def first_channel(self):
        self.current_index = 0
        return self.channels[0]


    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]


    def turn_channel(self, number:int):
        self.current_index = number - 1
        return self.channels[self.current_index]

    def next_channel(self):
        if self.current_index == len(self.channels) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        return self.channels[self.current_index]


    def previous_channel(self):
        if self.current_index == 0:
            self.current_index = len(self.channels) - 1
        else:
            self.current_index -= 1
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]


    def exists(self, value):
        if isinstance(value, int):
            if 1 <= value <= len(self.channels):
                return "Yes"
            return "No"

        elif isinstance(value, str):
            if value in self.channels:
                return "Yes"
            return "No"
        else:
            return "No"

controller = TVController(CHANNELS)


