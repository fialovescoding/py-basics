def get_pwd_from_user(message):
    print(message)

    #TODO: Get user input without showing on screen
    return None

# THE CODE STARTS HERE

mpwd = get_pwd_from_user(message="Enter the master password")

if verify_pwd(mpwd):
    what = get_user_input(message="What do you want to access?")

    # Search database for 'what' to get the matching values
    matches = dict_look_up(what)

    if matches is None:
        # No match found, report and restart
        restart(message="No matching secret found")

    which_one = get_user_input(message=matches)

    hint = get_hint(which_one)

    hint_response = get_user_input(message=hint)
    verify hint_response
else:
    restart()