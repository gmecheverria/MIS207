class Time:

    def __init__(self, seconds=0, minutes=0, hours=0):
        self._seconds = seconds+minutes*60+hours*(60*60)

    def __str__(self):
        hours = self._seconds // 3600
        minutes = (self._seconds % 3600) // 60
        seconds = (self._seconds % 3600) % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def get_seconds(self):
        return self._seconds

    def __add__(self, other):
        return Time(seconds=self._seconds+other.get_seconds())

    def __sub__(self, other):
        diff = self._seconds - other.get_seconds()
        if diff > 0:
            return Time(seconds=self._seconds-other.get_seconds())
        else:
            return Time()
    


