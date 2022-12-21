import view
import model
import logger

def run():
    user_request = view.choose_action()
    if user_request == 1:
        contact = view.new_contact()
        logger.create_person_logger(contact)
    elif user_request == 2:
        model.find_person()
    elif user_request == 3:
        model.list_employee()
        data = model.delete_person()
        contact = view.deleted_contact()
        logger.log_delet_person(data)
    elif user_request == 4:
        data = model.person_change()
        logger.log_person_change(data)
    elif user_request == 5:
        data = model.list_employee()
