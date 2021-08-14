
from KnowBasic1_1 import emailProcess, PrintEmail


def main():
    email_List = ['asd@gmail.com', 'qwe@gmail.com', 'zxc@gmail.com']
    for email in email_List:
        email_username, email_domain = emailProcess(email)
        PrintEmail(email_username, email_domain)


if __name__ == "__main__":
    main()
