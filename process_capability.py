import statistics
data = [10.1, 10.0, 10.2, 9.9, 10.1, 10.0, 10.2, 10.1]
lsl = float(input("Lower specification limit: "))
usl = float(input("Upper specification limit: "))
mean = statistics.mean(data)
sigma = statistics.stdev(data)
if usl <= lsl or sigma == 0:
    print("Check limits and data.")
else:
    cp = (usl-lsl)/(6*sigma)
    cpk = min((usl-mean)/(3*sigma), (mean-lsl)/(3*sigma))
    print("Cp =", cp, "Cpk =", cpk)
