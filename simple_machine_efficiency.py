# Efficiency (%) = (Mechanical Advantage / Velocity Ratio) * 100
load_n = float(input("Load (N): "))
effort_n = float(input("Effort (N): "))
vr = float(input("Velocity ratio: "))
if effort_n <= 0 or vr <= 0:
    print("Effort and velocity ratio must be positive.")
else:
    ma = load_n / effort_n
    print("Mechanical advantage =", ma)
    print("Efficiency (%) =", ma / vr * 100)
