def emailProcess(email):

    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]

    return [email_username, email_domain]


def PrintEmail(email1, email2):
    print(f"This is username {email1} and doamin {email2}")


def main():
    email = input("Please enter your email address: ").strip()
    # print(f"Hello email {email}")
    email_username, email_domain = emailProcess(email)
    PrintEmail(email_username, email_domain)


if __name__ == "__main__":
    main()
