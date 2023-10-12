"""
소프트웨어와 문제해결(003) - Plagiarism project
이름: 허버트
학번: 2020110876


"""

# Get the number of files the user wants to compare
file_number = int(input("How many files would you like to compare? "))  # input the number of files you want to compare

while True:
    if file_number <= 1 or file_number > 5:  # keep prompting the user to input the right value
        print("Input any number from 2 to 5!")
        file_number = int(input("How many files would you like to compare? "))
    else:
        break

# receiving text file names from the user and storing them in a list
file = []
x = 0
while x < file_number:
    file.append(input("Enter the text file name: "))  # stores the text file names in a list
    x += 1

# opening files, reading them and counting common words
commonAB = 0
commonAC = 0
commonAD = 0
commonAE = 0
commonBC = 0
commonBD = 0
commonBE = 0
commonCD = 0
commonCE = 0
commonDE = 0

if len(file) == 2:
    infile1 = open(file[0]).read()  # opens the file and reads it
    infile2 = open(file[1]).read()

    doc_A = infile1.split()  # split the files into a list of words
    doc_B = infile2.split()

    for word in doc_A:
        if word in doc_B:  # Checks for similar words in doc_A and doc_B
            commonAB += 1

    # Calculating similarity
    no_AB = len(doc_A) + len(doc_B)  # Total words in doc_A and doc_B

    sim_AB = (commonAB / (no_AB - commonAB)) * 100  # similarity percentage

    print(f"{file[0]} and {file[1]} have a similarity of {sim_AB:.1f}%")


elif len(file) == 3:
    infile1 = open(file[0]).read()
    infile2 = open(file[1]).read()
    infile3 = open(file[2]).read()

    doc_A = infile1.split()
    doc_B = infile2.split()
    doc_C = infile3.split()

    for word in doc_A:  # Checks for similar words
        if word in doc_B:
            commonAB += 1
        if word in doc_C:
            commonAC += 1

    for word in doc_B:  # Checks for similar words
        if word in doc_C:
            commonBC += 1

    # Calculating similarity
    no_AB = len(doc_A) + len(doc_B)  # Total words in doc_A and doc_B
    sim_AB = (commonAB / (no_AB - commonAB)) * 100  # similarity percentage

    no_AC = len(doc_A) + len(doc_C)
    sim_AC = (commonAC / (no_AC - commonAC)) * 100

    no_BC = len(doc_B) + len(doc_C)
    sim_BC = (commonBC / (no_BC - commonBC)) * 100

    # checking maximum similarity and printing the most similar
    max_sim = max(sim_AB, sim_AC, sim_BC)

    if sim_AB == max_sim:
        print(f"{file[0]} and {file[1]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AC == max_sim:
        print(f"{file[0]} and {file[2]} have the highest similarity: {max_sim:.1f}%")
    elif sim_BC == max_sim:
        print(f"{file[1]} and {file[2]} have the highest similarity: {max_sim:.1f}%")

elif len(file) == 4:
    infile1 = open(file[0]).read()
    infile2 = open(file[1]).read()
    infile3 = open(file[2]).read()
    infile4 = open(file[3]).read()

    doc_A = infile1.split()
    doc_B = infile2.split()
    doc_C = infile3.split()
    doc_D = infile4.split()

    for word in doc_A:  # Checks for similar words
        if word in doc_B:
            commonAB += 1
        if word in doc_C:
            commonAC += 1
        if word in doc_D:
            commonAD += 1

    for word in doc_B:  # Checks for similar words
        if word in doc_C:
            commonBC += 1
        if word in doc_D:
            commonBD += 1

    for word in doc_C:  # Checks for similar words
        if word in doc_D:
            commonCD += 1

    # Calculating similarity
    no_AB = len(doc_A) + len(doc_B)  # total words in doc_A and doc_B
    sim_AB = (commonAB / (no_AB - commonAB)) * 100  # similarity percentage

    no_AC = len(doc_A) + len(doc_C)
    sim_AC = (commonAC / (no_AC - commonAC)) * 100

    no_AD = len(doc_A) + len(doc_D)
    sim_AD = (commonAD / (no_AD - commonAD)) * 100

    no_BC = len(doc_B) + len(doc_C)
    sim_BC = (commonBC / (no_BC - commonBC)) * 100

    no_BD = len(doc_B) + len(doc_D)
    sim_BD = (commonBD / (no_BD - commonBD)) * 100

    no_CD = len(doc_C) + len(doc_D)
    sim_CD = (commonCD / (no_CD - commonCD)) * 100

    # checking maximum similarity and printing the most similar
    max_sim = max(sim_AB, sim_AC, sim_AD, sim_BC, sim_BD, sim_CD)

    if sim_AB == max_sim:
        print(f"{file[0]} and {file[1]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AC == max_sim:
        print(f"{file[0]} and {file[2]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AD == max_sim:
        print(f"{file[0]} and {file[3]} have the highest similarity: {max_sim:.1f}%")
    elif sim_BC == max_sim:
        print(f"{file[1]} and {file[2]} have the highest similarity: {max_sim:.1f}%")
    elif sim_BD == max_sim:
        print(f"{file[1]} and {file[3]} have the highest similarity: {max_sim:.1f}%")
    elif sim_CD == max_sim:
        print(f"{file[2]} and {file[3]} have the highest similarity: {max_sim:.1f}%")

elif len(file) == 5:
    infile1 = open(file[0]).read()
    infile2 = open(file[1]).read()
    infile3 = open(file[2]).read()
    infile4 = open(file[3]).read()
    infile5 = open(file[4]).read()

    doc_A = infile1.split()
    doc_B = infile2.split()
    doc_C = infile3.split()
    doc_D = infile4.split()
    doc_E = infile5.split()

    for word in doc_A:  # Checks for similar words
        if word in doc_B:
            commonAB += 1
        if word in doc_C:
            commonAC += 1
        if word in doc_D:
            commonAD += 1
        if word in doc_E:
            commonAE += 1

    for word in doc_B:  # Checks for similar words
        if word in doc_C:
            commonBC += 1
        if word in doc_D:
            commonBD += 1
        if word in doc_E:
            commonBE += 1

    for word in doc_C:  # Checks for similar words
        if word in doc_D:
            commonCD += 1
        if word in doc_E:
            commonCE += 1

    for word in doc_D:  # Checks for similar words
        if word in doc_E:
            commonDE += 1

    # Calculating similarity
    no_AB = len(doc_A) + len(doc_B)  # no. of words in doc_A
    sim_AB = (commonAB / (no_AB - commonAB)) * 100  # similarity percentage

    no_AC = len(doc_A) + len(doc_C)
    sim_AC = (commonAC / (no_AC - commonAC)) * 100

    no_AD = len(doc_A) + len(doc_D)
    sim_AD = (commonAD / (no_AD - commonAD)) * 100

    no_AE = len(doc_A) + len(doc_E)
    sim_AE = (commonAE / (no_AE - commonAE)) * 100

    no_BC = len(doc_B) + len(doc_C)
    sim_BC = (commonBC / (no_BC - commonBC)) * 100

    no_BD = len(doc_B) + len(doc_D)
    sim_BD = (commonBD / (no_BD - commonBD)) * 100

    no_BE = len(doc_B) + len(doc_E)
    sim_BE = (commonBE / (no_BE - commonBE)) * 100

    no_CD = len(doc_C) + len(doc_D)
    sim_CD = (commonCD / (no_CD - commonCD)) * 100

    no_CE = len(doc_C) + len(doc_E)
    sim_CE = (commonCE / (no_CE - commonCE)) * 100

    no_DE = len(doc_D) + len(doc_E)
    sim_DE = (commonDE / (no_DE - commonDE)) * 100

    # checking maximum similarity and printing the most similar
    max_sim = max(sim_AB, sim_AC, sim_AD, sim_AE, sim_BC, sim_BD, sim_BE, sim_CD, sim_CE, sim_DE)

    if sim_AB == max_sim:
        print(f"{file[0]} and {file[1]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AC == max_sim:
        print(f"{file[0]} and {file[2]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AD == max_sim:
        print(f"{file[0]} and {file[3]} have the highest similarity: {max_sim:.1f}%")
    elif sim_AE == max_sim:
        print(f"{file[0]} and {file[4]} have the highest similarity : {max_sim:.1f}%")
    elif sim_BC == max_sim:
        print(f"{file[1]} and {file[2]} have the highest similarity: {max_sim:.1f}%")
    elif sim_BD == max_sim:
        print(f"{file[1]} and {file[3]} have the highest similarity: {max_sim:.1f}%")
    elif sim_BE == max_sim:
        print(f"{file[1]} and {file[4]} have the highest similarity: {max_sim:.1f}%")
    elif sim_CD == max_sim:
        print(f"{file[2]} and {file[3]} have the highest similarity: {max_sim:.1f}%")
    elif sim_CE == max_sim:
        print(f"{file[2]} and {file[4]} have the highest similarity: {max_sim:.1f}%")
    elif sim_DE == max_sim:
        print(f"{file[3]} and {file[4]} have the highest similarity: {max_sim:.1f}%")
