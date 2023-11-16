from datetime import datetime

date_format = '%d/%m/%y %H:%M:%S'

def to_timestamp(str_time):
	return datetime.strptime(str_time, date_format).timestamp()

def time_to_string(t):
	return t.strftime('%B %d, %A, at %H:%M')

def time_from_utc(seconds):
	return datetime.utcfromtimestamp(seconds)