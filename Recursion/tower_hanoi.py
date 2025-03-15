def towerOfHanoi(n, s_pole, d_pole, i_pole):
    if n == 1:
        print("Move disc 1 from pole", s_pole, "to pole", d_pole)
        return
    towerOfHanoi(n-1, s_pole, i_pole, d_pole)
    print("Move disc", n, "from pole", s_pole, "to pole", d_pole)
    towerOfHanoi(n-1, i_pole, d_pole, s_pole)


n = 3
towerOfHanoi(n, 'A', 'C', 'B')



# s_pole = source pole
# d_pole = destination pole
# i_pole = intermediate pole