import matplotlib.pyplot as plt
strain = [0, .0005, .001, .0015, .002, .003, .005]
stress_mpa = [0, 100, 200, 300, 400, 430, 450]
plt.plot(strain, stress_mpa, marker="o")
plt.xlabel("Engineering strain (mm/mm)")
plt.ylabel("Engineering stress (MPa)")
plt.title("Illustrative stress-strain curve")
plt.grid(True); plt.show()
