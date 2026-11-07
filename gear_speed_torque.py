# Gear ratio is defined as input speed / output speed.
rpm_in = float(input("Input speed (rpm): "))
torque_in = float(input("Input torque (N.m): "))
ratio = float(input("Gear ratio (input/output): "))
if ratio <= 0:
    print("Gear ratio must be positive.")
else:
    print("Output speed (rpm) =", rpm_in / ratio)
    print("Ideal output torque (N.m) =", torque_in * ratio)
    print("Note: real torque is lower because of losses.")
