def main():
    # slicing = create a substring by extrating elements from another string
    #           indexing[] or slice()
    #           [start:stop:step]

    name = "Tien Dat";
   
    len1 = len(name)
    first_name = name[:3]; #Tie [0:3]
    last_name = name[4:]; # Dat [4:end]
    funky_name = name[0:8:2]; #or funky_name = name[::2] [0:end:2]
    reversed_name = name[::-1];
    first_name = name[:3];
    website1 =  "http://google.com";
    website2 =  "http://Facebook.com";
    print(first_name);
    print(last_name);
    print(funky_name );
    print(reversed_name); #taD neiT [0:end:-1]
   
    slice1 = slice(7,-4);
    #slice này giữ giá trị trong element
    print(website1[slice1])
    print(website2[slice1])


if __name__ == "__main__":
    main();


