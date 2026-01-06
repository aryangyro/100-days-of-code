
with open("/Users/aryanpanwar/Downloads/Mail Merge Project Completed/Input/Names/invited_names.txt") as file:
    names = file.readlines()

    
with open("/Users/aryanpanwar/Downloads/Mail Merge Project Completed/Input/Letters/starting_letter.txt")as file2:
    content = file2.read()
    for i in names:
        strip_name = i.strip()
        new_letter = content.replace("[name]",strip_name)
        with open(f"/Users/aryanpanwar/Downloads/Mail Merge Project Completed/Output/ReadyToSend/letter_for_{strip_name}.docx", mode="w") as file3:
            file3.write(f"{new_letter}")
    

