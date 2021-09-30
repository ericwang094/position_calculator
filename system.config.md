from following docs:
https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

https://www.youtube.com/watch?v=MAsp90tQGOA

* create ec2 in aws. and install required packages

```
sudo yum install python3-pip python3-devel 'Development Tools' openssl-devel libffi-devel python3-setuptools
```

* create a simple flask app [app.py](app/routes.py)

* create a service [file](useful_doc/position_calculator.service) under `/etc/systemd/system/`

* make sure user and group is config correctly

* then enable the service
```
sudo systemctl daemon-reload
sudo systemctl start position_calculator
sudo systemctl enable position_calculator
```

* Install Nginx 

```
sudo yum install nginx
```

* create two folders `/etc/nginx/sites-available` and `sites-enabled`

* create a [file](useful_doc/position_calculator) under sites-available. 

* Add sites-available folder into the nginx.conf under http block
```
include /etc/nginx/sites-enabled/*;
```

* link file from sites-available to sites-enabled
`sudo ln -s /etc/nginx/sites-available/position_calculator /etc/nginx/sites-enabled`

then `sudo systemctl restart nginx`