from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from data import action
from database import mycursor, mydb


def _buttons_set(status, text, text1):

    mycursor.execute("SELECT userid, lastname, firstname, id FROM base WHERE status = ?", (status, ))

    get = mycursor.fetchall()
    print(get)

    if get != []:

        i = 0

        myString = ""
        while i <= len(get)-1:
            myString+=f"<b>{get[i][3]}</b> - {get[i][1]} {get[i][2]}\n"
            print("myS", myString)
            i+=1

        btn = [
            [
                InlineKeyboardButton(str(text), callback_data=f"_{text}"),
                InlineKeyboardButton(str(text1), callback_data=f"_{text1}")
            ]
        ]

        # update.message.reply_html(f"{myString}", reply_markup=InlineKeyboardMarkup(btn))

        return myString, btn

    else:

        return None

def admin(update, context):

    text = _buttons_set("Teacher", "Tahrirlash", "O'chirish")

    if text != None:
        update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))
    else:
        update.message.reply_text("O'qituvchilar mavjud emas.")

    return admin


def req_teacher(update, context):

    text = _buttons_set("requestteacher", "Rad etish", "Qabul qilish")

    if text is not None:
        update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))

    else:
        update.message.reply_text("So'rovlar yo'q.")

    return admin

def accept_teacher(update, context):

    print(action)

    if len(action) != 0:
        if action[0] == "Qab":
            action.clear()
            id = update.message.text

            print(id)

            mycursor.execute("SELECT userid, firstname, lastname FROM base WHERE id = ?", (id, ))

            get = mycursor.fetchall()

            print(get)

            login = get[0][1].lower() + get[0][2].lower() + id
            password = get[0][1].lower() + str(get[0][0])[-3:-1]

            mycursor.execute("UPDATE base SET status = ? , login = ? , password = ? WHERE id = ?", ("Teacher", login, password, id, ))
            mydb.commit()

            context.bot.send_message(chat_id=get[0][0], text=f"Login: {login}\nParol: {password}")

            update.message.delete()
            update.message.reply_text("O'qituvchi qo'shildi.")

        elif action[0] == "Rad":
            action.clear()
            id = update.message.text

            mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (int(id), "requestteacher", ))
            mydb.commit()

            update.message.delete()
            update.message.reply_text("Rad etildi.")

        return admin
