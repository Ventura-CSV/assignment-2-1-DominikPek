def main():
    num_male = int(input('How many boys are there?'))
    num_female = int(input('How many girls are there?'))

    m_perc = (num_male / (num_male + num_female)) * 100
    f_perc = (num_female / (num_male + num_female)) * 100

    print(f'Percentage of males: {m_perc}')
    print(f'Percentage of females: {f_perc}')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
