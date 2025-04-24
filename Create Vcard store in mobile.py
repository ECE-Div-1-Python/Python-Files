

name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open("contact.vcf", "w") as file:
    file.write(vcard_content)

print("vCard created successfully.")
