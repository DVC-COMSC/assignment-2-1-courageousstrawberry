def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    #Set female and male variables
    male = int(input('Input the number of males in the class: '))
    fem = int(input('Input the number of females in the class: '))


    #Calculate the total number of students
    total = fem + male

    #Find the percentage of female and male students
    f_perc = (fem/total)
    m_perc = (male/total)

    #Print all the values
    print(f'\nThe total number of students: \t {total}')
    print(f'The number of males and females: \t {male} \t {fem}')
    print(f'The percentage of males and females: \t {m_perc:.2%} \t {f_perc:.2%}')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
