import uuid

def print_error_message():
    print("Unwanted response or no input given.")

def get_server_name():
    res =  input("Which server are you referring to?\n[a] prodsysadmin01\n[b] prodtrack01\n[c] prodapi01\n[d] prodweb01")

    if res == 'a' or res == 'A':
        return "prodsysadmin01"
    elif res == 'b' or res == 'B':
        return 'prodtrack01'
    elif res == 'c' or res == 'C':
        return 'prodapi01'
    elif res == 'd'or res == 'D':
        return 'prodweb01'
    else:
        print_error_message()
        return get_server_name()


def get_change_request_info():
    return input("Please explain the change request in details:\n")

def get_alert_report():
    res1 = input("Which server?\n[a] prodsysadmin01\n[b] prodtrack01\n[c] prodapi01\n[d] prodweb01\n")

    if res1 == 'a' or res1 == 'A':
        res2 = input("Which threshold has been reached?\n[a] CPU Usage\n[b] Memory Usage\n[c] Disk Usage\n")
        if res2 == 'a' or res2 == 'A':
            return "CPU usage threshold has been reached in prodsysadmin01"
        elif res2 == 'b' or res2 == 'B':
            return "Memory usage threshold has been reached in prodsysadmin01"
        elif res2 == 'c' or res2 == 'C':
            return "Disk usage threshold has been reached in prodsysadmin01"
        else: 
            print_error_message()
            get_alert_report()
    elif res1 == 'b' or res1 == 'B':
        res2 = input("Which threshold has been reached?\n[a] CPU Usage\n[b] Memory Usage\n[c] Disk Usage\n")
        if res2 == 'a' or res2 == 'A':
            return "CPU usage threshold has been reached in prodtrack01"
        elif res2 == 'b' or res2 == 'B':
            return "Memory usage threshold has been reached in prodtrack01"
        elif res2 == 'c' or res2 == 'C':
            return "Disk usage threshold has been reached in prodtrack01"
        else: 
            print_error_message()
            get_alert_report()
    elif res1 == 'c' or res1 == 'C':
        res2 = input("Which threshold has been reached?\n[a] CPU Usage\n[b] Memory Usage\n[c] Disk Usage\n")
        if res2 == 'a' or res2 == 'A':
            return "CPU usage threshold has been reached in prodapi01"
        elif res2 == 'b' or res2 == 'B':
            return "Memory usage threshold has been reached in prodapi01"
        elif res2 == 'c' or res2 == 'C':
            return "Disk usage threshold has been reached in prodapi01"
        else: 
            print_error_message()
            get_alert_report()
    elif res1 == 'd' or res1 == 'D':
        res2 = input("Which threshold has been reached?\n[a] CPU Usage\n[b] Memory Usage\n[c] Disk Usage\n")
        if res2 == 'a' or res2 == 'A':
            return "CPU usage threshold has been reached in prodweb01"
        elif res2 == 'b' or res2 == 'B':
            return "Memory usage threshold has been reached in prodweb01"
        elif res2 == 'c' or res2 == 'C':
            return "Disk usage threshold has been reached in prodweb01"
        else: 
            print_error_message()
            get_alert_report()
    else:
        print_error_message()
        get_alert_report()

def get_name():
    return input("First, please let us know who am I speaking with?\n")

def other_desc():
    res = input("Please tell us what happen?")

    return res

def get_issue_type():
    res = input("What type of issue would you like to report?\n[a] Server Downtime\n[b] Change Request\n[c]Reporting an alert \n[d] Others\nYour answer: ")

    if res == 'a' or res == 'A':
        return "Server Downtime"
    elif res == 'b' or res == 'B':
        return "Change Request"
    elif res == 'c' or res == 'C':
        return "Alert Reporting"
    elif res == 'd' or res == 'D':
        return "Others"
    else:
        print_error_message()
        return get_issue_type()


def ticket_bot():
    print("Welcome to nPlay Ticketing Bot! My name is nPlayBot!")
    
    name = get_name()
    print("Hi " + name + "! Nice to meet you. :D")

    issue_type = get_issue_type()
    if issue_type == "Server Downtime":
        res_get_server_name = get_server_name()
        print("We noted that " + res_get_server_name + " is currently down! We will get back soon, this is your ticket number: ", end="")
        print(uuid.uuid1())
    elif issue_type == "Change Request":
        res_get_change_request_info = get_change_request_info()
        print("Your change request will be processed. \nThis is your change request details: " + res_get_change_request_info + "\n")
        print("This is your ticket number: ", end="")
        print(uuid.uuid1())
    elif issue_type == "Alert Reporting":
        res_get_alert_report = get_alert_report()
        print(res_get_alert_report)
        print("This is your ticket number: ", end="")
        print(uuid.uuid1())
    elif issue_type == "Others":
        res_other_desc = other_desc()
        print("This is your description:")
        print(res_other_desc)
        print("This is your ticket number: ", end="")
        print(uuid.uuid1())
    else:
        return None

    repeat = input("Is there anything else we can assist you with? If yes then enter 'yes'\n")

    if repeat == "yes":
        ticket_bot()
    else:
        print("Thanks for contacting us, our support will be in contact with you shortly. (subjected to issue critical level)")


ticket_bot()