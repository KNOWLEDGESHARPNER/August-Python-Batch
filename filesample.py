
# f = open('D:/sample.txt','a')

# # f.write('1.hello Guys\n')
# # f.write('2.We are learning write mode')
# # f.write('3. This is my latest data')
# f.write('6.append mode write the content at the end of the file\n')
# f.close()

# reading file content in read mode

try:
    f = open('D:/sample.txt','r')

    data = f.readlines()
    print(data)
    print(data[0])
    print(data[1])
    # print(data[2])
    # f.close()# this will not reach # it is not optimal
except FileNotFoundError as e:
    print(e)
    # f.close()## it is not optimal
except:
    print('Something went wrong please try again')
    # f.close()# it is not optimal
finally:
    try:

        f.close()
        print('file closed successfully!!')
    except NameError as e:
        print(e)


    

print('File and exceptions handling')