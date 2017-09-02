from datetime import timedelta
def add_gigasecond(time_):
    # old
    # return datetime.fromtimestamp(time.mktime(time_.timetuple()) + 10**9)
    return time_ + timedelta(seconds=10**9)
