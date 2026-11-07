c_values = [0, 20, 25, 37, 100]
f_values = [(c * 9 / 5) + 32 for c in c_values]
for c, f in zip(c_values, f_values):
    print(f"{c} °C = {f:.1f} °F")
