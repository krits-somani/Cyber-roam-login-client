import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import mechanize
import time
users=["username"]   #id
passwords=["password"] #password
for i in range(12):
    for j in range(len(users)) :
        
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_refresh(False)
       
        br.open("https://10.100.56.55:8090/")  
        br.select_form('frmHTTPClientLogin')
        ima = users[j]
        br.form['username'] = users[j]
        br.form['password'] = passwords[j]
        br.submit()
        info= br.response().read()
        
        if 'login limit' in info:
            pass
        if 'logged in' in info:
            print "================="
            print "Logged in to : " + str(ima)
            print "================="
            break
    time.sleep(6000)




