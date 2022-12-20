import view
import model
import logger

def run():
    user_request = view.choose_action()
    if user_request == 1:
        contact = view.new_contact()
        logger.create_person_logger(contact)
    elif user_request == 2:
        result = model.find_person()
        # view.show_found(result)
    elif user_request == 3:
        data = model.delete_person()
        view.deleted_contact(data)
    elif user_request == 4:
        data = model.person_change()
    elif user_request == 5:
        data = model.list_employee()
        
