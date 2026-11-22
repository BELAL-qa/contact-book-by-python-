import json
c={}
try:
    with open(r'contact.json','r')as f:
        c=json.load(f)
     
        
except FileNotFoundError:
   print("there are no numbers stored yet")
except json.JSONDecodeError:
   print('The contacts file is damaged. Starting a new contact book.')   
   
while True:
      print('====contact====\n\t')
      print('add')
      print('show all')
      print('exit')
      choose=input('choose : ')
      if choose=='add':
         while True:
            name=input('enter the name : ')
            number=input ('enter the phone number : ')
            c[name] = number
            print('saved , 100%')
            q1=input('add more / back step : ')
            
            if q1=='add more':
               continue
            elif q1=='back step':
               break
            else:
               print('Unknown answer, going back to the menu.')
               break
      elif choose=='show all':
         for i in c.items():
            print (i)
         with open (r'contact.json','w')as f:
            json.dump(c,f)
            
            
      elif choose=="exit":
         with open (r'contact.json','w')as f:
            json.dump(c,f)
            print('fine , goodbye! .... i miss you ... come back .... NOW!! ')
            break
      else:
         print('Invalid choice, Please type: add, show all or exit.')
          