import re,time,requests

def get_email_by_site(sites):
    for i in sites:
        data_site = requests.get(i)
        return_regex = re.findall(f"[\w\.-]+@[\w\.-]+\.\w+",data_site.text)
        if return_regex:
            return (list(set(return_regex)))
        else:
            return None
        
sites = ["https://medium.com/labhacker"]

count_x = 0

try:
    for x in sites:
        mails = (get_email_by_site([x]))
        if mails != "None" or mails != None:
            print(mails)
        count_x = count_x + 1
except:
    print(x)
    pass