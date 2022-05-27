with open('numbers.txt','r') as f, open('output.html','w') as s, open('text.txt','r') as t:
    lines = f.readlines()
#count = 0
    for line in lines:
        msg = t.read()
        s.write(f' <a target="blank" href={"https://api.whatsapp.com/send/?phone=91"+line+"&text="+msg+""}>{line}</a>')
        #s.write("https://api.whatsapp.com/send/?phone=91"+line+"&text=https%3A%2F%2Fdzicard.com%2Fdbc%2Fneerworld-polymers+Click+the+above+link+and+connect+with+us+by+clicking+on+icon+in+the+link&app_absent=0")    
        #print("https://api.whatsapp.com/send/?phone=91"+line+"&text=https%3A%2F%2Fdzicard.com%2Fdbc%2Fneerworld-polymers+Click+the+above+link+and+connect+with+us+by+clicking+on+icon+in+the+link&app_absent=0")
