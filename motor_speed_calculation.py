# Calculate rpm from pulse count; no motor hardware is controlled.
pulses = int(input("Pulses counted: "))
seconds = float(input("Measurement time (s): "))
ppr = int(input("Pulses per revolution: "))
if seconds <= 0 or ppr <= 0:
    print("Time and pulses per revolution must be positive.")
else:
    print("Speed (rpm) =", pulses / ppr * 60 / seconds)
