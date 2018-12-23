## DAIRY

### DAIRY RECORD MANAGEMENT AND PRODUCTION DATA ANALYTICS SYSTEM

A complete record tracking and production data analytics for dairy industries. This project has been
developed as per the requirements of Argha Dairy Udhyog, Nepal.

#### Install Instructions

1. Clone the repository:
```shell
git clone https://github.com/anisbhsl/DAIRY.git
```

2. Install the requirements:
```shell
sudo pip3 install -r install.txt
```

3. Connecting to database:

In your dairy/settings.py
```shell
DATABASES = {
    'default': {
        'NAME':'my_database', ## This is your database name
        'HOST':' ' ##Hostname , default is '127.0.0.1',
        'USER':'username', ##name of user
        'PASSWORD':' ', 
        'ENGINE': 'django.db.backends.mysql',
    }
}

```
[Help](https://django-mssql.readthedocs.io/en/latest/settings.html)
4. Finally goto the cloned directory and execute:
```shell
python3 manage.py runserver
```

#### Features
1. Record Keeping 
    - Milk Purchase Record
    - Stock Records
    - Product Sales Records
    - Operational Cost Records
2. Nepali Date Format
    - Select date using embedded [Nepali datepicker](http://sajanmaharjan.com.np/my-works/nepali-datepicker-ui/) built on jQuery
3. Easier Report Analysis for desired period
    - Print Report 
    - Convert Report to Excel format

#### App Screenshots
1. Dashboard
![Dash](/screenshots/dash.png)

2. Purchase Milk
![Purchase Milk](/screenshots/purchase_milk.png)

3. Stock
![Stock](/screenshots/add_stock.png)

4. Sell
![Sell](/screenshots/sell_products.png)

5. Reports
![Report](/screenshots/report.png)

6. Purchase Report
![Purchase_report](/screenshots/purchase_report.png)


#### License: [MIT](https://opensource.org/licenses/MIThttps://opensource.org/licenses/MIT)

#### Author
[Anish Bhusal](http://www.anish.info.np/)
