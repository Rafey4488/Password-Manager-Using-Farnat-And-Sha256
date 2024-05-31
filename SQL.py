import sqlite3
import time

con = sqlite3.connect('IS_Project.db')
cursor = con.cursor()
cursor2 = con.cursor()
cursor3 = con.cursor()

# cursor.executescript('''
#     CREATE TABLE IF NOT EXISTS login (
#         UserName VARCHAR(50) PRIMARY KEY,
#         U_or_A CHAR(1) NOT NULL DEFAULT 'U',
#         Email VARCHAR(45) NOT NULL,
#         Password VARCHAR(256) NOT NULL,
#         UNIQUE (UserName),
#         UNIQUE (Email)
#     );

#     CREATE TABLE IF NOT EXISTS user_details (
#         ID INTEGER NOT NULL ,
#         LoginUserName VARCHAR(50) NOT NULL,
#         Account_Username VARCHAR(50) NOT NULL,
#         Account_Password VARCHAR(256) NOT NULL,
#         Website_Name VARCHAR(50) NOT NULL,
#         URL VARCHAR(200) NOT NULL,
#         Description VARCHAR(150),
#         User_Salt VARCHAR(256) NOT NULL,
#         PRIMARY KEY (ID, LoginUserName),
#         FOREIGN KEY (LoginUserName) REFERENCES login (UserName)
#     );

#     CREATE TABLE IF NOT EXISTS user_show (
#         ID INTEGER PRIMARY KEY,
#         UserName VARCHAR(50) NOT NULL,
#         Account_Username VARCHAR(50) NOT NULL,
#         Account_Password VARCHAR(256) NOT NULL,
#         Website_Name VARCHAR(50) NOT NULL,
#         URL VARCHAR(200) NOT NULL,
#         Description VARCHAR(150),
#         FOREIGN KEY (UserName) REFERENCES user_details (LoginUserName)
#     );
# ''')
# cursor.execute("Insert into login(UserName,U_or_A,Email,Password) values('Ahmed','A','az279158@gmail.com','ff2ccb6ba423d356bd549ed4bfb76e96976a0dcde05a09996a1cdb9f83422ec4')")
# cursor2.execute("Insert into login(UserName,U_or_A,Email,Password) values('Rafey','A','rafay@gmail.com','89aa1e580023722db67646e8149eb246c748e180e34a1cf679ab0b41a416d904')")
# cursor2.executescript('''
#                       DROP TRIGGER IF EXISTS insert_user_show;
# DROP TRIGGER IF EXISTS update_user_show;
# DROP TRIGGER IF EXISTS delete_user_show;''')

# time.sleep(10)

# cursor.executescript('''-- Insert Trigger
# CREATE TRIGGER insert_user_show
# AFTER INSERT ON user_details
# BEGIN
#     INSERT INTO user_show (ID, UserName, Account_Username, Account_Password, Website_Name, URL, Description)
#     VALUES (NEW.ID, NEW.LoginUserName, NEW.Account_Username, NEW.Account_Password, NEW.Website_Name, NEW.URL, NEW.Description);
# END;

# -- Update Trigger
# CREATE TRIGGER update_user_show
# AFTER UPDATE ON user_details
# BEGIN
#     UPDATE user_show
#     SET Account_Username = NEW.Account_Username,
#         Account_Password = NEW.Account_Password,
#         Website_Name = NEW.Website_Name,
#         URL = NEW.URL,
#         Description = NEW.Description
#     WHERE ID = NEW.ID;
# END;

# -- Delete Trigger
# CREATE TRIGGER delete_user_show
# AFTER DELETE ON user_details
# BEGIN
#     DELETE FROM user_show WHERE ID = OLD.ID;
# END;
# ''')

cursor.execute('''CREATE INDEX INDEX_OF_ACCOUNT_PASSWORD_COLUMN ON user_show(Account_Password);
''')

con.commit()
con.close()