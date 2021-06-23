# python_otp_sender
---
This is a python mudule by which one can easily send otp to any email. 
This is very helpful for web development purpose

## Prerequisites : --
1. install python module name as python-decouple
 ```bash
 pip install python-module
  ```
2. Create a gmail account for testing purpose and enable [less secure app](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NKHRfdHXxmxYgD6LATUhs6N6ww0sBX4aegeZFXtLmr_eZnEznzem-MKdS-PWBon8Nxo0ocZ3UZYJsm5aqb9VhvKlxayg)
3. Make `.env` file in your main directory and add these two lines in it
`EMAIL_ADDRESS=your testing email without ""
 PASSWORD=your testing email password without ""`
4. Keep the `python_otp` folder in your main directory.

## Demo code : -
```python
from python_otp import otp_for

email = "singh.rohitsingh2k@gmail.com"
otp = otp_for(email)
n = input("Enter recieved otp : ")

if n == otp:
   print("OTP IS CORRECT")
else:
   print("INCORRECT OTP")
```

## Note : -

The above module takes email where you want to send email as a string & it will return otp value which is sended to reciever's email.



