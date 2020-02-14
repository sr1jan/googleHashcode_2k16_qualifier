from math import sqrt, ceil

# calculates euclidean distance
distance = lambda x, y: ceil(sqrt(abs(x[0]-y[0])**2 + abs(x[1]-y[1])**2))

if __name__ == '__main__':
    sim_info = list(map(int, input().strip().split()))
    p_type = int(input())
    pt_w = list(map(int, input().strip().split()))
    num_wh = int(input())

    # warehouses
    wh = {}
    for w in range(num_wh):
        loc = tuple(map(int, input().strip().split()))
        items = list(map(int, input().strip().split()))
        wh[w] = [loc, items]

    # drones
    drones = {}
    for d in range(sim_info[2]):
        drones[d] = [wh[0][0][0], wh[0][0][1]]

    # orders
    num_ord = int(input())
    orders = {}
    for ord in range(num_ord):
        loc = tuple(map(int, input().strip().split()))
        n_items = int(input())
        items = list(map(int, input().strip().split()))
        wh_with_items = {}
        for w in wh:
            l = []
            for i in items:
                if wh[w][1][i] is not 0:
                    l.append(i)
            wh_with_items[w] = l
        wh_itms = [(w,len(wh_with_items[w])) for w in wh_with_items if len(wh_with_items[w]) is not 0]
        wh_itms = sorted(wh_itms, key=lambda x: distance(wh[x[0]][0], loc))
        orders[ord] = [loc, items, wh_itms]

    # for ord in orders:
    #     l = orders[ord][1]
    #     orders[ord][1] = sorted(l, key=lambda )

    # sort_ords = sorted(orders, key=lambda x: x[1])

    # print(*sim_info)
    # print(p_type)
    # print(*pt_w)
    # print(num_wh)
    print(drones)
    print(wh, end='\n\n')
    for o in orders:
        print(f"{o} -> {orders[o]}")

    # print(f"dist: o1:w1 -> {distance(orders[1][0], wh[1][0])}")


