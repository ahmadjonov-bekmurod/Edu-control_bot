from telegram import InlineKeyboardMarkup

from data import action
# from admin import accept_teacher
from database import mycursor, mydb


def query(update, context):

    query = update.callback_query


    if query.data.startswith("tick_admin"):

        id = query.data[10:]

        mycursor.execute("SELECT id, firstname, lastname FROM base WHERE userid = ?", (id, ))

        get = mycursor.fetchall()

        login = get[0][1].lower() + get[0][2].lower() + str(get[0][0])
        password = get[0][1].lower() + str(id)[-3:-1]

        print(login, password, id)

        mycursor.execute("UPDATE base SET status = ? , login = ? , password = ? WHERE userid = ?", ("Admin", login, password, id, ))
        mydb.commit()

        print("1>>",login)
        print("2>>",password)
        print("3>>",get)


        context.bot.send_message(chat_id=id, text=f"Login: <code>{login}</code>\nParol: <code>{password}</code>", parse_mode="HTML")

        query.message.delete()
        query.message.reply_text("Admin qo'shildi.")

    if query.data.startswith("x_admin"):

        id = query.data[7:]

        mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (id, "requestadmin", ))
        mydb.commit()

        query.message.delete()
        query.message.reply_text("Inkor qilindi.")

    if query.data.startswith("delete"):

        id = query.data[6:]

        print(id)

        mycursor.execute("DELETE FROM base WHERE id = ?", (id, ))
        mydb.commit()

        query.message.delete()
        query.message.reply_text("Admin o'chirildi.")

    if query.data == "_Rad etish":

        query.message.reply_html("<b>Rad etish</b>\nO'qituvchining id raqamini kiriting.")

        action.append("Rad")

    if query.data == "_Qabul qilish":

        query.message.reply_html("<b>Qabul qilish</b>\nO'qituvchining id raqamini kiriting.")

        action.append("Qab")

    # if query.data.startswith("_Rad etish"):
    #
    #     query.message.reply_text("O'qituvchining id raqamini kiriting.")
    #
    # if query.data == "_O'chirish":
    #
    #     query.message.reply_text("O'qituvchining id raqamini kiriting.")

    # if query.data.startswith("id") and query.data.endswith("delete"):
    #
    #     id = query.data[2:4]
    #
    #     mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (id, "requestteacher", ))
    #     mydb.commit()
    #
    #     query.message.delete()
    #     query.message.reply_text("O'chirildi.")
    #
    # if query.data == "_Rad etish":
    #
    #     text = query.message.text
    #
    #     mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (text[:2], "requestteacher", ))
    #     mydb.commit()
    #
    #     query.message.delete()
    #     query.message.reply_text("O'chirildi.")
    #
    # if query.data == "_Qabul qilish":
    #
    #     text = query.message.text
    #
    #     mycursor.execute("UPDATE base SET status = ? WHERE id = ?", ("Teacher", text[:2]))
    #     mydb.commit()
    #
    #     query.message.delete()
    #     query.message.reply_text("Qo'shildi.")
