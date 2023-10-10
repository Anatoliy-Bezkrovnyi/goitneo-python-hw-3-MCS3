from constans import SECONDS_IN_MINUTE

def minutes_to_seconds(minutes: int) -> int:
    return minutes * SECONDS_IN_MINUTE

def minutes_to_miliseconds(minutes: int) -> int:
    return minutes * SECONDS_IN_MINUTE * 1000

#print(minutes_to_seconds(23))
#print(minutes_to_miliseconds(23))