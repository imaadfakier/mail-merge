# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

# # iterate over invited.names.txt
# with open(file='/Users/Imaad Fakier/Desktop/ON MY COMPUTER/courses/I N  P R O G R E S S/PYTHON/programs/'
#                'day twenty four/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as names_data_file:
#     names = names_data_file.readlines()
#     # print(name)
#     for person_name in names:
#         with open(file='./Input/Letters/starting_letter.txt', mode='r') as letter_template_file:
#             letter_template = letter_template_file.read()
#             # print(letter_template)
#             # personal_invite = letter_template.replace(__old='[name]', __new=person_name)  # <--- learned something
#                                                                                             # new
#             # personal_invite = letter_template.replace('[name]', person_name)
#             # personal_invite = letter_template.replace('[name]', person_name.strip())   # <--- learned something new
#             personal_invite = letter_template.replace(PLACEHOLDER, person_name.strip())
#             # print(personal_invite)
#             # with open(file='./Output/ReadyToSend/{}.txt'.format(person_name)) as invite_letter:
#             # with open(file='./Output/ReadyToSend/{name}.txt'.format(name=person_name.strip())) as invite_letter:
#             with open(file=f'./Output/ReadyToSend/{person_name.strip()}.txt', mode='w') as invite_letter_file:
#                 contents = invite_letter_file.write(personal_invite)
#                 # print(contents)  # nothing wrong but won't output desired result as file mode is 'w' - not 'r'

# with open(file='/Users/Imaad Fakier/Desktop/ON MY COMPUTER/courses/I N  P R O G R E S S/PYTHON/programs/'
#                'day twenty four/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as names_data_file:
#     names = names_data_file.readlines()
#     with open(file='./Input/Letters/starting_letter.txt', mode='r') as letter_template_file:
#         letter_template = letter_template_file.read()
#         for person_name in names:    # <--- learned something new
#             personal_invite = letter_template.replace(PLACEHOLDER, person_name.strip())
#             with open(file=f'./Output/ReadyToSend/{person_name.strip()}.txt', mode='w') \
#                     as invite_letter_file:
#                 contents = invite_letter_file.write(personal_invite)

with open(file='/Users/Imaad Fakier/Desktop/ON MY COMPUTER/courses/I N  P R O G R E S S/PYTHON/programs/'
               'day twenty four/Mail Merge Project Start/Input/Names/invited_names.txt', mode='r') as names_data_file:
    names = names_data_file.readlines()

with open(file='./Input/Letters/starting_letter.txt', mode='r') as letter_template_file:  # <--- learned something new
    letter_template = letter_template_file.read()
    for person_name in names:    # <--- learned something new
        personal_invite = letter_template.replace(PLACEHOLDER, person_name.strip())
        with open(file=f'./Output/ReadyToSend/letter_for_{person_name.strip()}.txt', mode='w') as invite_letter_file:
            contents = invite_letter_file.write(personal_invite)

# NOTE: by default, mode parameter will be equal to 'r' if no mode is specified
