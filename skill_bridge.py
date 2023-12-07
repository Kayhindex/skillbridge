import sqlite3 as sq3
sqliteconn = sq3.connect("skill_bridge.db")
cursor = sqliteconn.cursor()


def run():
    #USER TABLE
    try:
        query = """CREATE TABLE user(
        user_id VARCHAR(10) Primary key not null,
        usename VARCHAR(20) not null,
        password VARCHAR(20) not null,
        email VARCHAR(50) not null,
        full_name VARCHAR(30) not null,
        date_of_birth VARCHAR(30) not null
        );
        """
        # cursor.execute(query)
        # query = 'DROP TABLE user'
        # cursor.execute(query)
        
    #SKILLS TABLE
        query = '''
            CREATE TABLE skills(
            skill_id VARCHAR(10) Primary key not null,
            skill_name VARCHAR(20) not null,
            description VARCHAR(20) not null                                     
        );
        '''
        # cursor.execute(query)
        # query = 'DROP TABLE skills'
        # cursor.execute(query)
    
    #LISTING TABLE
        query = '''
            CREATE TABLE listing(
            listing_id INTEGER(10) Primary key not null,
            user_id VARCHAR(20) not null,
            skill_id VARCHAR(20) not null,
            available_slots INTEGER(1) not null,
            price_per_slot INTEGER(10) not null
        );
        '''
        # cursor.execute(query)
        # query = 'DROP TABLE listing'
        # cursor.execute(query)
    
        
   
     #REQUEST TABLE
        query = '''
            CREATE TABLE request(
            request_id VARCHAR(10) PRIMARY KEY not null,
            user_id VARCHAR(10) not null,
            skill_id VARCHAR(10) not null,
            request_date VARCHAR(30) not null,
            status VARCHAR(20) not null    
        );
        '''
        # cursor.execute(query)
        # query = 'DROP TABLE request'
        # cursor.execute(query)
        

    #TRANSACTION TABLE
        query = '''
        CREATE TABLE transact(
        transaction_id VARCHAR(10) PRIMARY KEY,
        request_id VARCHAR(10),
        transaction_date VARCHAR(10),
        payment_status VARCHAR(15)
        
        );
        '''
        #cursor.execute(query)
        


    #RATING TABLE
        query ='''
            CREATE TABLE rating(
            rating_id VARCHAR(10) PRIMARY KEY not null,
            user_id VARCHAR(10) not null,
            skill_id VARCHAR(10) not null,
            rating_value INTEGER(2) not null,
            review_comment VARCHAR(100) not null
           
        );
        '''
        # cursor.execute(query)
       
        # query = 'DROP TABLE rating'
        # cursor.execute(query)

    #Inserting into user table:
        query ='''INSERT INTO user(user_id,usename,password,email,full_name,date_of_birth)
        VALUES("user001", "kennytech", "Heroes2019", "ayo@gmail.com","Akinpelu Kehinde", "6TH OF MAY");
        '''
        # cursor.execute(query)

        query ='''INSERT INTO user(user_id,usename,password,email,full_name,date_of_birth)
        VALUES("user002", "billon", "beulah23", "bay@gmail.com","Akinpelu Beulah", "6TH OF MAY");
        '''
        # cursor.execute(query)   
        query ='''INSERT INTO user(user_id,usename,password,email,full_name,date_of_birth)
        VALUES("user003", "tee-master", "Teeboy2023", "tee@gmail.com","Akinpelu Taiwo", "6TH OF MAY");
        '''
        # cursor.execute(query)
    
    #Inserting into skills table
        query =  '''INSERT INTO skills(skill_id,skill_name,description)
        VALUEs("sk001","frontend web developer", "i am a  professional at building a responsive website");
        '''
        # cursor.execute(query)
        query =  '''INSERT INTO skills(skill_id,skill_name,description)
        VALUEs("sk002","data scientist", "i am here to mine and clean your data");
        '''
        # cursor.execute(query)

        query =  '''INSERT INTO skills(skill_id,skill_name,description)
        VALUEs("sk003","business analyst", "i am business analyst");
        '''
        # cursor.execute(query)

    #Inserting into listing table
        query = '''INSERT INTO listing(listing_id,user_id,skill_id,available_slots,price_per_slot)
        VALUES(001, "user001","sk001",3, 100000);
        '''
        # cursor.execute(query)

        query = '''INSERT INTO listing(listing_id,user_id,skill_id,available_slots,price_per_slot)
        VALUES(002, "user003","sk002", 2, 100000);
        '''
        # cursor.execute(query)

        query = '''INSERT INTO listing(listing_id,user_id,skill_id,available_slots,price_per_slot)
        VALUES(003, "user003","sk001", 1, 100000);
        '''
        # cursor.execute(query)

    #Inserting into request table
        query = '''INSERT INTO request(request_id, user_id,skill_id,request_date, status)
        VALUES("R10001","user001","sk001","22nd Jan,2023", "pending");
        '''
        # cursor.execute(query)

        query = '''INSERT INTO request(request_id, user_id,skill_id,request_date, status)
        VALUES("R10002","user002","sk002","5th April,2023", "sucessful");
        '''
        # cursor.execute(query)

        query = '''INSERT INTO request(request_id, user_id,skill_id,request_date, status)
        VALUES("R10003","user003","sk003","3rd Sept,2023", "pending");
        '''
        # cursor.execute(query)

    #Inserting into transaction table
        query = '''INSERT INTO transact(transaction_id, request_id, transaction_date, payment_status)
        VALUES("#tr00041","R10001","7th may,2023", "paid");
        '''
        # cursor.execute(query)

        query = '''INSERT INTO transact(transaction_id, request_id, transaction_date, payment_status)
        VALUES("#tr00042","R10002","3rd june,2023", "paid");
        '''
        # cursor.execute(query)

        query = '''INSERT INTO transact(transaction_id, request_id, transaction_date, payment_status)
        VALUES("#tr00043","R10003","1st dec,2023", "paid");
        '''
        # cursor.execute(query)

    #Inserting into rating table

        query ='''INSERT INTO rating(rating_id,user_id,skill_id,rating_value, review_comment)
         VALUES("ra0001", "user001","sk001", "Good", "This platform is doing a great job!"); 
         '''
        # cursor.execute(query)

        query ='''INSERT INTO rating(rating_id,user_id,skill_id,rating_value, review_comment)
         VALUES("ra0002", "user002","sk002", "Fair"," "); 
         '''
        # cursor.execute(query)

        query ='''INSERT INTO rating(rating_id,user_id,skill_id,rating_value, review_comment)
         VALUES("ra0003", "user003","sk003", "Excellent", "This platform is doing a great job"); 
         '''
        # cursor.execute(query)



        
        
                                                           


        sqliteconn.commit()
        sqliteconn.close()


    except Exception as e:
        print(f"Error:{e}")

    finally:
        sqliteconn.close()
        print("Sqliteconnection closed")

if __name__ == "__main__":
    run()

