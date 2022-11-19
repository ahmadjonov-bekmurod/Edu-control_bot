from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler, CommandHandler, MessageHandler, Filters

from admin import admin, req_teacher, accept_teacher
from login import login
from manager import manager, admin_management
from query import query
from requestadmin import requestadmin, request_first_name, request_last_name
from requestpupil import request_pupil_first_name, request_pupil_last_name, requestpupil
from requestteacher import request_teacher_first_name, request_teacher_last_name, requestteacher
from start import start
from teacher import marks, lessons, homeworks, teacher


def main():

    # TOKEN = "5204287604:AAGM95e3c_B-6DraDjCx2B6VJFvjbeMstbs" # Echo bot
    TOKEN = "5931193613:AAH4GVnxO7PdQmT694zjQYjLc2xOLJNpd8E" # @edu_control_bot

    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CallbackQueryHandler(query))

    chand = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            start: [
                MessageHandler(Filters.text & ~Filters.command, login)
            ],
            manager: [
                MessageHandler(Filters.regex('^(Admin qo\'shish)$'), manager),
                MessageHandler(Filters.regex('^(Adminlarni boshqarish)$'), admin_management),
            ],
            admin: [
                MessageHandler(Filters.regex("O\'qituvchilarni boshqarish"), admin),
                MessageHandler(Filters.regex("O\'qituvchi qo\'shish"), req_teacher),
                MessageHandler(Filters.regex("^[0-9]*$"), accept_teacher)
            ],
            teacher: [
                MessageHandler(Filters.regex("^(Baholar)$"), marks),
                MessageHandler(Filters.regex("^(Qo\'shimcha darslik)$"), lessons),
                MessageHandler(Filters.regex("^(Uyga vazifa)$"), homeworks)
            ]
        },
        fallbacks=[CommandHandler('start', start)])

    request = ConversationHandler(
            entry_points=[CommandHandler('requestadmin', request_first_name)],
            states={
            request_first_name: [
                MessageHandler(Filters.text & ~Filters.command, request_last_name)
            ],
            request_last_name: [
                MessageHandler(Filters.text & ~Filters.command, requestadmin)
            ]
        },
        fallbacks=[CommandHandler('start', start)])

    request_t = ConversationHandler(
            entry_points=[CommandHandler('requestteacher', request_teacher_first_name)],
            states={
            request_teacher_first_name: [
                MessageHandler(Filters.text & ~Filters.command, request_teacher_last_name)
            ],
            request_teacher_last_name: [
                MessageHandler(Filters.text & ~Filters.command, requestteacher)
            ]
        },
        fallbacks=[CommandHandler('start', start)])


    request_p = ConversationHandler(
            entry_points=[CommandHandler('requestpupil', request_pupil_first_name)],
            states={
            request_pupil_first_name: [
                MessageHandler(Filters.text & ~Filters.command, request_pupil_last_name)
            ],
            request_pupil_last_name: [
                MessageHandler(Filters.text & ~Filters.command, requestpupil)
            ]
        },
        fallbacks=[CommandHandler('start', start)])


    dispatcher.add_handler(request_p)
    dispatcher.add_handler(request_t)
    dispatcher.add_handler(request)
    dispatcher.add_handler(chand)

    # dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

main()
