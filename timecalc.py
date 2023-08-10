import math

# start = '11:43 PM'
# dur = '83:20'


def add_time(start_time, duration, day = None):
    week = ['monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']
    time_script = ['AM','PM']
    
    # making a list of start time
    start_time_list = start_time.split(':')
    min_script_list = start_time_list[1].split(' ')
    start_time_list.remove(start_time_list[1])
    
    for x in min_script_list:
        start_time_list.append(x)
    # print(start_time_list)
    
    # making a list of duration
    duration_list = duration.split(':')
    
    # making time to be added 
    start_hour = int(start_time_list[0])
    start_minutes = int(start_time_list[1])
    start_time_script = start_time_list[2]
    # print(start_time_script)
    
    hours_to_be_added = int(duration_list[0])
    minutes_to_be_added = int(duration_list[1])
    
    # vaidating minutes in the duration provided 
    if minutes_to_be_added >= 60:
        raise Exception('MinutesError: Minutes should be less than 60')
    else:pass
    # print(duration_list)
    
    
    # adding the time 
    # sorting the hour addition
    final_Twelve_HCS = start_hour + hours_to_be_added
    
    original_total = final_Twelve_HCS
    
    if final_Twelve_HCS >= 12:
        
        final_Twelve_HCS = final_Twelve_HCS % 12
        
        if start_time_script == 'AM':
            # final_time_script =start_time_script
            final_time_script = 'PM'
        else:
            final_time_script ='AM'
            # final_time_script = time_script[0]
            
    else:
        final_time_script = start_time_script       
    # adding minutes 
    end_minutes = start_minutes + minutes_to_be_added
    
    if end_minutes >= 60:
        end_minutes = end_minutes % 60
        final_Twelve_HCS += 1
        
        if final_Twelve_HCS >= 12:
        
            final_Twelve_HCS = final_Twelve_HCS % 12
            
            if start_time_script == 'AM':
                final_time_script = 'PM'
                
            elif start_time_script == 'PM':
                final_time_script = 'AM'
        else:
            final_time_script = start_time_script
        
        
    # days 
    if original_total >= (24):
        day_index = (original_total/24).__round__(1)
        # day_index = int(day_index)
        # print(original_total)
        days_no = math.ceil(day_index)
        # print(days_no)
        if day_index > 1:
            if int(days_no) < 4:
                
                if not day:
                    print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} ({days_no} days later)')
                else:
                    for x in range(len(week)):
                        if day == week[x]:
                            next_day = week[x + days_no]
                            print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} {next_day}({days_no} days later)')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} ({int(day_index.__round__(0))} days later)')
        elif day_index == 1:
            print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} (next later)')
        else:
            if not day:
                 print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script}')    
            else:   
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} {day}')
    else:
        if start_time_script =='AM' and final_time_script =='PM':
            if day:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} {day}')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script}')
        elif start_time_script =='PM' and final_time_script =='AM':
            if not day:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} (next day)')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script}')
        elif start_time_script == final_time_script:
            if day:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script} {day}')
            else:
                print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script}')
   
    # print(f'{final_Twelve_HCS}:{end_minutes} {final_time_script}')    

add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tuesday")
add_time("6:30 PM", "205:12")