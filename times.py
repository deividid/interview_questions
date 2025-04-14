def time_conflict(events):
    times = len(events)
    for i in range(times):
        i_start, i_end = events[i]
        for j in range(i + 1, times):
            j_start, j_end = events[j]
            overlap = []
            if j_start <= i_start <= j_end:
                if j_start <= i_end <= j_end:
                    overlap.append(i_start)
                    overlap.append(i_end)
                else:
                    overlap.append(i_start)
                    overlap.append(j_end)

            elif j_start <= i_end <= j_end:
                overlap.append(j_start)
                overlap.append(i_end)

            if len(overlap) > 0:
                return [True, overlap]

    return False


number_of_events = int(input())

events = []

for _ in range(number_of_events):
    event = input().split(', ')
    start_time = event[0].split(':')
    end_time = event[1].split(':')
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    end_hour = int(end_time[0])
    end_minute = int(end_time[1])
    s_time = start_hour * 60 + start_minute
    e_time = end_hour * 60 + end_minute
    events.append([s_time, e_time])


result = time_conflict(events)

if not result:
    print('false')
    print("The two events do not overlap.")

else:
    print('true')
    s_time = result[1][0]
    e_time = result[1][1]
    s_minute = s_time % 60
    s_hour = int((s_time - s_minute) / 60)
    e_minute = e_time % 60
    e_hour = int((e_time - e_minute) / 60)
    if s_minute < 10:
        s_minute = '0' + str(s_minute)
    if s_hour < 10:
        s_hour = '0' + str(s_hour)

    if e_minute < 10:
        e_minute = '0' + str(e_minute)

    if e_hour < 10:
        e_hour = '0' + str(e_hour)

    print(f"The two events overlap from {s_hour}:{s_minute} to {e_hour}:{e_minute}.")

