import pandas as pd
from datetime import datetime
import networkx as nx

def k_step_pic_E(from_cam, to_cam,
                from_sam, to_sam,
                repo, td_max, k=1):
    pic_E = []
    pic_L = []
    SPL_list = []
    Date_list = []

    d = {'from': from_cam, 'to': to_cam}
    df = pd.DataFrame(d)
    G_cam = nx.from_pandas_edgelist(df=df,
                                    source='from', target='to',
                                    create_using=nx.DiGraph())

    for i in range(len(from_sam)):
        from_date = datetime.strptime(str(repo[from_sam[i]]), "%Y%m%d")
        to_date = datetime.strptime(str(repo[to_sam[i]]), "%Y%m%d")
        diff_day = from_date - to_date
        diff_date = diff_day.days

        if abs(diff_date) <= td_max:
            if diff_date <= 0:
                E = from_sam[i]
                L = to_sam[i]
            else:
                E = to_sam[i]
                L = from_sam[i]
            if E != L:
                idx_E = [e for e, value in enumerate(
                    from_cam) if value == E]

                chk = 0
                for idx_e in idx_E:
                    if to_cam[idx_e] == L:
                        chk += 1
                        break
                    else:
                        pass
                if chk == 0:
                    try:
                        SPL = nx.algorithms.shortest_path_length(
                            G=G_cam, source=E, target=L, method='dijkstra')
                    except (nx.NetworkXNoPath, nx.NodeNotFound):
                        SPL = -999

                    if SPL == (int(k) + 1):
                        SPL_list.append(SPL-1)
                        Date_list.append(abs(diff_date))
                        pic_E.append(E)
                        pic_L.append(L)
                        
    d = {'P_E': pic_E, 'P_L': pic_L}
    df = pd.DataFrame(d)
    results = df.drop_duplicates(['P_E', 'P_L'])
    return results

# +
if __name__ == '__main__':
    from_cam = ['P1', 'P1', 'P2', 'P2', 'P3', 'P3', 'P4', 'P7', 'P8', 'P10']
    to_cam = ['P2', 'P4', 'P3', 'P7', 'P4', 'P6', 'P5', 'P8', 'P9', 'P9']
    from_sam = ['P1', 'P1', 'P1', 'P1', 'P1']
    to_sam = ['P3', 'P5', 'P6', 'P9', 'P10']
    repo = {'P1': 20050101,
            'P2': 20070101,
            'P3': 20100101,
            'P4': 20150101,
            'P5': 20200101,
            'P6': 20150101,
            'P7': 20100101,
            'P8': 20150101,
            'P9': 20200101,
            'P10': 20150101}

    results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                           from_sam=from_sam, to_sam=to_sam,
                           repo=repo, td_max=365*20, k=1)
    print("* * 1step-PIC * * \n", results, "\n")

    results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                           from_sam=from_sam, to_sam=to_sam,
                           repo=repo, td_max=365*20, k=2)
    print("* * 2step-PIC * * \n", results, "\n")

    results = k_step_pic_E(from_cam=from_cam, to_cam=to_cam,
                           from_sam=from_sam, to_sam=to_sam,
                           repo=repo, td_max=365*20, k=3)
    print("* * 3step-PIC * * \n", results, "\n")
