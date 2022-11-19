from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from database import mycursor


def manager(update, context):

    id = update.message.from_user.id

    mycursor.execute("SELECT userid, lastname, firstname FROM base WHERE status = ?", ("requestadmin", ))

    get = mycursor.fetchall()
    print(get)

    if get != []:
        admin_id = get[0][0]
        admin_firstname = get[0][1]
        admin_lastname = get[0][2]

        check = [
            [
                InlineKeyboardButton("✅", callback_data=f"tick_admin{admin_id}"),
                InlineKeyboardButton("❌", callback_data=f"x_admin{admin_id}")
            ]
        ]

        update.message.reply_text(f"{admin_firstname} {admin_lastname}", reply_markup=InlineKeyboardMarkup(check))

    else:

        update.message.reply_text("So'rovlar yo'q.")

def admin_management(update, context):


    id = update.message.from_user.id

    mycursor.execute("SELECT userid FROM base WHERE status = ?", ("Admin", ))
    get = mycursor.fetchone()

    check = [
        [
            InlineKeyboardButton("❌", callback_data=f"delete{get}")
        ]
    ]

    mycursor.execute("SELECT lastname, firstname FROM base WHERE status = ?", ("Admin", ))

    get = mycursor.fetchall()
    print(get)

    if get != []:
        admin_firstname = get[0][0]
        # mycursor.execute("SELECT lastname FROM base WHERE status = ?", ("requestadmin", ))
        admin_lastname = get[0][1]

        update.message.reply_text(f"{admin_firstname} {admin_lastname}", reply_markup=InlineKeyboardMarkup(check))

    else:

        update.message.reply_text("Adminlar yo'q.")
