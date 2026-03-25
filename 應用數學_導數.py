def f(x):
    return x ** 2


def forward_diff(val, step):
    return (f(val + step) - f(val)) / step

def backward_diff(val, step):
    return (f(val) - f(val - step)) / step

def central_diff(val, step):
    return (f(val + step) - f(val - step)) / (2 * step)

x_val = 2
h_values = [0.1, 0.01, 0.001]
true_derivative = 2 * x_val

for h_step in h_values:
    fwd = forward_diff(x_val, h_step)
    bwd = backward_diff(x_val, h_step)
    cen = central_diff(x_val, h_step)

    print(f"x = {x_val}, h = {h_step}")
    print(f"前向差分: {fwd:.6f}")
    print(f"後向差分: {bwd:.6f}")
    print(f"中央差分: {cen:.6f}")
    print(f"真實導數: {true_derivative}\n")