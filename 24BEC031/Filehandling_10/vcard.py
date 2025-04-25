def create_vcf():

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    add = input("Enter address: ")


    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:{add}
END:VCARD
"""

    # Save the vCard to a file
    fname = "files/contact.vcf"
    with open(fname, 'w') as file:
        file.write(vcard)

    print(f"vCard created successfully! You can store  '{fname}' in your cell.")

create_vcf()
