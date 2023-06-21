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
    m = int(input('Input the number of males in the class: '))
    f = int(input('Input the number of females in the class: '))


    #Calculate the total number of students
    total = f + m

    #Find the percentage of female and male students
    f_perc = (float(f)/total)
    m_perc = (float(m)/total)

    #Print all the values
    print(f'\nThe total number of students: \t {total}')
    print(f'The number of males and females: \t {m} \t {f}')
    print(f'The percentage of males and females: \t {m_perc:.2%} \t {f_perc:.2%}')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
