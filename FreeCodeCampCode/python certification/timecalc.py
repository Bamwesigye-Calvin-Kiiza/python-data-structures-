import math

def add_time(start_time, duration, day=None):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    time_script = ['AM', 'PM']
    
    start_time_list = start_time.split(':')
    min_script_list = start_time_list[1].split(' ')
    start_time_list.remove(start_time_list[1])
    
    for x in min_script_list:
        start_time_list.append(x)
    
    duration_list = duration.split(':')
    
    start_hour = int(start_time_list[0])
    start_minutes = int(start_time_list[1])
    start_time_script = start_time_list[2]
    
    hours_to_be_added = int(duration_list[0])
    minutes_to_be_added = int(duration_list[1])
    
    if minutes_to_be_added >= 60:
        raise Exception('MinutesError: Minutes should be less than 60')
    
    end_minutes = start_minutes + minutes_to_be_added
    final_Twelve_HCS = start_hour + hours_to_be_added  
    
    if end_minutes >= 60:
        end_minutes = end_minutes % 60
        final_Twelve_HCS += 1
         
    original_total = final_Twelve_HCS
    
    if final_Twelve_HCS > 12:
        final_Twelve_HCS = final_Twelve_HCS % 12
        
        if start_time_script == 'AM':
            final_time_script = 'PM'
        else:
            final_time_script = 'AM'
            
    elif   final_Twelve_HCS == 12:  
        final_Twelve_HCS = 12
        if start_time_script == 'AM':
            final_time_script = 'PM'
        else:
            final_time_script = 'AM'
        
    else:
        final_time_script = start_time_script
        
    
    if original_total >= 24:
        day_index = (original_total / 24).__round__(1)
        days_no = math.ceil(day_index)
        
        if day_index > 1:
            if int(days_no) < 4:
                if not day:
                    print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script} ({days_no} days later)')
                else:
                    next_day = week[(week.index(day.lower()) + days_no) % 7]
                    print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}, {next_day.capitalize()} ({days_no} days later)')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script} ({int(day_index.__round__(0))} days later)')
        elif day_index == 1:
            print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script} (next day)')
        else:
            if not day:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}, {day.capitalize()}')
    else:
        if start_time_script == 'AM' and final_time_script == 'PM':
            if day:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}, {day.capitalize()}')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}')
        elif start_time_script == 'PM' and final_time_script == 'AM':
            if not day:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script} (next day)')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}')
        elif start_time_script == final_time_script:
            if day:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}, {day.capitalize()}')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes:02} {final_time_script}')

# Example usage
add_time("8:16 PM", "466:02", "tuesday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("2:59 AM", "24:00")
