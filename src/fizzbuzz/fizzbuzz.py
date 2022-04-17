def main():
    pass

for counter in range(100) :
    print(counter)
    if counter %3 == 0 and counter%5 == 0:
        print('fizzbuzz')
    elif counter %3 == 0:
        print('fizz')
    elif counter%5 == 0:
        print("buzz")
    else:
        print('')

    # if counter %3 == 0 and counter %5 != 0:
    #     print('fizz')
    # elif counter %5 == 0 and counter %3 != 0:
    #     print('buzz')
    # elif counter %3 == 0 and counter%5 == 0:
    #     print("fizzbuzz")
    # else:
    #     print('')



if __name__ == '__main__':
    main()