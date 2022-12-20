def computepay(hours, rate):
    if hours>40:
        rate=rate*1.5
        wage=rate*hours
    else:
        wage=rate*hours

    print("Liczba przepracowanych godzin: ", hours)
    print("Stawka godzinowa: ", rate)
    print("Zarobiles ", hours*rate)


computepay(45, 10)