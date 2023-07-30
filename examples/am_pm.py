
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

def timeConversion(s):

    for i in s:

        if i == "P":
            PM = s.replace("PM", "")
            PM = PM.split(":")
            PM = [int(i) for i in PM]

            if PM[0] == 12:
                PM = [str(i) for i in PM]

                for j in PM:
                    if len(j) == 1:
                        PM[PM.index(j)] = "0" + j
                    else:
                        pass
                PM = ":".join(PM)
                return PM

            else:
                PM[0] += 12

                PM = [str(i) for i in PM]
                for j in PM:
                    if len(j) == 1:
                        PM[PM.index(j)] = "0" + j
                    else:
                        pass
                PM = ":".join(PM)
                return PM

        elif i == "A":

            AM = s.replace("AM", "")
            AM = AM.split(":")
            AM = [int(i) for i in AM]

            if AM[0] < 12:
                AM = [str(i) for i in AM]

                for j in AM:
                    if len(j) == 1:
                        AM[AM.index(j)] = "0" + j
                    else:
                        pass
                AM = ":".join(AM)
                return AM

            else:
                AM[0] -= 12
                AM = [str(i) for i in AM]

                for j in AM:
                    if len(j) == 1:
                        print(1)
                        AM[AM.index(j)] = "0" + j
                    else:
                        pass
                AM = ":".join(AM)
                return AM


def main():
    s = "07:05:05AM"
    print(timeConversion(s))

main()