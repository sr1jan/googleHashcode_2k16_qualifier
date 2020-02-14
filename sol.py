if __name__ == '__main__':
    sim_info = list(map(int, input().strip().split()))
    p_type = int(input())
    pt_w = list(map(int, input().strip().split()))
    num_wh = int(input())

    wh = {}
    for w in range(num_wh):
        loc = tuple(map(int, input().strip().split()))
        items = list(map(int, input().strip().split()))
        wh[w] = [loc, items]

    num_ord = int(input())
    orders = {}
    for ord in range(num_ord):
        loc = tuple(map(int, input().strip().split()))
        n_items = int(input())
        items = list(map(int, input().strip().split()))
        orders[ord] = [loc, items]

    # print(*sim_info)
    # print(p_type)
    # print(*pt_w)
    print(num_wh)
    print(wh)
    print(orders)


