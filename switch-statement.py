# Using a match ststement as an alternative to an if statement.
# if statement vs match statement

from unittest import case


http_status = 404

if http_status == 200 or http_status == 201:
    print('Success') 
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not found')
elif http_status == 500 or http_status == 501:
    print('server error')
else:
    print('Unknown')

match http_status:
  case 200:
    print('Success')
  case 400:
    print('Bad Request')
  case 500:
    print('Server Error')
  case _:
    print('unknown')

        
