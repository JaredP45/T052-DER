**Setup Instructions**
1. Clone repository
2. Create virtual env using `python3 -m venv venv`
3. cd into `DERSite`
4. Run `pip3 install -r requirements.txt`; all site packages used should install.
7. Run `python3 ./manage.py runserver` to run server and check localhost.
8. If localhost does not run, check:
   * Migrations should not have to be updated as both the database `db.sqlite3` and migrations folder are included, but in case server does not load run `python3 ./manage.py makemigrations`. If there are migrations to be made, run `python3 ./manage.py migrate`. __DO NOT PUSH UP CHANGES WITH MIGRATIONS!__as this will cause an alignment issue with existing migrations and the database. Running migrations terminal commands should be used only to get the localhost site to run for previewing/testing.
10. Site should be up and running!

**Website Requirements**

* Just below the navigation bar, there should be a photo banner with solar panels, wind turbines, and batteries. The title, “Welcome to DER8.9” with the subheading

* “Part of JakaaGen Inc” should be displayed over the photo.

* Just below the banner image, the following paragraph should be displayed: “DER8.9 is a leading utility company specializing in Distributed Energy Resources(DER). We are dedicated to revolutionizing the energy landscape by harnessing the power of renewable energy and advanced technology.”

* The top navigation bar should be designed in the following order: • DER8.9 logo • About Us • DER Data • Contact Us • Log In button

* When you click on the “About Us” link, scroll to the lower half of the page. You should be presented with a 3x2 cell block and the following heads: • Solar Power Solutions • Energy Storage Solutions • Microgrid Development • Demand Response Programs • Energy Management and Monitoring • Smart Grid Integration

* You should be able to login as an administrator using the below credentials: Email: admin@cfc.com | Password: test1234

* Upon logging in as admin, you should be welcomed to the Admin Portal and see 3 links on the left side of the page: • Dashboard • Contact Submissions • Registered Users

* Still logged in, click on the DER Data. You should see several graphs. The graph data should be live, and some graphs should be moving to show that.

* Clicking on the DER8.9 logo should bring you back to the “Home” screen.
* At the bottom of the page, upon clicking “Contact Us” you should be prompted with a Contact Form that requests: Full Name, Email, Phone Number, and a Message with an optional File Upload.


**Resources**

[User management](https://realpython.com/django-user-management/)
