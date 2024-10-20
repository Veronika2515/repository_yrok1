try:
    print('start code')
    # print(error)
    print("No errors")
except NameError as error:
    print(error)
else:
    print("I'm else")
finally:
    print("Finnaly code")
    