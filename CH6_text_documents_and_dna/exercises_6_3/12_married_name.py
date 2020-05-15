def married_name(full_name, spouse_last_name, hyphenate):
    """

    Args:
        full_name (str): The person's first and last name prior to the marriage.
        spouse_last_name (str): Spouse's last name
        hyphenate (bool): True if post-marriage name is hyphenation approach else False.

    Returns:
        (str): Person's new first and last name after the marriage.
    """

    if hyphenate:
        # Already have a string ending with the prior last name that simply
        #   needs hyphen plus spouse LN added--that's full_name:
        married_name = full_name + '-' + spouse_last_name
    else:
        first = full_name[:full_name.find(' ')] # Split off first name
        married_name = first + ' ' + spouse_last_name
    return married_name


name = 'Jane Doe'
spouse = 'Deer'

print(married_name(name, spouse, False))
print(married_name(name, spouse, True))
