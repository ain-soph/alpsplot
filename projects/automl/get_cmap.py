from matplotlib.cm import get_cmap
import numpy as np

cmap = get_cmap('coolwarm')


def float2int(num: float) -> int:
    return int(num*255+0.5)


def tuple2str(r: float, g: float, b: float, a: float = 1.0) -> str:
    assert a == 1.0
    return f'{int(float2int(r)):02X}{int(float2int(g)):02X}{int(float2int(b)):02X}'


a = [1.286, 1.509, 1.377, 1.455,
     1.288, 1.245, 1.231, 1.381,
     1.272, 1.115, 1.172, 1.125,
     1.259, 1.050, 1.115, 1.151, ]
a = np.array(a)
a -= a.min()
a /= a.max()
print(a)
b = [tuple2str(*(cmap(element))) for element in a]
print(b)
