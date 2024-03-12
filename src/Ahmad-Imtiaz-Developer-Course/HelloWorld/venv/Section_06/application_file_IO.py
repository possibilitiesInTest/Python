# myfile = open('C:/Users/goura/Downloads/sample.txt')
#
# content = myfile.read()
# print(content)
#
# myfile.seek(0)
# print("\n-------------------\n")
#
# data = myfile.read()
# myfile.seek(0)
#
# content_list = myfile.readlines()
# myfile.close()
# print(content_list)

# with open('C:/Users/goura/Downloads/sample.txt', mode='w+') as my_file:
#     my_file.write("\nYOYO")
#
# appended_content = open('C:/Users/goura/Downloads/sample.txt')
#
# print(appended_content.read())

try:
    file_3 = open("C:/Users/goura/Downloads/sample3.txt", mode="r")
    try:
        print(file_3.read())
    except IOError:
        print("Issue working with the file")
    # except FileNotFoundError:
    #     print("file does not exist: FileNotFoundError")
    # except TypeError:
    #     print("there was a type error")
    # except:
    #     print("Error Occurred Logging to the system")
    finally:
        if file_3 != None:
            file_3.close()
        print("This will always run regardless of exceptions")
except:
    print("Some inner defined error happened")

print("this file was run . . .")