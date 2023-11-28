class PeriodHandler:
    def __init__(self, periods):
        self.periods = periods

    def compute_average_length_of_period(self):
        total_length = 0
        for period in self.periods:
            total_length += period.length
        return total_length / (len(self.periods))

    def get_most_recent_complete(self):
        return self.periods[-1]

    def compute_average_length_of_cycle(self):
        cycle_distances = []
        (len(self.periods))

        for i in range(len(self.periods)-1):
            length = self.periods[i + 1].start - self.periods[i].start
            cycle_distances.append(int(length.days))
        return sum(cycle_distances)/len(cycle_distances)
