from telegram import ReplyKeyboardMarkup

from admin import admin
from database import mycursor
from manager import manager
from start import start
from teacher import teacher

manager_buttons = ReplyKeyboardMarkup([['Admin qo\'shish'], ["Adminlarni boshqarish"]],
                                      resize_keyboard=True)  # , one_time_keyboard=True
admin_buttons = ReplyKeyboardMarkup(
    [['O\'qituvchi qo\'shish', 'O\'qituvchilarni boshqarish'], ["O'quvchilarni qo'shish", "O'quvchi boshqarish"],
     ["Ota-ona qo'shish", "Ota-onalarni boshqarish"]], resize_keyboard=True)  # , one_time_keyboard=True
teacher_buttons = ReplyKeyboardMarkup([['Baholar', 'Qo\'shimcha darslik'], ["Uyga vazifa"]],
                                      resize_keyboard=True)  # , one_time_keyboard=True
pupil_buttons = ReplyKeyboardMarkup([['Baholarim', 'Qo\'shimcha darsliklarim'], ["Uyga vazifalarim"]],
                                    resize_keyboard=True)  # , one_time_keyboard=True
parent_buttons = ReplyKeyboardMarkup([['Baholarim', 'Qo\'shimcha darsliklarim'], ["Uyga vazifalarim"]],
                                     resize_keyboard=True)  # , one_time_keyboard=True


def login(update, context):
    id = update.message.from_user.id
    msg = update.message.text

    mycursor.execute("SELECT userid FROM base")
    ids = mycursor.fetchall()

    id_list = []

    for idm in range(len(ids)):
        id_list.append(ids[idm][0])
    print(id_list)
    if id in id_list:
        mycursor.execute("SELECT login, password, status FROM base WHERE userid = ?", (id,))
        get = mycursor.fetchall()

        _login = get[0][0]
        _password =get[0][1]
        _status = get[0][2]

        if len(msg.split()) == 2:
            login = msg.split()[0]
            password = msg.split()[1]

            if login == _login and password == _password:
                if _status == "Manager":
                    update.message.reply_html("Quyidagi tugmalardan birini tanlang: ", reply_markup=manager_buttons)

                    return manager

                if _status == "Admin":
                    update.message.reply_html("Quyidagi tugmalardan birini tanlang: ", reply_markup=admin_buttons)

                    return admin

                if _status == "Teacher":
                    update.message.reply_html("Quyidagi tugmalardan birini tanlang: ", reply_markup=teacher_buttons)

                    return teacher

                if _status == "Pupil":
                    update.message.reply_html("Quyidagi tugmalardan birini tanlang: ", reply_markup=pupil_buttons)

                    return admin


            else:

                update.message.reply_text("Parol yoki login no'to'g'ri! Iltimos qaytadan kiriting: ")

                return start

        else:

            update.message.reply_text("Login yoki parol kiritilmadi!")

            return start

    else:

        update.message.reply_text("Siz ro'yxatdan o'tmagansiz.")