from database import mycursor, mydb

firstname = ""
lastname = ""


def request_first_name(update, context):

    update.message.reply_text("Ismingizni kiriting: ")

    return request_first_name

def request_last_name(update, context):
    global firstname
    firstname = update.message.text

    update.message.reply_text("Familyangizni kiriting: ")

    return request_last_name

def requestadmin(update, context):

    lastname = update.message.text

    id = update.message.from_user.id


    # login = firstname.lower() + lastname.lower()
    # password = firstname.lower() + str(id)[-3:-1]

    mycursor.execute("INSERT INTO base(userid, firstname, lastname, teacher, mother, father, status, login, password) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, firstname, lastname, None, None, None, "requestadmin", None, None))
    mydb.commit()

    update.message.reply_text("Ariza topshirildi!")

