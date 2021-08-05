from typing import Counter


def main():
    # dasdasd Không cần kiểu khai báo biến như java hoặc các ngôn ngữ khác
    # Counter = 100;
    # miles = 1000.0;
    # name = "TienDat";
    # print(Counter);
    # print(miles);
    # print(name);

    # Multiple Assignment Nếu 2 phần tử giống nhau cùng khai bảo thì python sẻ lấy phần tử cuối cùng
    # a = b = c = 1;
    # z,x,c = 1,2,"TienDat";
    # print(a,b,c);

    #Multi-Line Stament ( "/")
    # total = item_one + \
    #         item_two + \
    #         item_three;

    # Quotation in Python
    # word = 'Word';
    # sentence = "This is a sentence.";
    # paragraph = """This is a paragraph. It is made up 
    #         of multiple lines and sentence""";

    #String Python

    # str = "Hello World";

    # print(str); #print String
    # print (str[0]) #print first element of String
    # print (str[2:5]) # Prints characters starting from 3rd to 5th
    # print (str[2:]) # Prints string starting from 3rd character
    # print (str * 2) # Prints string two times
    # print (str + " TEST") # Prints concatenated string


    #List Python

    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']

    print(list)          # Prints complete list
    print (list[0])       # Prints first element of the list
    print (list[1:3])     # Prints elements starting from 2nd till 3rd 
    print (list[2:])       # Prints elements starting from 3rd element
    print (tinylist * 2)  # Prints list two times
    print (list + tinylist) # Prints concatenated lists


if __name__ == "__main__":
    main();