phone=int(input("enter the phone:+91 "))
email=input("enter the email:")
with open("files/contact.vcf","w") as f:
    f.write(f"Phone number: {phone}\n")
    f.write(f"email: {email}\n ")
print("your contact detail saved successfully!")


