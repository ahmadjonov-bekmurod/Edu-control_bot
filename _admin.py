# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#
# from database import mycursor, mydb
#
#
# # def id_buttons(status):
# #
# #     mycursor.execute("SELECT id FROM base WHERE status = ?", (status, ))
# #
# #     ids = mycursor.fetchall()
# #
# #     buttons = []
# #     tmp_b = []
# #
# #     for id in ids:
# #
# #         tmp_b.append(InlineKeyboardButton(str(id[0]), callback_data="id" + str(id[0]) + "delete"))
# #
# #         if len(tmp_b) == 3:
# #             buttons.append(tmp_b)
# #             tmp_b = []
# #
# #     return buttons
#
#
# def _teacher(status, text, text1):
#
#     mycursor.execute("SELECT userid, lastname, firstname, id FROM base WHERE status = ?", (status, ))
#
#     get = mycursor.fetchall()
#     print(get)
#
#     if get != []:
#
#         i = 0
#
#         myString = ""
#         while i <= len(get)-1:
#             myString+=f"<b>{get[i][3]}</b> - {get[i][1]} {get[i][2]}\n"
#             print("myS", myString)
#             i+=1
#
#         btn = [
#             [
#                 InlineKeyboardButton(str(text), callback_data=f"_{text}"),
#                 InlineKeyboardButton(str(text1), callback_data=f"_{text1}")
#             ]
#         ]
#
#         # update.message.reply_html(f"{myString}", reply_markup=InlineKeyboardMarkup(btn))
#
#         return myString, btn
#
#     else:
#
#         return None
#
# # def admin(update, context):
#
#     # text = teacher("Teacher", "Tahrirlash", "O'chirish")
#     #
#     # if text != None:
#     #     update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))
#     # else:
#     #     update.message.reply_text("O'qituvchilar mavjud emas.")
#     #
#     # return admin
#
# def _teacher(update, context):
#
#     text = update.message.text
#
#     if text == "O\'qituvchilarni boshqarish":
#
#         text = teacher("Teacher", "Tahrirlash", "O'chirish")
#
#         if text != None:
#             update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))
#         else:
#             update.message.reply_text("O'qituvchilar mavjud emas.")
#
#         return delete_teacher
#
#     if text == "O\'qituvchi qo\'shish":
#         text = teacher("requestteacher", "Rad etish", "Qabul qilish")
#
#         if text is not None:
#             update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))
#
#         else:
#             update.message.reply_text("So'rovlar yo'q.")
#
#         return reject_teacher
#
# def delete_teacher(update, context):
#
#         id = update.message.text
#
#         mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (int(id), "Teacher", ))
#         mydb.commit()
#
#         update.message.delete()
#         update.message.reply_text("O'chirildi.")
#
#         return delete_teacher
#
# def reject_teacher(update, context):
#
#         id = update.message.text
#
#         mycursor.execute("DELETE FROM base WHERE id = ? and status = ?", (int(id), "requestteacher", ))
#         mydb.commit()
#
#         update.message.delete()
#         update.message.reply_text("Rad etildi.")
#
#         return reject_teacher
# #
# # def accept_teacher(update, context):
# #
# #     id = update.message.text
# #
# #     mycursor.execute("SELECT id, firstname, lastname FROM base WHERE userid = ?", (id, ))
# #
# #     get = mycursor.fetchall()
# #
# #     login = get[0][1].lower() + get[0][2].lower() + str(get[0][0])
# #     password = get[0][1].lower() + str(id)[-3:-1]
# #
# #     mycursor.execute("UPDATE base SET status = ? , login = ? , password = ? WHERE userid = ?", ("Teacher", login, password, id, ))
# #     mydb.commit()
# #
# #     context.bot.send_message(chat_id=id, text=f"Login: {login}\nParol: {password}")
# #
# #     update.message.delete()
# #     update.message.reply_text("O'qituvchi qo'shildi.")
# #
# #     return accept_teacher
#
# # def req_teacher(update, context):
# #
# #     text = teacher("requestteacher", "Rad etish", "Qabul qilish")
# #
# #     if text is not None:
# #         update.message.reply_html(text[0], reply_markup=InlineKeyboardMarkup(text[1]))
# #
# #     else:
# #         update.message.reply_text("So'rovlar yo'q.")
# #
# #     return admin
#
# def student(update, context):
#
#     update.message.reply_text("pupil")
#
# def parent(update, context):
#
#     update.message.reply_text("parent")
