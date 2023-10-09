def fake_bin(x):
    return ''.join(('1','0')[i < '5'] for i in x)
